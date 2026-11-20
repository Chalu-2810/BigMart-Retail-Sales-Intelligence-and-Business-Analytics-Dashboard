"""
data_cleaning.py
----------------
Level 1 & 2 – Data Understanding and Data Preparation
Sysslan IT Solutions – Business Analytics Internship
"""

import pandas as pd
import numpy as np
import os


# ─────────────────────────────────────────────
# LEVEL 1 – DATA UNDERSTANDING
# ─────────────────────────────────────────────

def load_data(filepath: str) -> pd.DataFrame:
    """Load the raw dataset from a CSV file."""
    df = pd.read_csv(filepath)
    print(f"[INFO] Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def dataset_overview(df: pd.DataFrame) -> dict:
    """Return a comprehensive overview of the dataset."""
    overview = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "missing_pct": (df.isnull().mean() * 100).round(2).to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "memory_mb": round(df.memory_usage(deep=True).sum() / 1024**2, 3),
    }
    return overview


def descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Generate descriptive statistics for all columns."""
    num_stats = df.describe().T
    cat_cols = df.select_dtypes(include="object").columns

    def _top_value(s):
        return s.value_counts().index[0] if s.notna().any() else None

    def _top_freq(s):
        return s.value_counts().iloc[0] if s.notna().any() else None

    cat_stats = pd.DataFrame({
        "unique_values": df[cat_cols].nunique(),
        "top_value": df[cat_cols].apply(_top_value),
        "top_freq": df[cat_cols].apply(_top_freq),
    })
    return num_stats, cat_stats


def identify_inconsistencies(df: pd.DataFrame) -> dict:
    """Detect known inconsistencies in categorical columns."""
    fat_values = df["Item_Fat_Content"].value_counts().to_dict()
    outlet_size_missing = int(df["Outlet_Size"].isna().sum())
    zero_visibility = int((df["Item_Visibility"] == 0).sum())
    return {
        "fat_content_variants": fat_values,
        "outlet_size_missing": outlet_size_missing,
        "zero_visibility_rows": zero_visibility,
    }


def print_level1_report(df: pd.DataFrame) -> None:
    """Print a formatted Level 1 report to stdout."""
    print("\n" + "="*60)
    print("  LEVEL 1 – DATA UNDERSTANDING REPORT")
    print("="*60)
    ov = dataset_overview(df)
    print(f"\n📦 Shape            : {ov['shape'][0]} rows, {ov['shape'][1]} columns")
    print(f"💾 Memory           : {ov['memory_mb']} MB")
    print(f"🔁 Duplicate Rows   : {ov['duplicates']}")

    print("\n📋 Column Data Types:")
    for col, dtype in ov["dtypes"].items():
        print(f"   {col:<35} {dtype}")

    print("\n❓ Missing Values:")
    for col, n in ov["missing_values"].items():
        if n > 0:
            print(f"   {col:<35} {n:>5} ({ov['missing_pct'][col]}%)")

    inc = identify_inconsistencies(df)
    print("\n⚠  Inconsistencies Detected:")
    print(f"   Item_Fat_Content variants : {inc['fat_content_variants']}")
    print(f"   Outlet_Size missing       : {inc['outlet_size_missing']}")
    print(f"   Item_Visibility = 0       : {inc['zero_visibility_rows']}")
    print("="*60 + "\n")


# ─────────────────────────────────────────────
# LEVEL 2 – DATA PREPARATION
# ─────────────────────────────────────────────

def clean_fat_content(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise Item_Fat_Content to 'Low Fat' / 'Regular'.

    Normalises case/whitespace first so any future variant of the same
    label (e.g. ' LF ', 'REG') is still mapped correctly instead of being
    silently turned into NaN by an exact-match dictionary.
    """
    normalized = df["Item_Fat_Content"].astype(str).str.strip().str.lower()
    mapping = {
        "lf": "Low Fat",
        "low fat": "Low Fat",
        "reg": "Regular",
        "regular": "Regular",
    }
    df["Item_Fat_Content"] = normalized.map(mapping)
    return df


def fill_item_weight(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing Item_Weight with the median weight of the same Item_Identifier."""
    weight_median = df.groupby("Item_Identifier")["Item_Weight"].transform("median")
    df["Item_Weight"] = df["Item_Weight"].fillna(weight_median)
    # Remaining NaN (items with no matches) → global median
    global_median = df["Item_Weight"].median()
    df["Item_Weight"] = df["Item_Weight"].fillna(global_median)
    return df


def fill_outlet_size(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing Outlet_Size with the mode per Outlet_Type."""
    size_mode = df.groupby("Outlet_Type")["Outlet_Size"].transform(
        lambda s: s.fillna(s.mode().iloc[0] if not s.mode().empty else "Small")
    )
    df["Outlet_Size"] = df["Outlet_Size"].fillna(size_mode)
    return df


def fix_zero_visibility(df: pd.DataFrame) -> pd.DataFrame:
    """Replace zero Item_Visibility with per-item-type median."""
    df["Item_Visibility"] = df["Item_Visibility"].replace(0, np.nan)
    vis_median = df.groupby("Item_Type")["Item_Visibility"].transform("median")
    df["Item_Visibility"] = df["Item_Visibility"].fillna(vis_median)
    return df


def add_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add analytically useful derived columns.

    Notes
    -----
    ``Item_Outlet_Sales`` is a **documented synthetic target**, not a real
    revenue figure. The public BigMart Sales dataset used here ships (in this
    split) without an actual sales column, so a transparent, reproducible
    proxy is generated to make the rest of the analytics pipeline (KPIs,
    correlations, dashboard) demonstrable end-to-end:

        Item_Outlet_Sales = Item_MRP * (1 - Item_Visibility) * noise

    where ``noise`` is drawn from U(0.85, 1.15) with a fixed random seed
    (``np.random.seed(42)``) for full reproducibility. This is intentionally
    disclosed here, in the README, and inside the in-app "Data Quality
    Report" page so the numbers are never mistaken for real transactions.
    If you plug in the official BigMart *training* split (which does include
    a genuine ``Item_Outlet_Sales`` column), simply skip this step and the
    rest of the pipeline works unchanged on real data.
    """
    current_year = 2024
    df["Outlet_Age"] = current_year - df["Outlet_Establishment_Year"]

    # Item category from prefix
    df["Item_Category"] = df["Item_Identifier"].str[:2].map({
        "FD": "Food",
        "DR": "Drinks",
        "NC": "Non-Consumable",
    }).fillna("Other")

    # Synthetic sales proxy — see docstring above for full disclosure.
    np.random.seed(42)
    noise = np.random.uniform(0.85, 1.15, len(df))
    df["Item_Outlet_Sales"] = (df["Item_MRP"] * (1 - df["Item_Visibility"]) * noise).round(2)

    # MRP bands
    df["MRP_Band"] = pd.cut(
        df["Item_MRP"],
        bins=[0, 75, 125, 175, 225, 300],
        labels=["< 75", "75-125", "125-175", "175-225", "> 225"],
    )
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before > after:
        print(f"[INFO] Removed {before - after} duplicate rows.")
    return df


def clean_dataset(raw_path: str, save_path: str) -> pd.DataFrame:
    """Full pipeline: load → clean → save."""
    df = load_data(raw_path)
    print_level1_report(df)

    df = remove_duplicates(df)
    df = clean_fat_content(df)
    df = fill_item_weight(df)
    df = fill_outlet_size(df)
    df = fix_zero_visibility(df)
    df = add_derived_columns(df)

    # Verify no nulls remain in key columns
    remaining_nulls = df[["Item_Weight", "Outlet_Size", "Item_Visibility"]].isnull().sum()
    print("[INFO] Remaining nulls after cleaning:")
    print(remaining_nulls)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"\n[INFO] Cleaned dataset saved → {save_path}")
    print(f"[INFO] Final shape: {df.shape}\n")
    return df


if __name__ == "__main__":
    BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw = os.path.join(BASE, "data", "raw_dataset.csv")
    clean = os.path.join(BASE, "data", "cleaned_dataset.csv")
    clean_dataset(raw, clean)
