import pytest
import pandas as pd
from custom_parsers.icici_parser import parse
from pathlib import Path

TEST_DATA_DIR = Path("data/icici")

def test_parse_returns_dataframe():
    csv_path = TEST_DATA_DIR / "sample_icici.csv"
    df = parse(str(csv_path))
    assert isinstance(df, pd.DataFrame)

def test_dataframe_not_empty():
    csv_path = TEST_DATA_DIR / "sample_icici.csv"
    df = parse(str(csv_path))
    assert not df.empty

def test_dataframe_has_expected_columns():
    csv_path = TEST_DATA_DIR / "sample_icici.csv"
    df = parse(str(csv_path))
    expected_columns = ["Date", "Description", "Debit", "Credit", "Balance"]  # replace with actual columns in your CSV
    assert list(df.columns) == expected_columns
