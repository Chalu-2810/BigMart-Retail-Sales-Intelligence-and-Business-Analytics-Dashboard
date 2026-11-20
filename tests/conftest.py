"""Shared pytest fixtures for the test suite."""
import os
import sys

import pandas as pd
import pytest

# Make `src` importable when running `pytest` from the project root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import data_cleaning as dc  # noqa: E402

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, "data", "raw_dataset.csv")


@pytest.fixture(scope="session")
def raw_df():
    """The untouched raw dataset, loaded once per test session."""
    return pd.read_csv(RAW_PATH)


@pytest.fixture
def cleaned_df(raw_df):
    """A fully cleaned dataset, rebuilt fresh for each test (cheap: <6k rows)."""
    df = raw_df.copy()
    df = dc.remove_duplicates(df)
    df = dc.clean_fat_content(df)
    df = dc.fill_item_weight(df)
    df = dc.fill_outlet_size(df)
    df = dc.fix_zero_visibility(df)
    df = dc.add_derived_columns(df)
    return df
