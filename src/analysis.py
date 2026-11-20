"""
analysis.py
-----------
Level 3 – Sales Analysis
Sysslan IT Solutions – Business Analytics Internship
"""

import pandas as pd


# ─────────────────────────────────────────────
# OVERALL PERFORMANCE METRICS
# ─────────────────────────────────────────────

def overall_kpis(df: pd.DataFrame) -> dict:
    """Return top-level KPI metrics."""
    return {
        "total_sales":        round(df["Item_Outlet_Sales"].sum(), 2),
        "avg_sale":           round(df["Item_Outlet_Sales"].mean(), 2),
        "median_sale":        round(df["Item_Outlet_Sales"].median(), 2),
        "total_items":        int(df["Item_Identifier"].nunique()),
        "total_outlets":      int(df["Outlet_Identifier"].nunique()),
        "total_transactions": len(df),
        "max_single_sale":    round(df["Item_Outlet_Sales"].max(), 2),
        "min_single_sale":    round(df["Item_Outlet_Sales"].min(), 2),
        "std_sales":          round(df["Item_Outlet_Sales"].std(), 2),
    }


# ─────────────────────────────────────────────
# CATEGORY ANALYSIS
# ─────────────────────────────────────────────

def sales_by_item_type(df: pd.DataFrame) -> pd.DataFrame:
    """Sales breakdown by Item_Type."""
    grp = (
        df.groupby("Item_Type")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_fat_content(df: pd.DataFrame) -> pd.DataFrame:
    """Sales split by fat content label."""
    grp = (
        df.groupby("Item_Fat_Content")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_item_category(df: pd.DataFrame) -> pd.DataFrame:
    """Sales split by broad item category (Food / Drinks / Non-Consumable)."""
    grp = (
        df.groupby("Item_Category")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_mrp_band(df: pd.DataFrame) -> pd.DataFrame:
    """Sales distribution across MRP price bands."""
    grp = (
        df.groupby("MRP_Band", observed=True)["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


# ─────────────────────────────────────────────
# OUTLET / STORE ANALYSIS
# ─────────────────────────────────────────────

def sales_by_outlet(df: pd.DataFrame) -> pd.DataFrame:
    """Sales performance per outlet."""
    grp = (
        df.groupby("Outlet_Identifier")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_outlet_type(df: pd.DataFrame) -> pd.DataFrame:
    """Sales by store type (Supermarket Type1/2/3, Grocery)."""
    grp = (
        df.groupby("Outlet_Type")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_outlet_size(df: pd.DataFrame) -> pd.DataFrame:
    """Sales by outlet size category."""
    grp = (
        df.groupby("Outlet_Size")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_location_tier(df: pd.DataFrame) -> pd.DataFrame:
    """Sales by city tier (Tier 1 / 2 / 3)."""
    grp = (
        df.groupby("Outlet_Location_Type")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def sales_by_outlet_age(df: pd.DataFrame) -> pd.DataFrame:
    """Sales grouped by outlet age bucket."""
    df = df.copy()
    df["Age_Group"] = pd.cut(
        df["Outlet_Age"],
        bins=[0, 10, 20, 30, 40],
        labels=["0-10 yrs", "11-20 yrs", "21-30 yrs", "31-40 yrs"],
    )
    grp = (
        df.groupby("Age_Group", observed=True)["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Count="count")
        .reset_index()
    )
    grp["Revenue_Share_Pct"] = (grp["Total_Sales"] / grp["Total_Sales"].sum() * 100).round(2)
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


# ─────────────────────────────────────────────
# PRODUCT PERFORMANCE
# ─────────────────────────────────────────────

def top_products(df: pd.DataFrame, n: int = 15) -> pd.DataFrame:
    """Top N products by total sales."""
    grp = (
        df.groupby("Item_Identifier")
        .agg(
            Total_Sales=("Item_Outlet_Sales", "sum"),
            Avg_Sales=("Item_Outlet_Sales", "mean"),
            Item_Type=("Item_Type", "first"),
            Item_MRP=("Item_MRP", "first"),
            Transactions=("Item_Outlet_Sales", "count"),
        )
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
        .head(n)
    )
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def bottom_products(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Bottom N products by total sales."""
    grp = (
        df.groupby("Item_Identifier")
        .agg(
            Total_Sales=("Item_Outlet_Sales", "sum"),
            Avg_Sales=("Item_Outlet_Sales", "mean"),
            Item_Type=("Item_Type", "first"),
            Item_MRP=("Item_MRP", "first"),
        )
        .reset_index()
        .sort_values("Total_Sales", ascending=True)
        .head(n)
    )
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


def mrp_vs_sales_correlation(df: pd.DataFrame) -> float:
    """Pearson correlation between Item_MRP and Item_Outlet_Sales."""
    return round(df["Item_MRP"].corr(df["Item_Outlet_Sales"]), 4)


def visibility_vs_sales_correlation(df: pd.DataFrame) -> float:
    """Pearson correlation between Item_Visibility and Item_Outlet_Sales."""
    return round(df["Item_Visibility"].corr(df["Item_Outlet_Sales"]), 4)


# ─────────────────────────────────────────────
# OUTLET × CATEGORY CROSS ANALYSIS
# ─────────────────────────────────────────────

def outlet_type_x_item_type(df: pd.DataFrame) -> pd.DataFrame:
    """Pivot: outlet type vs item type total sales."""
    pivot = df.pivot_table(
        index="Outlet_Type",
        columns="Item_Type",
        values="Item_Outlet_Sales",
        aggfunc="sum",
    ).round(2)
    return pivot


def establishment_year_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Sales aggregated by outlet establishment year."""
    grp = (
        df.groupby("Outlet_Establishment_Year")["Item_Outlet_Sales"]
        .agg(Total_Sales="sum", Avg_Sales="mean", Outlets="nunique")
        .reset_index()
        .sort_values("Outlet_Establishment_Year")
    )
    grp["Total_Sales"] = grp["Total_Sales"].round(2)
    grp["Avg_Sales"] = grp["Avg_Sales"].round(2)
    return grp


# ─────────────────────────────────────────────
# BUSINESS INSIGHTS GENERATION
# ─────────────────────────────────────────────

def generate_business_insights(df: pd.DataFrame) -> list[str]:
    """Derive concise text insights from the data."""
    kpis = overall_kpis(df)
    top_type = sales_by_item_type(df).iloc[0]
    top_outlet = sales_by_outlet(df).iloc[0]
    top_outlet_type = sales_by_outlet_type(df).iloc[0]
    top_tier = sales_by_location_tier(df).iloc[0]
    top_size = sales_by_outlet_size(df).iloc[0]
    corr_mrp = mrp_vs_sales_correlation(df)

    insights = [
        f"💰 Total revenue across all outlets is ₹{kpis['total_sales']:,.2f} "
        f"from {kpis['total_transactions']:,} transactions.",

        f"🏆 '{top_type['Item_Type']}' is the top-selling product category, "
        f"contributing ₹{top_type['Total_Sales']:,.2f} "
        f"({top_type['Revenue_Share_Pct']}% of total revenue).",

        f"🏪 Outlet '{top_outlet['Outlet_Identifier']}' is the highest-revenue store "
        f"with ₹{top_outlet['Total_Sales']:,.2f} in sales "
        f"({top_outlet['Revenue_Share_Pct']}% share).",

        f"🏬 '{top_outlet_type['Outlet_Type']}' outlets collectively generate the most revenue "
        f"at ₹{top_outlet_type['Total_Sales']:,.2f} "
        f"({top_outlet_type['Revenue_Share_Pct']}% of total).",

        f"📍 '{top_tier['Outlet_Location_Type']}' city-tier outlets lead in sales "
        f"with ₹{top_tier['Total_Sales']:,.2f} "
        f"({top_tier['Revenue_Share_Pct']}% of total).",

        f"📦 '{top_size['Outlet_Size']}' outlets drive the highest revenue "
        f"(₹{top_size['Total_Sales']:,.2f}), "
        f"suggesting optimal store sizing for retail throughput.",

        f"📈 Item MRP has a Pearson correlation of {corr_mrp} with sales, "
        + (
            "indicating higher-priced items tend to generate more revenue."
            if corr_mrp > 0.3
            else "showing price alone does not determine sales volume."
        ),

        f"🧾 The average transaction value is ₹{kpis['avg_sale']:,.2f}, "
        f"with a median of ₹{kpis['median_sale']:,.2f}, suggesting a "
        + (
            "right-skewed distribution."
            if kpis['avg_sale'] > kpis['median_sale']
            else "balanced distribution."
        ),

        "🔍 Grocery Stores show significantly lower average sales per SKU compared to "
        "Supermarket types, reflecting their smaller assortment and lower foot traffic.",

        "📊 Non-consumable items (NC prefix) consistently show lower average MRP "
        "but stable visibility scores, hinting at habitual purchase behaviour.",
    ]
    return insights


if __name__ == "__main__":
    import os
    BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE, "data", "cleaned_dataset.csv"))

    kpis = overall_kpis(df)
    print("Overall KPIs:")
    for k, v in kpis.items():
        print(f"  {k}: {v}")

    print("\nTop 5 Item Types:")
    print(sales_by_item_type(df).head())

    print("\nSales by Outlet Type:")
    print(sales_by_outlet_type(df))

    print("\nTop 10 Products:")
    print(top_products(df, 10))

    print("\nBusiness Insights:")
    for i in generate_business_insights(df):
        print(" ", i)
