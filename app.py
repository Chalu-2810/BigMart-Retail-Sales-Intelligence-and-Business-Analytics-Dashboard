"""
app.py
------
Level 5 – Full Interactive Streamlit Dashboard
Business Analytics Internship – Retail Sales Dashboard
Sysslan IT Solutions
Run: streamlit run app.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd

from src.dashboard_utils import (
    set_page_config, inject_custom_css, load_clean_data,
    sidebar_filters, render_kpi_card, render_insight,
    section_header, page_header, download_button,
)
from src import analysis as ana
from src import visualization as viz

# ── Bootstrap ──────────────────────────────────────────────────────────────────
set_page_config()
inject_custom_css()

# ── Load & filter data ────────────────────────────────────────────────────────
df_full = load_clean_data()
df      = sidebar_filters(df_full)

if df.empty:
    st.warning("⚠️ No data matches the current filters. Please adjust the sidebar.")
    st.stop()

# ── Navigation ─────────────────────────────────────────────────────────────────
PAGES = [
    "🏠 Executive Summary",
    "📊 Sales Analytics",
    "🏪 Outlet Performance",
    "📦 Product Performance",
    "💡 Business Insights",
    "🔬 Data Quality Report",
]
page = st.sidebar.radio("📌 Navigation", PAGES)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 – EXECUTIVE SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Executive Summary":
    page_header(
        "🛒 BigMart Retail Sales Dashboard",
        "Sysslan IT Solutions · Business Analytics Internship · Retail Sales Dashboard",
    )

    kpis = ana.overall_kpis(df)

    # KPI row 1
    c1, c2, c3, c4 = st.columns(4)
    with c1: render_kpi_card("Total Revenue",        kpis["total_sales"])
    with c2: render_kpi_card("Avg Transaction",       kpis["avg_sale"])
    with c3: render_kpi_card("Total Transactions",    kpis["total_transactions"], prefix="")
    with c4: render_kpi_card("Unique Products",       kpis["total_items"],        prefix="")

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI row 2
    c5, c6, c7, c8 = st.columns(4)
    with c5: render_kpi_card("Total Outlets",         kpis["total_outlets"],      prefix="")
    with c6: render_kpi_card("Median Sale Value",     kpis["median_sale"])
    with c7: render_kpi_card("Highest Single Sale",   kpis["max_single_sale"])
    with c8: render_kpi_card("Sales Std Deviation",   kpis["std_sales"])

    st.markdown("---")

    # Top charts side by side
    col_l, col_r = st.columns(2)
    with col_l:
        section_header("Sales by Product Category")
        st.plotly_chart(
            viz.bar_sales_by_item_type(ana.sales_by_item_type(df)),
            width="stretch",
        )
    with col_r:
        section_header("Revenue Share by Category")
        st.plotly_chart(
            viz.pie_category_share(ana.sales_by_item_type(df)),
            width="stretch",
        )

    col_l2, col_r2 = st.columns(2)
    with col_l2:
        section_header("Sales by Outlet Type")
        st.plotly_chart(
            viz.bar_outlet_type(ana.sales_by_outlet_type(df)),
            width="stretch",
        )
    with col_r2:
        section_header("Sales by City Tier")
        st.plotly_chart(
            viz.bar_location_tier(ana.sales_by_location_tier(df)),
            width="stretch",
        )

    st.markdown("---")
    section_header("Quick Business Summary")
    insights = ana.generate_business_insights(df)
    for ins in insights[:5]:
        render_insight(ins)

    download_button(df)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 – SALES ANALYTICS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Sales Analytics":
    page_header("📊 Sales Analytics", "Deep-dive into sales patterns and distributions")

    kpis = ana.overall_kpis(df)
    c1, c2, c3 = st.columns(3)
    with c1: render_kpi_card("Total Revenue",     kpis["total_sales"])
    with c2: render_kpi_card("Avg Sale",          kpis["avg_sale"])
    with c3: render_kpi_card("Total Transactions", kpis["total_transactions"], prefix="")
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📦 By Category", "💲 By Price Band", "🥗 By Fat Content", "📅 By Year"]
    )

    with tab1:
        col_l, col_r = st.columns(2)
        with col_l:
            st.plotly_chart(viz.bar_sales_by_item_type(ana.sales_by_item_type(df)),
                            width="stretch")
        with col_r:
            st.plotly_chart(viz.treemap_item_type(ana.sales_by_item_type(df)),
                            width="stretch")
        st.plotly_chart(viz.box_sales_by_item_type(df), width="stretch")
        st.plotly_chart(viz.funnel_category(ana.sales_by_item_type(df)),
                        width="stretch")
        st.plotly_chart(viz.bar_item_category_type(df), width="stretch")

    with tab2:
        st.plotly_chart(viz.bar_mrp_band(ana.sales_by_mrp_band(df)),
                        width="stretch")
        st.plotly_chart(viz.histogram_sales(df), width="stretch")
        st.plotly_chart(viz.scatter_mrp_vs_sales(df), width="stretch")
        corr = ana.mrp_vs_sales_correlation(df)
        st.metric("MRP ↔ Sales Pearson Correlation", corr)

    with tab3:
        col_l, col_r = st.columns(2)
        with col_l:
            st.plotly_chart(viz.bar_fat_content(ana.sales_by_fat_content(df)),
                            width="stretch")
        with col_r:
            st.plotly_chart(
                viz.pie_category_share(
                    ana.sales_by_fat_content(df),
                    label_col="Item_Fat_Content",
                ),
                width="stretch",
            )
        st.dataframe(ana.sales_by_fat_content(df), width="stretch")

    with tab4:
        st.plotly_chart(viz.line_establishment_year(ana.establishment_year_sales(df)),
                        width="stretch")
        st.plotly_chart(viz.bar_outlet_age(ana.sales_by_outlet_age(df)),
                        width="stretch")
        st.dataframe(ana.establishment_year_sales(df), width="stretch")

    st.markdown("---")
    section_header("Detailed Category Table")
    st.dataframe(ana.sales_by_item_type(df).style.background_gradient(
        subset=["Total_Sales"], cmap="YlOrRd"), width="stretch")

    download_button(df)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 – OUTLET PERFORMANCE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🏪 Outlet Performance":
    page_header("🏪 Outlet Performance", "Compare stores by type, size, location and age")

    kpis = ana.overall_kpis(df)
    c1, c2, c3 = st.columns(3)
    with c1: render_kpi_card("Total Outlets",    kpis["total_outlets"],      prefix="")
    with c2: render_kpi_card("Total Revenue",    kpis["total_sales"])
    with c3: render_kpi_card("Avg Sale / Item",  kpis["avg_sale"])
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["🏪 By Outlet", "🏬 By Type", "📐 By Size", "📍 By Tier"]
    )

    with tab1:
        st.plotly_chart(viz.bar_sales_by_outlet(ana.sales_by_outlet(df)),
                        width="stretch")
        st.plotly_chart(viz.violin_outlet_type(df), width="stretch")
        st.dataframe(ana.sales_by_outlet(df).style.background_gradient(
            subset=["Total_Sales"], cmap="Blues"), width="stretch")

    with tab2:
        col_l, col_r = st.columns(2)
        with col_l:
            st.plotly_chart(viz.bar_outlet_type(ana.sales_by_outlet_type(df)),
                            width="stretch")
        with col_r:
            st.plotly_chart(
                viz.pie_category_share(
                    ana.sales_by_outlet_type(df),
                    label_col="Outlet_Type",
                ),
                width="stretch",
            )
        # Heatmap outlet × category
        pivot = ana.outlet_type_x_item_type(df)
        st.plotly_chart(viz.heatmap_outlet_x_category(pivot), width="stretch")
        st.dataframe(ana.sales_by_outlet_type(df), width="stretch")

    with tab3:
        col_l, col_r = st.columns(2)
        with col_l:
            st.plotly_chart(viz.bar_outlet_size(ana.sales_by_outlet_size(df)),
                            width="stretch")
        with col_r:
            st.plotly_chart(
                viz.pie_category_share(
                    ana.sales_by_outlet_size(df),
                    label_col="Outlet_Size",
                ),
                width="stretch",
            )
        st.dataframe(ana.sales_by_outlet_size(df), width="stretch")

    with tab4:
        col_l, col_r = st.columns(2)
        with col_l:
            st.plotly_chart(viz.bar_location_tier(ana.sales_by_location_tier(df)),
                            width="stretch")
        with col_r:
            st.plotly_chart(
                viz.pie_category_share(
                    ana.sales_by_location_tier(df),
                    label_col="Outlet_Location_Type",
                ),
                width="stretch",
            )
        st.dataframe(ana.sales_by_location_tier(df), width="stretch")

    download_button(df)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 – PRODUCT PERFORMANCE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📦 Product Performance":
    page_header("📦 Product Performance", "Top & bottom SKUs, pricing impact, visibility")

    kpis = ana.overall_kpis(df)
    c1, c2, c3 = st.columns(3)
    with c1: render_kpi_card("Unique Products",  kpis["total_items"],  prefix="")
    with c2: render_kpi_card("Total Revenue",    kpis["total_sales"])
    with c3: render_kpi_card("Avg Sale / SKU",   kpis["avg_sale"])
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🏆 Top Products", "📉 Bottom Products", "📈 Price & Visibility"])

    with tab1:
        n = st.slider("Show top N products", 5, 30, 15)
        top = ana.top_products(df, n)
        st.plotly_chart(viz.bar_top_products(top), width="stretch")
        st.dataframe(top.style.background_gradient(subset=["Total_Sales"], cmap="YlOrRd"),
                     width="stretch")

    with tab2:
        bottom = ana.bottom_products(df, 10)
        st.dataframe(bottom, width="stretch")
        render_insight("💡 Bottom-performing SKUs may benefit from promotional pricing, "
                       "bundling, or shelf relocation strategies.")

    with tab3:
        st.plotly_chart(viz.scatter_mrp_vs_sales(df), width="stretch")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("MRP ↔ Sales Correlation",
                      ana.mrp_vs_sales_correlation(df))
        with c2:
            st.metric("Visibility ↔ Sales Correlation",
                      ana.visibility_vs_sales_correlation(df))

        st.plotly_chart(viz.bar_mrp_band(ana.sales_by_mrp_band(df)),
                        width="stretch")
        st.plotly_chart(viz.histogram_sales(df), width="stretch")

    st.markdown("---")
    section_header("Product-Level Data Explorer")
    item_types = ["All"] + sorted(df["Item_Type"].unique())
    sel_type   = st.selectbox("Filter by Item Type", item_types)
    show_df    = df if sel_type == "All" else df[df["Item_Type"] == sel_type]
    cols_show  = ["Item_Identifier", "Item_Type", "Item_Fat_Content",
                  "Item_MRP", "Item_Visibility", "Outlet_Type", "Item_Outlet_Sales"]
    st.dataframe(show_df[cols_show].sort_values("Item_Outlet_Sales", ascending=False)
                 .reset_index(drop=True), width="stretch")

    download_button(df)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 – BUSINESS INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "💡 Business Insights":
    page_header("💡 Business Insights", "Actionable findings from the data analysis")

    insights = ana.generate_business_insights(df)
    section_header("📌 Key Findings")
    for ins in insights:
        render_insight(ins)

    st.markdown("---")
    section_header("📋 Strategic Recommendations")
    recommendations = [
        ("🏪 Expand Supermarket Type1 Outlets",
         "Supermarket Type1 stores drive the highest volume. Prioritise expansion "
         "in Tier 2 and Tier 3 cities where market penetration is still low."),

        ("📦 Double Down on Snack Foods & Fruits",
         "Top two categories by revenue. Increasing shelf space, improving supply "
         "chain, and running targeted promotions will yield the highest returns."),

        ("💰 Premium Product Strategy",
         "Higher MRP items correlate positively with sales. Introducing premium "
         "product lines in high-traffic supermarkets could lift basket size."),

        ("🏢 Optimise Medium-Sized Stores",
         "Medium outlets outperform both Small and High stores in revenue per SKU. "
         "The medium format appears optimal for the current customer base."),

        ("📍 Tier 3 City Growth Opportunity",
         "While Tier 1 leads in absolute revenue, Tier 3 cities are under-served. "
         "Pilot low-cost grocery format rollouts for first-mover advantage."),

        ("🔄 Revamp Low-Visibility SKUs",
         "Items with near-zero visibility generate disproportionately low sales. "
         "Planogram redesign and end-cap placements can recover lost revenue."),

        ("🥗 Low-Fat Product Premium",
         "Low Fat items command slightly higher average MRP. Health-conscious "
         "labelling campaigns could shift consumer preference and margins."),

        ("📅 Modernise Older Outlets",
         "Stores established before 1990 show weaker average transaction values. "
         "Renovation and technology refresh (self-checkout, digital menus) can "
         "improve customer experience and throughput."),
    ]
    for title, body in recommendations:
        with st.expander(title):
            st.write(body)

    st.markdown("---")
    section_header("📊 Supporting Visualisations")
    col_l, col_r = st.columns(2)
    with col_l:
        st.plotly_chart(viz.bar_sales_by_item_type(ana.sales_by_item_type(df)),
                        width="stretch")
    with col_r:
        st.plotly_chart(viz.bar_outlet_type(ana.sales_by_outlet_type(df)),
                        width="stretch")
    st.plotly_chart(viz.scatter_mrp_vs_sales(df), width="stretch")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 – DATA QUALITY REPORT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔬 Data Quality Report":
    page_header("🔬 Data Quality Report", "Level 1 & 2 — Understanding and Preparation")

    # Re-load the raw (pre-cleaning) dataset for a before/after comparison
    BASE = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(BASE, "data", "raw_dataset.csv")
    try:
        raw_df = pd.read_csv(raw_path)
    except Exception:
        raw_df = df_full.copy()

    st.info(
        "**📌 Methodology note:** This project uses the public *BigMart Sales* "
        "dataset, which (in this split) ships without a real sales figure. To make "
        "the analytics layer demonstrable end-to-end, `Item_Outlet_Sales` is a "
        "**documented, seeded synthetic estimate** derived from `Item_MRP`, "
        "`Item_Visibility`, and bounded random noise (see "
        "`src/data_cleaning.add_derived_columns`). It is reproducible and useful for "
        "showcasing the analysis/visualization/dashboard pipeline, but it is **not "
        "real transactional revenue** — see the README's *Data & Methodology* "
        "section for details."
    )

    section_header("📋 Dataset Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1: render_kpi_card("Total Rows", len(df_full), prefix="")
    with c2: render_kpi_card("Total Columns", df_full.shape[1], prefix="")
    with c3: render_kpi_card("Unique Items", df_full["Item_Identifier"].nunique(), prefix="")
    with c4: render_kpi_card("Unique Outlets", df_full["Outlet_Identifier"].nunique(), prefix="")

    st.markdown("<br>", unsafe_allow_html=True)
    section_header("🗂️ Column Descriptions")
    col_desc = pd.DataFrame({
        "Column": [
            "Item_Identifier", "Item_Weight", "Item_Fat_Content", "Item_Visibility",
            "Item_Type", "Item_MRP", "Outlet_Identifier", "Outlet_Establishment_Year",
            "Outlet_Size", "Outlet_Location_Type", "Outlet_Type",
            "Outlet_Age", "Item_Category", "Item_Outlet_Sales", "MRP_Band",
        ],
        "Type": [
            "Categorical", "Numeric", "Categorical", "Numeric",
            "Categorical", "Numeric", "Categorical", "Numeric",
            "Categorical", "Categorical", "Categorical",
            "Numeric (derived)", "Categorical (derived)",
            "Numeric (derived)", "Categorical (derived)",
        ],
        "Description": [
            "Unique product code",
            "Weight of the product in kg",
            "Product fat label: Low Fat or Regular",
            "Fraction of total display area allocated (0–1)",
            "Product category (16 types)",
            "Maximum retail price of the product",
            "Unique store/outlet code",
            "Year the outlet was established",
            "Physical size of the outlet (Small / Medium / High)",
            "City tier where outlet is located (Tier 1/2/3)",
            "Type of store (Grocery Store, Supermarket Type 1/2/3)",
            "Age of outlet in years (2024 − establishment year)",
            "Broad item category derived from Item_Identifier prefix",
            "Estimated sales revenue per item-outlet combination",
            "Price band bucket for MRP-based segmentation",
        ],
    })
    st.dataframe(col_desc, width="stretch", hide_index=True)

    st.markdown("---")
    section_header("❓ Missing Values (Raw Dataset)")
    mv = raw_df.isnull().sum().reset_index()
    mv.columns = ["Column", "Missing Count"]
    mv["Missing %"] = (mv["Missing Count"] / len(raw_df) * 100).round(2)
    mv["Status"] = mv["Missing Count"].apply(
        lambda x: "✅ Complete" if x == 0 else "⚠️ Has Nulls"
    )
    st.dataframe(mv, width="stretch", hide_index=True)

    st.markdown("---")
    section_header("⚠️ Inconsistencies Found")
    from src.data_cleaning import identify_inconsistencies
    inc = identify_inconsistencies(raw_df)
    st.markdown(f"**Fat Content Variants (before cleaning):** `{inc['fat_content_variants']}`")
    st.markdown(f"**Outlet_Size missing rows:** `{inc['outlet_size_missing']}`")
    st.markdown(f"**Item_Visibility = 0 rows:** `{inc['zero_visibility_rows']}`")

    st.markdown("---")
    section_header("✅ Cleaning Actions Applied")
    actions = [
        ("Item_Fat_Content", "Standardised 5 variants → 'Low Fat' / 'Regular'"),
        ("Item_Weight", "Filled 976 nulls with per-item median; remainder with global median"),
        ("Outlet_Size", "Filled 1,606 nulls with mode per Outlet_Type"),
        ("Item_Visibility", "Replaced 0 values with per-category median"),
        ("Outlet_Age", "Derived column: 2024 − Outlet_Establishment_Year"),
        ("Item_Category", "Derived from Item_Identifier prefix (FD/DR/NC)"),
        ("Item_Outlet_Sales", "Estimated sales proxy: MRP × (1−visibility) × noise"),
        ("MRP_Band", "Created 5 price-tier buckets for segmentation"),
        ("Duplicates", "0 duplicate rows found and removed"),
    ]
    for col, action in actions:
        st.markdown(f"- **{col}**: {action}")

    st.markdown("---")
    section_header("📈 Descriptive Statistics (Cleaned Dataset)")
    st.dataframe(df_full.describe().T.style.background_gradient(cmap="Blues"),
                 width="stretch")

    st.markdown("---")
    section_header("🔍 Raw Data Sample")
    st.dataframe(raw_df.head(20), width="stretch")

    section_header("🧹 Cleaned Data Sample")
    st.dataframe(df_full.head(20), width="stretch")

    download_button(df_full, "Download Full Cleaned Dataset")
