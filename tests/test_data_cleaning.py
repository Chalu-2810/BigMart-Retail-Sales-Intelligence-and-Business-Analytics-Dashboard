"""Unit tests for src/data_cleaning.py (Level 1 & 2 pipeline)."""
import numpy as np
import pandas as pd

from src import data_cleaning as dc


class TestCleanFatContent:
    def test_collapses_all_known_variants_to_two_labels(self, raw_df):
        df = dc.clean_fat_content(raw_df.copy())
        assert set(df["Item_Fat_Content"].unique()) == {"Low Fat", "Regular"}

    def test_is_case_and_whitespace_insensitive(self):
        df = pd.DataFrame({"Item_Fat_Content": [" LF ", "REG", "Low Fat", "regular"]})
        out = dc.clean_fat_content(df)
        assert out["Item_Fat_Content"].tolist() == [
            "Low Fat", "Regular", "Low Fat", "Regular",
        ]

    def test_unknown_variant_becomes_nan_not_silently_dropped(self):
        df = pd.DataFrame({"Item_Fat_Content": ["LF", "totally_unknown"]})
        out = dc.clean_fat_content(df)
        assert out["Item_Fat_Content"].isna().sum() == 1


class TestFillItemWeight:
    def test_no_nulls_remain(self, raw_df):
        out = dc.fill_item_weight(raw_df.copy())
        assert out["Item_Weight"].isnull().sum() == 0

    def test_existing_values_are_not_overwritten(self, raw_df):
        before = raw_df["Item_Weight"].dropna()
        out = dc.fill_item_weight(raw_df.copy())
        pd.testing.assert_series_equal(
            out.loc[before.index, "Item_Weight"], before, check_exact=True
        )


class TestFillOutletSize:
    def test_no_nulls_remain(self, raw_df):
        out = dc.fill_outlet_size(raw_df.copy())
        assert out["Outlet_Size"].isnull().sum() == 0

    def test_only_valid_categories_used(self, raw_df):
        out = dc.fill_outlet_size(raw_df.copy())
        assert set(out["Outlet_Size"].unique()) <= {"Small", "Medium", "High"}


class TestFixZeroVisibility:
    def test_no_zero_visibility_remains(self, raw_df):
        out = dc.fix_zero_visibility(raw_df.copy())
        assert (out["Item_Visibility"] == 0).sum() == 0

    def test_visibility_stays_within_valid_range(self, raw_df):
        out = dc.fix_zero_visibility(raw_df.copy())
        assert out["Item_Visibility"].between(0, 1).all()


class TestAddDerivedColumns:
    def test_creates_expected_columns(self, cleaned_df):
        for col in ["Outlet_Age", "Item_Category", "Item_Outlet_Sales", "MRP_Band"]:
            assert col in cleaned_df.columns

    def test_item_category_matches_identifier_prefix(self, cleaned_df):
        prefix_map = {"FD": "Food", "DR": "Drinks", "NC": "Non-Consumable"}
        sample = cleaned_df.sample(min(200, len(cleaned_df)), random_state=0)
        for _, row in sample.iterrows():
            expected = prefix_map.get(row["Item_Identifier"][:2], "Other")
            assert row["Item_Category"] == expected

    def test_outlet_age_is_non_negative(self, cleaned_df):
        assert (cleaned_df["Outlet_Age"] >= 0).all()

    def test_synthetic_sales_target_is_reproducible(self, raw_df):
        """The disclosed synthetic Item_Outlet_Sales formula must be
        deterministic (fixed seed) so results never silently drift."""
        df1 = dc.add_derived_columns(
            dc.fix_zero_visibility(dc.fill_item_weight(raw_df.copy()))
        )
        df2 = dc.add_derived_columns(
            dc.fix_zero_visibility(dc.fill_item_weight(raw_df.copy()))
        )
        np.testing.assert_allclose(
            df1["Item_Outlet_Sales"].values, df2["Item_Outlet_Sales"].values
        )

    def test_synthetic_sales_are_non_negative(self, cleaned_df):
        assert (cleaned_df["Item_Outlet_Sales"] >= 0).all()


class TestIdentifyInconsistencies:
    def test_reports_expected_counts(self, raw_df):
        inc = dc.identify_inconsistencies(raw_df)
        assert inc["outlet_size_missing"] == raw_df["Outlet_Size"].isna().sum()
        assert inc["zero_visibility_rows"] == int((raw_df["Item_Visibility"] == 0).sum())


class TestRemoveDuplicates:
    def test_drops_exact_duplicate_rows(self):
        df = pd.DataFrame({"a": [1, 1, 2], "b": [1, 1, 2]})
        out = dc.remove_duplicates(df)
        assert len(out) == 2


class TestCleanedDatasetIntegrity:
    """End-to-end sanity checks on the full pipeline output."""

    def test_no_nulls_in_key_columns(self, cleaned_df):
        key_cols = ["Item_Weight", "Outlet_Size", "Item_Visibility", "Item_Outlet_Sales"]
        assert cleaned_df[key_cols].isnull().sum().sum() == 0

    def test_row_count_preserved(self, raw_df, cleaned_df):
        assert len(cleaned_df) == len(raw_df.drop_duplicates())
