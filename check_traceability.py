"""Fail if the traceability matrix references a file or test that does not exist.

Usage: python check_traceability.py /path/to/retail-demand-forecast-api
"""
import re
import subprocess
import sys
from pathlib import Path

MATRIX = Path(__file__).parent / "docs" / "04-traceability-matrix.md"


def collect_tests(repo: Path) -> set[str]:
    found = set()
    for test_file in (repo / "tests").glob("test_*.py"):
        for name in re.findall(r"^def (test_\w+)\(", test_file.read_text(), flags=re.M):
            found.add(f"tests/{test_file.name}::{name}")
    return found


def main(repo_arg: str) -> int:
    repo = Path(repo_arg)
    table_rows = [ln for ln in MATRIX.read_text().splitlines() if ln.startswith("| ")]
    refs = re.findall(r"`([^`]+)`", "\n".join(table_rows))

    existing_tests = collect_tests(repo)
    problems = []
    checked_tests = checked_files = 0

    for ref in refs:
        ref = ref.split(" ")[0]
        if "::" in ref:
            checked_tests += 1
            if ref not in existing_tests:
                problems.append(f"test not found: {ref}")
        elif "/" in ref or ref.endswith((".py", ".yml", ".json")) or ref == "Dockerfile":
            if ref.startswith("tests/") and ref.endswith(".py"):
                continue
            checked_files += 1
            if not (repo / ref).exists():
                problems.append(f"file not found: {ref}")

    referenced = {r.split(" ")[0] for r in refs if "::" in r}
    unreferenced = sorted(existing_tests - referenced)

    print(f"checked {checked_tests} test references and {checked_files} file references")
    for p in problems:
        print("PROBLEM:", p)
    for t in unreferenced:
        print("NOTE: test not referenced by any requirement:", t)

    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
