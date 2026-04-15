#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from eval_lib import load_json, read_text, validate_text  # noqa: E402


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def resolve_repo_path(root: Path, path_str: str) -> Path:
    path = Path(path_str)
    if path.is_absolute():
        return path
    return root / path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate one saved Copilot output against one eval spec."
    )
    parser.add_argument(
        "--spec",
        required=True,
        help="Path to the eval JSON spec.",
    )
    parser.add_argument(
        "--output-file",
        help="Path to the saved model output text file.",
    )
    parser.add_argument(
        "--output-text",
        help="Raw output text passed directly on the command line.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON.",
    )

    args = parser.parse_args()

    root = repo_root()
    spec_path = resolve_repo_path(root, args.spec)
    spec = load_json(spec_path)

    if args.output_file:
        output_path = resolve_repo_path(root, args.output_file)
        text = read_text(output_path)
    elif args.output_text is not None:
        output_path = None
        text = args.output_text
    else:
        suggested_output = spec.get("output_file") or spec.get("suggested_output_file")
        if not suggested_output:
            parser.error("Provide either --output-file or --output-text")

        output_path = resolve_repo_path(root, suggested_output)
        if not output_path.exists():
            parser.error(
                "No output source provided and the spec's saved output file does not exist: "
                f"{output_path}"
            )
        text = read_text(output_path)

    result = validate_text(spec, text)
    result["spec_path"] = str(spec_path.relative_to(root))
    result["output_file"] = str(output_path.relative_to(root)) if output_path else None

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if result["overall_pass"] else "FAIL"
        print(f"[{status}] {result['id']} - {result['title']}")
        print(f"Checks: {result['passed_checks']}/{result['total_checks']}")
        print(f"Non-empty lines: {result['nonempty_line_count']}")
        for item in result["results"]:
            marker = "PASS" if item["passed"] else "FAIL"
            print(f"{marker} {item['name']}: {item['message']}")

    return 0 if result["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
