# Data Understanding Report
## BigMart Retail Sales — Level 1
**Sysslan IT Solutions · Business Analytics Internship**

---

## 1. Project Overview

| Field | Value |
|-------|-------|
| Dataset | BigMart Sales Data |
| Source | Big Mart Retail Operations |
| Records | 5,681 rows |
| Features | 11 columns (raw) → 15 columns (enriched) |
| Analysis Tool | Python 3.10 / Pandas 2.1 |
| Report Date | 2024 |

---

## 2. Dataset Structure

### 2.1 Column Inventory

| # | Column | Data Type | Nullable | Unique Values | Sample Values |
|---|--------|-----------|----------|---------------|---------------|
| 1 | Item_Identifier | object | No | 1,543 | FDW58, NCN55, DRM11 |
| 2 | Item_Weight | float64 | **Yes** (976) | Continuous | 20.75, 8.3, 14.6 |
| 3 | Item_Fat_Content | object | No | 5 | Low Fat, reg, LF, Regular, low fat |
| 4 | Item_Visibility | float64 | No | Continuous | 0.0076, 0.0384, 0.0996 |
| 5 | Item_Type | object | No | 16 | Snack Foods, Dairy, Others |
| 6 | Item_MRP | float64 | No | Continuous | 107.86, 87.32, 241.75 |
| 7 | Outlet_Identifier | object | No | 10 | OUT049, OUT017, OUT010 |
| 8 | Outlet_Establishment_Year | int64 | No | 9 | 1999, 2007, 1998 |
| 9 | Outlet_Size | object | **Yes** (1,606) | 3 | Medium, Small, High |
| 10 | Outlet_Location_Type | object | No | 3 | Tier 1, Tier 2, Tier 3 |
| 11 | Outlet_Type | object | No | 4 | Supermarket Type1, Grocery Store |

---

## 3. Missing Value Analysis

| Column | Missing Count | Missing % | Impact | Action |
|--------|--------------|-----------|--------|--------|
| Item_Weight | 976 | 17.18% | Medium | Impute with per-item median |
| Outlet_Size | 1,606 | 28.27% | High | Impute with mode per outlet type |
| All others | 0 | 0% | None | No action needed |

**Total missing cells: 2,582 out of 62,491 (4.13% of dataset)**

---

## 4. Duplicate Records

- **Exact duplicate rows found: 0**
- The dataset is free of full row duplicates.

---

## 5. Inconsistencies Identified

### 5.1 Item_Fat_Content — Multiple Representations

| Value Found | Count | Standardised To |
|-------------|-------|----------------|
| Low Fat | 3,396 | Low Fat |
| Regular | 1,935 | Regular |
| LF | 206 | Low Fat |
| reg | 78 | Regular |
| low fat | 66 | Low Fat |

**Total affected: 350 rows (6.16%) with non-standard labels**

### 5.2 Item_Visibility — Zero Values

- **353 rows** have `Item_Visibility = 0.0`
- A visibility of zero is physically impossible (an item must occupy some shelf space to be sold).
- These are data entry errors and will be replaced with the per-category median.

### 5.3 Outlet_Size — High Null Rate

- 1,606 missing (28.27%) — likely a data collection gap for certain outlet chains.
- Pattern: All nulls correspond to `Supermarket Type1` and `Supermarket Type2` outlets.

---

## 6. Descriptive Statistics

### 6.1 Numerical Columns

| Statistic | Item_Weight | Item_Visibility | Item_MRP | Outlet_Est_Year |
|-----------|------------|-----------------|----------|-----------------|
| Count | 4,705 | 5,681 | 5,681 | 5,681 |
| Mean | 12.70 | 0.0657 | 141.02 | 1,997.8 |
| Std Dev | 4.66 | 0.0513 | 61.81 | 8.37 |
| Min | 4.555 | 0.000 | 31.99 | 1985 |
| 25th %ile | 8.645 | 0.0270 | 94.41 | 1987 |
| Median | 12.50 | 0.0542 | 141.42 | 1999 |
| 75th %ile | 16.70 | 0.0935 | 186.03 | 2004 |
| Max | 21.35 | 0.3236 | 266.59 | 2009 |

### 6.2 Categorical Columns

| Column | Unique | Top Value | Top Frequency |
|--------|--------|-----------|--------------|
| Item_Identifier | 1,543 | FDA15 | 10 |
| Item_Fat_Content | 5 | Low Fat | 3,396 |
| Item_Type | 16 | Snack Foods | 789 |
| Outlet_Identifier | 10 | OUT027 | 624 |
| Outlet_Size | 3 | Small | 2,388 |
| Outlet_Location_Type | 3 | Tier 3 | 2,388 |
| Outlet_Type | 4 | Supermarket Type1 | 3,717 |

---

## 7. Item Type Distribution

| Item Type | Count | % of Dataset |
|-----------|-------|-------------|
| Snack Foods | 789 | 13.89% |
| Fruits and Vegetables | 781 | 13.75% |
| Household | 638 | 11.23% |
| Frozen Foods | 570 | 10.03% |
| Dairy | 454 | 7.99% |
| Baking Goods | 438 | 7.71% |
| Canned | 435 | 7.66% |
| Health and Hygiene | 338 | 5.95% |
| Meat | 311 | 5.47% |
| Soft Drinks | 281 | 4.95% |
| Breads | 165 | 2.91% |
| Hard Drinks | 148 | 2.61% |
| Starchy Foods | 121 | 2.13% |
| Others | 111 | 1.95% |
| Breakfast | 76 | 1.34% |
| Seafood | 25 | 0.44% |

---

## 8. Outlet Distribution

| Outlet ID | Count | Outlet Type | Location | Size |
|-----------|-------|-------------|----------|------|
| OUT013 | 621 | Supermarket Type1 | Tier 3 | High |
| OUT027 | 624 | Supermarket Type3 | Tier 3 | Medium |
| OUT017 | 617 | Supermarket Type1 | Tier 2 | — |
| OUT035 | 620 | Supermarket Type1 | Tier 2 | Small |
| OUT018 | 618 | Supermarket Type2 | Tier 3 | Medium |
| OUT045 | 619 | Supermarket Type1 | Tier 2 | — |
| OUT046 | 620 | Supermarket Type1 | Tier 1 | Small |
| OUT049 | 620 | Supermarket Type1 | Tier 1 | Medium |
| OUT010 | 370 | Grocery Store | Tier 3 | — |
| OUT019 | 352 | Grocery Store | Tier 1 | Small |

---

## 9. Skills Demonstrated (Level 1)

- ✅ Dataset loading and initial exploration
- ✅ Column identification and type inference
- ✅ Missing value detection and quantification
- ✅ Duplicate record detection
- ✅ Categorical inconsistency identification
- ✅ Basic descriptive statistics generation
- ✅ Distribution analysis
- ✅ Data quality assessment and reporting

---

*Report generated by Sysslan IT Solutions Business Analytics Internship Pipeline*
