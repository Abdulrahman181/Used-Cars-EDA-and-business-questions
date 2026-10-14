"""Fast repository checks that do not require the optional source dataset."""

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "vehicles-EDA.ipynb"


def _notebook() -> dict:
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))


def test_notebook_is_valid_and_code_compiles() -> None:
    notebook = _notebook()
    assert notebook["nbformat"] >= 4
    assert notebook["cells"]
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            ast.parse("".join(cell["source"]))


def test_notebook_has_no_stale_outputs_or_execution_counts() -> None:
    for cell in _notebook()["cells"]:
        if cell["cell_type"] == "code":
            assert cell["execution_count"] is None
            assert cell["outputs"] == []


def test_data_loading_is_portable_and_data_gated() -> None:
    source = "\n".join(
        "".join(cell.get("source", []))
        for cell in _notebook()["cells"]
        if cell["cell_type"] == "code"
    )
    assert "/kaggle/" not in source
    assert "USED_CARS_DATA" in source
    assert "FileNotFoundError" in source
    assert "synthetic" not in source.lower()


def test_required_runtime_dependencies_are_declared() -> None:
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    for package in ("pandas", "numpy", "matplotlib", "seaborn", "jupyter"):
        assert package in requirements
