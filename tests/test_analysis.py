"""Unit tests for src/analysis.py (Level 3 sales analysis)."""
import math

from src import analysis as ana


class TestOverallKpis:
    def test_total_sales_matches_sum(self, cleaned_df):
        kpis = ana.overall_kpis(cleaned_df)
        assert math.isclose(
            kpis["total_sales"], cleaned_df["Item_Outlet_Sales"].sum(), rel_tol=1e-6
        )

    def test_total_transactions_matches_row_count(self, cleaned_df):
        kpis = ana.overall_kpis(cleaned_df)
        assert kpis["total_transactions"] == len(cleaned_df)

    def test_unique_counts_are_consistent(self, cleaned_df):
        kpis = ana.overall_kpis(cleaned_df)
        assert kpis["total_items"] == cleaned_df["Item_Identifier"].nunique()
        assert kpis["total_outlets"] == cleaned_df["Outlet_Identifier"].nunique()


class TestGroupedSalesTables:
    def test_revenue_share_sums_to_100(self, cleaned_df):
        grp = ana.sales_by_item_type(cleaned_df)
        assert math.isclose(grp["Revenue_Share_Pct"].sum(), 100.0, abs_tol=0.1)

    def test_sorted_descending_by_total_sales(self, cleaned_df):
        grp = ana.sales_by_item_type(cleaned_df)
        assert grp["Total_Sales"].is_monotonic_decreasing

    def test_outlet_type_grouping_covers_all_outlet_types(self, cleaned_df):
        grp = ana.sales_by_outlet_type(cleaned_df)
        assert set(grp["Outlet_Type"]) == set(cleaned_df["Outlet_Type"].unique())


class TestTopAndBottomProducts:
    def test_top_products_respects_n(self, cleaned_df):
        top5 = ana.top_products(cleaned_df, n=5)
        assert len(top5) == 5

    def test_top_products_are_actually_the_highest(self, cleaned_df):
        top = ana.top_products(cleaned_df, n=3)
        full = ana.top_products(cleaned_df, n=len(cleaned_df["Item_Identifier"].unique()))
        assert list(top["Item_Identifier"]) == list(full["Item_Identifier"].head(3))

    def test_bottom_products_are_actually_the_lowest(self, cleaned_df):
        bottom = ana.bottom_products(cleaned_df, n=3)
        assert (bottom["Total_Sales"] <= cleaned_df["Item_Outlet_Sales"].max()).all()


class TestCorrelations:
    def test_mrp_sales_correlation_within_valid_range(self, cleaned_df):
        corr = ana.mrp_vs_sales_correlation(cleaned_df)
        assert -1.0 <= corr <= 1.0

    def test_visibility_sales_correlation_within_valid_range(self, cleaned_df):
        corr = ana.visibility_vs_sales_correlation(cleaned_df)
        assert -1.0 <= corr <= 1.0


class TestBusinessInsights:
    def test_generates_a_non_empty_list_of_strings(self, cleaned_df):
        insights = ana.generate_business_insights(cleaned_df)
        assert isinstance(insights, list)
        assert len(insights) > 0
        assert all(isinstance(i, str) and len(i) > 0 for i in insights)
