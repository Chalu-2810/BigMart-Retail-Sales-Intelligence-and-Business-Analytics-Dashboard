"""
dashboard_utils.py
------------------
Shared helpers for the Streamlit dashboard.
Sysslan IT Solutions – Business Analytics Internship
"""

import pandas as pd
import streamlit as st
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).resolve().parent.parent
DATA_DIR   = BASE_DIR / "data"
RAW_PATH   = DATA_DIR / "raw_dataset.csv"
CLEAN_PATH = DATA_DIR / "cleaned_dataset.csv"


# ── Data Loading (cached) ──────────────────────────────────────────────────────

@st.cache_data(show_spinner="⏳ Loading dataset …")
def load_clean_data() -> pd.DataFrame:
    """Load the cleaned dataset; clean on-the-fly if not present."""
    if not CLEAN_PATH.exists():
        from src.data_cleaning import clean_dataset
        clean_dataset(str(RAW_PATH), str(CLEAN_PATH))
    df = pd.read_csv(CLEAN_PATH)
    # Ensure MRP_Band is categorical ordered
    df["MRP_Band"] = pd.Categorical(
        df["MRP_Band"],
        categories=["< 75", "75-125", "125-175", "175-225", "> 225"],
        ordered=True,
    )
    return df


# ── Page Config ────────────────────────────────────────────────────────────────

def set_page_config():
    st.set_page_config(
        page_title="BigMart Retail Sales Dashboard",
        page_icon="🛒",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def inject_custom_css():
    st.markdown("""
    <style>
    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A3C5E 0%, #0d2137 100%);
    }
    [data-testid="stSidebar"] * { color: #F0F4F8 !important; }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label { color: #E87722 !important; font-weight: 600; }

    /* ── KPI Cards ── */
    .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 18px 22px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        border-left: 5px solid #E87722;
        text-align: center;
    }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #1A3C5E; }
    .kpi-label { font-size: 0.85rem; color: #666; margin-top: 4px; }

    /* ── Insight boxes ── */
    .insight-box {
        background: #FFF8F2;
        border-left: 4px solid #E87722;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
        font-size: 0.95rem;
        color: #2C3E50;
    }

    /* ── Section headers ── */
    .section-header {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1A3C5E;
        border-bottom: 3px solid #E87722;
        padding-bottom: 6px;
        margin-bottom: 16px;
    }

    /* ── Page title ── */
    .page-title {
        font-size: 2rem;
        font-weight: 800;
        color: #1A3C5E;
    }
    .page-subtitle { color: #555; font-size: 1rem; }

    /* ── Data quality badge ── */
    .badge-ok {
        background:#27AE60; color:white; padding:3px 10px;
        border-radius:20px; font-size:0.8rem;
    }
    .badge-warn {
        background:#E87722; color:white; padding:3px 10px;
        border-radius:20px; font-size:0.8rem;
    }

    /* Remove default top padding */
    .block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)


# ── Reusable UI Components ─────────────────────────────────────────────────────

def render_kpi_card(label: str, value, prefix: str = "₹", suffix: str = "") -> None:
    """Render a styled KPI metric card."""
    if isinstance(value, float):
        formatted = f"{prefix}{value:,.2f}{suffix}"
    elif isinstance(value, int):
        formatted = f"{prefix}{value:,}{suffix}"
    else:
        formatted = f"{prefix}{value}{suffix}"
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-value">{formatted}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def render_insight(text: str) -> None:
    st.markdown(f'<div class="insight-box">{text}</div>', unsafe_allow_html=True)


def section_header(title: str) -> None:
    st.markdown(f'<div class="section-header">{title}</div>', unsafe_allow_html=True)


def page_header(title: str, subtitle: str = "") -> None:
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="page-subtitle">{subtitle}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


# ── Sidebar Filter Panel ───────────────────────────────────────────────────────

def sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    """Render sidebar filter widgets and return the filtered DataFrame."""
    st.sidebar.image(
        "https://img.icons8.com/color/96/shopping-cart.png", width=60
    )
    st.sidebar.markdown("## 🛒 BigMart Dashboard")
    st.sidebar.markdown("*Sysslan IT Solutions*")
    st.sidebar.markdown("---")

    st.sidebar.markdown("### 🔎 Filters")

    # Outlet Type
    all_outlet_types = sorted(df["Outlet_Type"].unique())
    sel_outlet_types = st.sidebar.multiselect(
        "Store Type", all_outlet_types, default=all_outlet_types
    )

    # Location Tier
    all_tiers = sorted(df["Outlet_Location_Type"].unique())
    sel_tiers = st.sidebar.multiselect(
        "City Tier", all_tiers, default=all_tiers
    )

    # Outlet Size
    all_sizes = sorted(df["Outlet_Size"].dropna().unique())
    sel_sizes = st.sidebar.multiselect(
        "Outlet Size", all_sizes, default=all_sizes
    )

    # Item Category
    all_categories = sorted(df["Item_Category"].unique())
    sel_categories = st.sidebar.multiselect(
        "Item Category", all_categories, default=all_categories
    )

    # MRP Range
    mrp_min = float(df["Item_MRP"].min())
    mrp_max = float(df["Item_MRP"].max())
    sel_mrp = st.sidebar.slider(
        "MRP Range (₹)", mrp_min, mrp_max, (mrp_min, mrp_max)
    )

    # Fat Content
    all_fat = sorted(df["Item_Fat_Content"].unique())
    sel_fat = st.sidebar.multiselect(
        "Fat Content", all_fat, default=all_fat
    )

    st.sidebar.markdown("---")

    # Apply filters
    mask = (
        df["Outlet_Type"].isin(sel_outlet_types) &
        df["Outlet_Location_Type"].isin(sel_tiers) &
        df["Outlet_Size"].isin(sel_sizes) &
        df["Item_Category"].isin(sel_categories) &
        df["Item_MRP"].between(*sel_mrp) &
        df["Item_Fat_Content"].isin(sel_fat)
    )
    filtered = df[mask].copy()

    st.sidebar.info(f"**Rows after filter:** {len(filtered):,} / {len(df):,}")
    return filtered


def download_button(df: pd.DataFrame, label: str = "Download Filtered Data") -> None:
    """Render a CSV download button for the filtered dataset."""
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=f"⬇️ {label}",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv",
    )
