#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
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


def discover_spec_files(evals_dir: Path) -> list[Path]:
    files = []
    for path in evals_dir.rglob("*.json"):
        if "outputs" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run all saved eval specs under tools/evals."
    )
    parser.add_argument(
        "--spec-dir",
        default="tools/evals",
        help="Directory containing eval spec JSON files.",
    )
    parser.add_argument(
        "--results-log",
        default="logs/eval-results.jsonl",
        help="Path to append summary results as JSONL.",
    )
    args = parser.parse_args()

    root = repo_root()
    evals_dir = resolve_repo_path(root, args.spec_dir)
    results_log = resolve_repo_path(root, args.results_log)
    results_log.parent.mkdir(parents=True, exist_ok=True)

    spec_files = discover_spec_files(evals_dir)
    if not spec_files:
        print(f"No eval specs found under {evals_dir}.")
        return 1

    all_passed = True
    total = 0
    passed = 0

    for spec_path in spec_files:
        spec = load_json(spec_path)
        output_rel = spec.get("output_file") or spec.get("suggested_output_file")
        output_path = root / output_rel if output_rel else None

        total += 1

        if not output_path or not output_path.exists():
            record = {
                "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                "id": spec.get("id"),
                "title": spec.get("title"),
                "spec_path": str(spec_path.relative_to(root)),
                "output_file": str(output_path.relative_to(root)) if output_path else None,
                "overall_pass": False,
                "error": "missing_output_file",
            }
            with results_log.open("a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

            print(
                f"[FAIL] {spec.get('id')} - missing output file: "
                f"{output_path.relative_to(root) if output_path else 'not set'}"
            )
            all_passed = False
            continue

        text = read_text(output_path)
        result = validate_text(spec, text)
        result_record = {
            "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "id": result["id"],
            "title": result["title"],
            "spec_path": str(spec_path.relative_to(root)),
            "output_file": str(output_path.relative_to(root)),
            "overall_pass": result["overall_pass"],
            "passed_checks": result["passed_checks"],
            "total_checks": result["total_checks"],
            "nonempty_line_count": result["nonempty_line_count"],
        }

        with results_log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(result_record, ensure_ascii=False) + "\n")

        if result["overall_pass"]:
            passed += 1
            print(f"[PASS] {result['id']} ({result['passed_checks']}/{result['total_checks']})")
        else:
            all_passed = False
            print(f"[FAIL] {result['id']} ({result['passed_checks']}/{result['total_checks']})")

    print()
    print(f"Summary: {passed}/{total} evals passed")
    print(f"Detailed results log: {results_log.relative_to(root)}")

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
