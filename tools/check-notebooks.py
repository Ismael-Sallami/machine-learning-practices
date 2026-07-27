#!/usr/bin/env python3
"""Check that every notebook is valid and that its code parses.

The notebooks were run on Colab against datasets that are not in the repository,
so they cannot be executed here. What can be checked without the data is that the
file is a well formed notebook and that every code cell is syntactically valid
Python, which is what catches a truncated or half-saved notebook.

    python3 tools/check-notebooks.py

@author Ismael Sallami Moreno
"""

import ast
import json
import pathlib
import sys

SOURCE = pathlib.Path("src")

# Cell magics and shell escapes are valid in a notebook and not in Python.
def strip_magics(code: str) -> str:
    kept = []
    for line in code.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("%", "!", "?")):
            continue
        kept.append(line)
    return "\n".join(kept)


def check(path: pathlib.Path) -> bool:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"FAIL  {path}: not valid JSON, {error}")
        return False

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        print(f"FAIL  {path}: no cells")
        return False

    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    bad = 0
    for number, cell in enumerate(code_cells, start=1):
        code = strip_magics("".join(cell.get("source", [])))
        if not code.strip():
            continue
        try:
            ast.parse(code)
        except SyntaxError as error:
            print(f"FAIL  {path}: code cell {number} does not parse, line {error.lineno}: {error.msg}")
            bad += 1

    if bad:
        return False
    print(f"ok    {path}: {len(cells)} cells, {len(code_cells)} of them code")
    return True


def main() -> int:
    notebooks = sorted(SOURCE.glob("*.ipynb"))
    if not notebooks:
        print("no notebooks found")
        return 1
    if all(check(path) for path in notebooks):
        print(f"\n{len(notebooks)} notebooks are valid and their code parses")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
