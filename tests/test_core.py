import csv
import tempfile
from pathlib import Path

import pytest

from src.core.data_loader import load_csv
from src.core.pipeline import run_pipeline


@pytest.fixture
def temp_csv_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.csv"
        data = [
            {"name": "A", "price": "100"},
            {"name": "B", "price": "200"}
        ]
        with open(file_path, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        yield str(file_path)


def test_load_csv(temp_csv_file):
    data = load_csv(temp_csv_file)
    assert len(data) > 0
    assert "name" in data[0]


def test_pipeline(temp_csv_file):
    data = load_csv(temp_csv_file)
    processed = run_pipeline(data, {"where": "price>100"})
    assert len(processed) < len(data)
