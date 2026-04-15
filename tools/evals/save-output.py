#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from eval_lib import load_json, validate_text  # noqa: E402


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def resolve_repo_path(root: Path, path_str: str) -> Path:
    path = Path(path_str)
    if path.is_absolute():
        return path
    return root / path


def discover_spec_files(evals_dir: Path) -> list[Path]:
    files = []
    for path in evals_dir.rglob("*.json"):
        if "outputs" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def load_spec_by_prompt(root: Path, prompt_path_str: str, spec_dir_str: str) -> tuple[Path, dict[str, Any]]:
    prompt_path = str(resolve_repo_path(root, prompt_path_str).relative_to(root)).replace("\\", "/")
    spec_dir = resolve_repo_path(root, spec_dir_str)
    matches: list[tuple[Path, dict[str, Any]]] = []

    for spec_path in discover_spec_files(spec_dir):
        spec = load_json(spec_path)
        prompt_file = spec.get("prompt_file")
        if prompt_file == prompt_path:
            matches.append((spec_path, spec))

    if not matches:
        raise ValueError(f"No eval spec found for prompt file: {prompt_path}")
    if len(matches) > 1:
        joined = ", ".join(str(path.relative_to(root)) for path, _ in matches)
        raise ValueError(f"Multiple eval specs matched prompt file {prompt_path}: {joined}")

    return matches[0]


def read_input_text(args: argparse.Namespace, root: Path) -> str:
    if args.output_text is not None:
        return args.output_text
    if args.input_file:
        return resolve_repo_path(root, args.input_file).read_text(encoding="utf-8")
    if args.stdin:
        return sys.stdin.read()
    raise ValueError("Provide one of --output-text, --input-file, or --stdin")


def print_result(result: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    status = "PASS" if result["overall_pass"] else "FAIL"
    print(f"[{status}] {result['id']} - {result['title']}")
    print(f"Checks: {result['passed_checks']}/{result['total_checks']}")
    print(f"Non-empty lines: {result['nonempty_line_count']}")
    for item in result["results"]:
        marker = "PASS" if item["passed"] else "FAIL"
        print(f"{marker} {item['name']}: {item['message']}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Save a Copilot response into tools/evals/outputs and optionally validate it."
    )
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--spec", help="Path to the eval JSON spec.")
    source_group.add_argument(
        "--prompt",
        help="Prompt file path. The tool will find the matching spec via its prompt_file field.",
    )
    parser.add_argument(
        "--spec-dir",
        default="tools/evals",
        help="Directory containing eval spec JSON files when using --prompt.",
    )
    parser.add_argument(
        "--output-file",
        help="Override where to save the output text. Defaults to the spec's output_file or suggested_output_file.",
    )
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--output-text", help="Raw output text passed directly on the command line.")
    input_group.add_argument("--input-file", help="Read output text from a file.")
    input_group.add_argument("--stdin", action="store_true", help="Read output text from standard input.")
    parser.add_argument("--validate", action="store_true", help="Validate immediately after saving.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON when validating.")

    args = parser.parse_args()

    root = repo_root()
    try:
        if args.spec:
            spec_path = resolve_repo_path(root, args.spec)
            spec = load_json(spec_path)
        else:
            spec_path, spec = load_spec_by_prompt(root, args.prompt, args.spec_dir)

        output_rel = args.output_file or spec.get("output_file") or spec.get("suggested_output_file")
        if not output_rel:
            parser.error("The spec does not define output_file or suggested_output_file, and --output-file was not provided.")

        output_path = resolve_repo_path(root, output_rel)
        text = read_input_text(args, root)
    except ValueError as exc:
        parser.error(str(exc))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    print(f"Saved output to {output_path.relative_to(root)}")

    if not args.validate:
        return 0

    result = validate_text(spec, text)
    result["spec_path"] = str(spec_path.relative_to(root))
    result["output_file"] = str(output_path.relative_to(root))
    print_result(result, args.json)
    return 0 if result["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
