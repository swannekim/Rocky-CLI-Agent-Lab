#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re
from typing import Any


@dataclass
class CheckResult:
    name: str
    passed: bool
    message: str


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def _normalized(value: str, case_insensitive: bool) -> str:
    return value.lower() if case_insensitive else value


def _nonempty_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def _contains(haystack: str, needle: str, case_insensitive: bool) -> bool:
    return _normalized(needle, case_insensitive) in _normalized(haystack, case_insensitive)


def _count_occurrences(haystack: str, needle: str, case_insensitive: bool) -> int:
    return _normalized(haystack, case_insensitive).count(_normalized(needle, case_insensitive))


def _line_startswith_any(lines: list[str], prefixes: list[str], case_insensitive: bool) -> bool:
    normalized_lines = [_normalized(line, case_insensitive) for line in lines]
    normalized_prefixes = [_normalized(prefix, case_insensitive) for prefix in prefixes]
    return any(
        line.startswith(prefix)
        for line in normalized_lines
        for prefix in normalized_prefixes
    )


def validate_text(spec: dict[str, Any], text: str) -> dict[str, Any]:
    checks = spec.get("checks", {})
    case_insensitive = checks.get("case_insensitive", True)
    lines = _nonempty_lines(text)
    results: list[CheckResult] = []

    def add(name: str, passed: bool, message: str) -> None:
        results.append(CheckResult(name=name, passed=passed, message=message))

    min_lines = checks.get("min_nonempty_lines")
    if min_lines is not None:
        passed = len(lines) >= int(min_lines)
        add(
            "min_nonempty_lines",
            passed,
            f"Expected at least {min_lines} non-empty lines, got {len(lines)}.",
        )

    max_lines = checks.get("max_nonempty_lines")
    if max_lines is not None:
        passed = len(lines) <= int(max_lines)
        add(
            "max_nonempty_lines",
            passed,
            f"Expected at most {max_lines} non-empty lines, got {len(lines)}.",
        )

    for needle in checks.get("required_substrings", []):
        passed = _contains(text, needle, case_insensitive)
        add(
            f"required_substring:{needle}",
            passed,
            f"Required substring {'found' if passed else 'missing'}: {needle}",
        )

    for idx, group in enumerate(checks.get("required_any_of", []), start=1):
        found = any(_contains(text, item, case_insensitive) for item in group)
        add(
            f"required_any_of:{idx}",
            found,
            f"Expected at least one of {group}; {'found' if found else 'none found'}.",
        )

    for needle in checks.get("banned_substrings", []):
        passed = not _contains(text, needle, case_insensitive)
        add(
            f"banned_substring:{needle}",
            passed,
            f"Banned substring {'not present' if passed else 'present'}: {needle}",
        )

    for phrase, max_allowed in checks.get("max_occurrences", {}).items():
        count = _count_occurrences(text, phrase, case_insensitive)
        passed = count <= int(max_allowed)
        add(
            f"max_occurrences:{phrase}",
            passed,
            f"Expected at most {max_allowed} occurrences of '{phrase}', got {count}.",
        )

    for prefix in checks.get("required_line_prefixes", []):
        found = _line_startswith_any(lines, [prefix], case_insensitive)
        add(
            f"required_line_prefix:{prefix}",
            found,
            f"Expected a line starting with '{prefix}'; {'found' if found else 'not found'}.",
        )

    for idx, group in enumerate(checks.get("required_line_prefixes_any_of", []), start=1):
        found = _line_startswith_any(lines, group, case_insensitive)
        add(
            f"required_line_prefixes_any_of:{idx}",
            found,
            f"Expected a line starting with one of {group}; {'found' if found else 'not found'}.",
        )

    for pattern in checks.get("must_match_regex", []):
        matched = re.search(pattern, text, flags=re.IGNORECASE if case_insensitive else 0) is not None
        add(
            f"must_match_regex:{pattern}",
            matched,
            f"Regex {'matched' if matched else 'did not match'}: {pattern}",
        )

    for pattern in checks.get("must_not_match_regex", []):
        matched = re.search(pattern, text, flags=re.IGNORECASE if case_insensitive else 0) is not None
        passed = not matched
        add(
            f"must_not_match_regex:{pattern}",
            passed,
            f"Regex {'not present' if passed else 'present'}: {pattern}",
        )

    passed_count = sum(1 for r in results if r.passed)
    total_count = len(results)
    overall_pass = all(r.passed for r in results) if results else False

    return {
        "id": spec.get("id"),
        "title": spec.get("title"),
        "overall_pass": overall_pass,
        "passed_checks": passed_count,
        "total_checks": total_count,
        "nonempty_line_count": len(lines),
        "results": [
            {
                "name": r.name,
                "passed": r.passed,
                "message": r.message,
            }
            for r in results
        ],
    }