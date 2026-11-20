"""
visualization.py
----------------
Level 4 – Data Visualization
Sysslan IT Solutions – Business Analytics Internship
All charts use Plotly and return fig objects ready for Streamlit.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Brand palette ──────────────────────────────────────────────────────────────
PRIMARY    = "#E87722"   # Sysslan orange
SECONDARY  = "#1A3C5E"   # Deep navy
ACCENT     = "#27AE60"   # Green
LIGHT_BG   = "#F8F9FA"
GRID_COLOR = "#E0E0E0"

CATEGORY_COLORS = px.colors.qualitative.Set2
SEQUENTIAL      = "YlOrRd"

LAYOUT_DEFAULTS = dict(
    paper_bgcolor="white",
    plot_bgcolor=LIGHT_BG,
    font=dict(family="Segoe UI, Arial", size=13, color="#2C3E50"),
    margin=dict(l=40, r=40, t=60, b=40),
    legend=dict(bgcolor="white", bordercolor=GRID_COLOR, borderwidth=1),
)


def _apply_defaults(fig: go.Figure, title: str) -> go.Figure:
    fig.update_layout(title=dict(text=title, font=dict(size=17, color=SECONDARY)),
                      **LAYOUT_DEFAULTS)
    fig.update_xaxes(showgrid=True, gridcolor=GRID_COLOR, linecolor=GRID_COLOR)
    fig.update_yaxes(showgrid=True, gridcolor=GRID_COLOR, linecolor=GRID_COLOR)
    return fig


# ─────────────────────────────────────────────
# KPI CARDS (gauge / indicator)
# ─────────────────────────────────────────────

def kpi_indicator(value, title: str, prefix: str = "₹", suffix: str = "") -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="number",
        value=value,
        number=dict(prefix=prefix, suffix=suffix,
                    font=dict(size=42, color=PRIMARY)),
        title=dict(text=title, font=dict(size=14, color=SECONDARY)),
    ))
    fig.update_layout(paper_bgcolor="white", margin=dict(l=10, r=10, t=30, b=10), height=150)
    return fig


# ─────────────────────────────────────────────
# CATEGORY CHARTS
# ─────────────────────────────────────────────

def bar_sales_by_item_type(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Total_Sales", y="Item_Type",
        orientation="h", text="Revenue_Share_Pct",
        color="Total_Sales", color_continuous_scale=SEQUENTIAL,
        labels={"Total_Sales": "Total Sales (₹)", "Item_Type": "Product Category"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(coloraxis_showscale=False, yaxis=dict(autorange="reversed"))
    return _apply_defaults(fig, "💰 Total Sales by Product Category")


def pie_category_share(df_grp: pd.DataFrame,
                       label_col: str = "Item_Type",
                       value_col: str = "Total_Sales") -> go.Figure:
    fig = px.pie(
        df_grp, names=label_col, values=value_col,
        color_discrete_sequence=CATEGORY_COLORS,
        hole=0.38,
    )
    fig.update_traces(textinfo="percent+label", pull=[0.03]*len(df_grp))
    return _apply_defaults(fig, "🍕 Revenue Share by Category")


def treemap_item_type(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.treemap(
        df_grp, path=["Item_Type"], values="Total_Sales",
        color="Total_Sales", color_continuous_scale=SEQUENTIAL,
        labels={"Total_Sales": "Total Sales (₹)"},
    )
    fig.update_traces(textinfo="label+percent root")
    return _apply_defaults(fig, "🌳 Treemap – Revenue by Product Category")


def bar_fat_content(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Item_Fat_Content", y="Total_Sales",
        color="Item_Fat_Content",
        color_discrete_sequence=[PRIMARY, SECONDARY],
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "Item_Fat_Content": "Fat Content"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    return _apply_defaults(fig, "🥗 Sales by Fat Content")


def bar_mrp_band(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="MRP_Band", y="Total_Sales",
        color="MRP_Band",
        color_discrete_sequence=px.colors.sequential.Oranges[2:],
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "MRP_Band": "MRP Price Band"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    return _apply_defaults(fig, "💲 Sales Distribution by MRP Band")


# ─────────────────────────────────────────────
# OUTLET CHARTS
# ─────────────────────────────────────────────

def bar_sales_by_outlet(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Outlet_Identifier", y="Total_Sales",
        color="Total_Sales", color_continuous_scale=SEQUENTIAL,
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "Outlet_Identifier": "Outlet"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(coloraxis_showscale=False)
    return _apply_defaults(fig, "🏪 Total Sales by Outlet")


def bar_outlet_type(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Outlet_Type", y="Total_Sales",
        color="Outlet_Type",
        color_discrete_sequence=[PRIMARY, SECONDARY, ACCENT, "#8E44AD"],
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "Outlet_Type": "Store Type"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    return _apply_defaults(fig, "🏬 Sales by Outlet Type")


def bar_outlet_size(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Outlet_Size", y="Total_Sales",
        color="Outlet_Size",
        color_discrete_sequence=[ACCENT, PRIMARY, SECONDARY],
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "Outlet_Size": "Store Size"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    return _apply_defaults(fig, "📐 Sales by Outlet Size")


def bar_location_tier(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Outlet_Location_Type", y="Total_Sales",
        color="Outlet_Location_Type",
        color_discrete_sequence=[PRIMARY, SECONDARY, ACCENT],
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "Outlet_Location_Type": "City Tier"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    return _apply_defaults(fig, "📍 Sales by City Location Tier")


def line_establishment_year(df_grp: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_grp["Outlet_Establishment_Year"],
        y=df_grp["Total_Sales"],
        mode="lines+markers+text",
        line=dict(color=PRIMARY, width=3),
        marker=dict(size=9, color=SECONDARY),
        text=df_grp["Total_Sales"].apply(lambda v: f"₹{v:,.0f}"),
        textposition="top center",
        name="Total Sales",
    ))
    return _apply_defaults(fig, "📅 Sales by Outlet Establishment Year")


def bar_outlet_age(df_grp: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_grp, x="Age_Group", y="Total_Sales",
        color="Age_Group",
        color_discrete_sequence=[PRIMARY, SECONDARY, ACCENT, "#8E44AD"],
        text="Revenue_Share_Pct",
        labels={"Total_Sales": "Total Sales (₹)", "Age_Group": "Outlet Age"},
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    return _apply_defaults(fig, "⏳ Sales by Outlet Age Group")


# ─────────────────────────────────────────────
# PRODUCT PERFORMANCE CHARTS
# ─────────────────────────────────────────────

def bar_top_products(df_top: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        df_top, x="Total_Sales", y="Item_Identifier",
        orientation="h",
        color="Item_Type",
        color_discrete_sequence=CATEGORY_COLORS,
        text="Total_Sales",
        labels={"Total_Sales": "Total Sales (₹)", "Item_Identifier": "Product ID"},
    )
    fig.update_traces(texttemplate="₹%{text:,.0f}", textposition="outside")
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return _apply_defaults(fig, "🏆 Top 15 Products by Total Sales")


def scatter_mrp_vs_sales(df: pd.DataFrame) -> go.Figure:
    sample = df.sample(min(1500, len(df)), random_state=42)
    fig = px.scatter(
        sample, x="Item_MRP", y="Item_Outlet_Sales",
        color="Outlet_Type",
        size="Item_Visibility",
        hover_data=["Item_Identifier", "Item_Type"],
        color_discrete_sequence=CATEGORY_COLORS,
        opacity=0.65,
        labels={"Item_MRP": "Item MRP (₹)", "Item_Outlet_Sales": "Sales (₹)"},
        trendline="ols",
    )
    return _apply_defaults(fig, "📈 MRP vs. Sales (with trend line)")


def box_sales_by_item_type(df: pd.DataFrame) -> go.Figure:
    fig = px.box(
        df, x="Item_Type", y="Item_Outlet_Sales",
        color="Item_Type",
        color_discrete_sequence=CATEGORY_COLORS,
        labels={"Item_Outlet_Sales": "Sales (₹)", "Item_Type": "Category"},
    )
    fig.update_layout(showlegend=False, xaxis_tickangle=-35)
    return _apply_defaults(fig, "📦 Sales Distribution per Category (Box Plot)")


def histogram_sales(df: pd.DataFrame) -> go.Figure:
    fig = px.histogram(
        df, x="Item_Outlet_Sales", nbins=60,
        color_discrete_sequence=[PRIMARY],
        labels={"Item_Outlet_Sales": "Sales (₹)", "count": "Frequency"},
    )
    fig.update_traces(marker_line_color="white", marker_line_width=0.5)
    return _apply_defaults(fig, "📊 Sales Frequency Distribution")


def heatmap_outlet_x_category(pivot: pd.DataFrame) -> go.Figure:
    fig = px.imshow(
        pivot,
        color_continuous_scale=SEQUENTIAL,
        aspect="auto",
        labels=dict(color="Sales (₹)"),
    )
    return _apply_defaults(fig, "🔥 Heatmap – Outlet Type × Product Category Sales")


def violin_outlet_type(df: pd.DataFrame) -> go.Figure:
    fig = px.violin(
        df, x="Outlet_Type", y="Item_Outlet_Sales",
        color="Outlet_Type",
        box=True, points="outliers",
        color_discrete_sequence=CATEGORY_COLORS,
        labels={"Item_Outlet_Sales": "Sales (₹)", "Outlet_Type": "Store Type"},
    )
    fig.update_layout(showlegend=False)
    return _apply_defaults(fig, "🎻 Sales Distribution by Outlet Type (Violin)")


def funnel_category(df_grp: pd.DataFrame) -> go.Figure:
    fig = go.Figure(go.Funnel(
        y=df_grp["Item_Type"].head(8),
        x=df_grp["Total_Sales"].head(8),
        textinfo="value+percent total",
        marker=dict(color=px.colors.sequential.Oranges[1:9]),
    ))
    return _apply_defaults(fig, "🔻 Sales Funnel – Top 8 Categories")


def bar_item_category_type(df: pd.DataFrame) -> go.Figure:
    grp = (
        df.groupby(["Item_Category", "Item_Type"])["Item_Outlet_Sales"]
        .sum().reset_index()
    )
    fig = px.bar(
        grp, x="Item_Category", y="Item_Outlet_Sales",
        color="Item_Type",
        barmode="stack",
        color_discrete_sequence=CATEGORY_COLORS,
        labels={"Item_Outlet_Sales": "Total Sales (₹)", "Item_Category": "Broad Category"},
    )
    return _apply_defaults(fig, "📚 Stacked Sales – Broad Category × Product Type")
