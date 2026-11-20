# Sales Analysis Report
## BigMart Retail Sales — Level 3
**Sysslan IT Solutions · Business Analytics Internship**

> ⚠️ **Data note:** `Item_Outlet_Sales` in this report is a documented,
> reproducible synthetic proxy (the source dataset's test split has no real
> sales column) — see the README's *Data & Methodology* section and
> `src/data_cleaning.add_derived_columns` for the exact formula. Figures
> below illustrate the analysis pipeline, not real BigMart revenue.

---

## 1. Executive Summary

| KPI | Value |
|-----|-------|
| Total Revenue | ₹7,44,710.81 |
| Total Transactions | 5,681 |
| Average Transaction Value | ₹131.09 |
| Median Transaction Value | ₹127.40 |
| Unique Products (SKUs) | 1,543 |
| Unique Outlets | 10 |
| Highest Single Sale | ₹295.20 |
| Sales Std Deviation | ₹59.00 |
| MRP–Sales Correlation | 0.97 (strong positive) |

---

## 2. Methodology

### 2.1 Data Preparation
- Raw dataset cleaned per Level 2 pipeline
- Sales proxy derived: `Item_Outlet_Sales = Item_MRP × (1 − Item_Visibility) × noise_factor`
- Noise factor: uniform random U(0.85, 1.15), seed=42, for realistic variance

### 2.2 Analysis Dimensions
All sales analysis is performed across five key dimensions:
1. Product category (Item_Type)
2. Fat content label
3. Outlet identifier
4. Outlet type / size / location tier
5. Establishment year / outlet age

---

## 3. Sales by Product Category

| Rank | Category | Total Sales (₹) | Avg Sale (₹) | Count | Revenue Share % |
|------|----------|----------------|-------------|-------|----------------|
| 1 | Snack Foods | 1,07,284.90 | 135.98 | 789 | 14.41% |
| 2 | Fruits & Vegetables | 1,03,778.82 | 132.88 | 781 | 13.94% |
| 3 | Household | 88,276.60 | 138.36 | 638 | 11.85% |
| 4 | Frozen Foods | 70,763.63 | 124.15 | 570 | 9.50% |
| 5 | Dairy | 60,984.13 | 134.33 | 454 | 8.19% |
| 6 | Baking Goods | 59,073.76 | 134.87 | 438 | 7.93% |
| 7 | Canned | 57,540.22 | 132.28 | 435 | 7.73% |
| 8 | Health & Hygiene | 46,003.10 | 136.10 | 338 | 6.18% |
| 9 | Meat | 42,147.84 | 135.52 | 311 | 5.66% |
| 10 | Soft Drinks | 38,159.14 | 135.80 | 281 | 5.12% |
| 11 | Breads | 22,437.01 | 135.98 | 165 | 3.01% |
| 12 | Hard Drinks | 20,180.78 | 136.36 | 148 | 2.71% |
| 13 | Starchy Foods | 16,465.21 | 136.07 | 121 | 2.21% |
| 14 | Others | 8,004.37 | 72.11 | 111 | 1.07% |
| 15 | Breakfast | 10,396.22 | 136.79 | 76 | 1.40% |
| 16 | Seafood | 3,215.08 | 128.60 | 25 | 0.43% |

**Key Finding:** Snack Foods and Fruits & Vegetables together account for 28.35% of total revenue, making them the most critical categories for inventory and promotion planning.

---

## 4. Sales by Broad Item Category

| Category | Total Sales (₹) | Revenue Share % | Avg Sale (₹) | Count |
|----------|----------------|----------------|-------------|-------|
| Food (FD) | 5,66,000+ | ~76% | 133.5 | 4,300+ |
| Non-Consumable (NC) | ~1,10,000 | ~15% | 129.8 | ~850 |
| Drinks (DR) | ~68,000 | ~9% | 133.9 | ~530 |

---

## 5. Sales by Fat Content

| Fat Content | Total Sales (₹) | Avg Sale (₹) | Count | Revenue Share % |
|------------|----------------|-------------|-------|----------------|
| Low Fat | ~4,75,000 | 131.5 | 3,668 | 63.8% |
| Regular | ~2,70,000 | 130.5 | 2,013 | 36.2% |

**Key Finding:** Low Fat items command a marginally higher average MRP and dominate volume (63.8% of transactions), reflecting growing consumer health consciousness.

---

## 6. Sales by Outlet

| Outlet | Total Sales (₹) | Avg Sale (₹) | Revenue Share % | Outlet Type |
|--------|----------------|-------------|----------------|-------------|
| OUT049 | 83,314.95 | 134.38 | 11.19% | Supermarket Type1 |
| OUT027 | 82,885.94 | 132.83 | 11.13% | Supermarket Type3 |
| OUT013 | 82,365.98 | 132.63 | 11.06% | Supermarket Type1 |
| OUT046 | 80,756.10 | 130.25 | 10.84% | Supermarket Type1 |
| OUT035 | 80,341.40 | 129.58 | 10.79% | Supermarket Type1 |
| OUT017 | 83,126.39 | 134.73 | 11.16% | Supermarket Type1 |
| OUT018 | 80,865.64 | 130.85 | 10.86% | Supermarket Type2 |
| OUT045 | 81,743.67 | 132.06 | 10.98% | Supermarket Type1 |
| OUT010 | 45,937.76 | 124.15 | 6.17% | Grocery Store |
| OUT019 | 43,373.98 | 123.23 | 5.82% | Grocery Store |

**Key Finding:** Supermarket outlets (OUT049, OUT027, OUT013) dominate revenue. Both Grocery Stores (OUT010, OUT019) show 40–45% lower revenue per outlet, reflecting smaller format and limited SKU assortment.

---

## 7. Sales by Outlet Type

| Outlet Type | Total Sales (₹) | Avg Sale (₹) | Count | Revenue Share % |
|-------------|----------------|-------------|-------|----------------|
| Supermarket Type1 | 4,89,585.75 | 131.72 | 3,717 | 65.74% |
| Grocery Store | 91,373.48 | 126.56 | 722 | 12.27% |
| Supermarket Type3 | 82,885.94 | 132.83 | 624 | 11.13% |
| Supermarket Type2 | 80,865.64 | 130.85 | 618 | 10.86% |

---

## 8. Sales by Outlet Size

| Outlet Size | Total Sales (₹) | Avg Sale (₹) | Revenue Share % |
|-------------|----------------|-------------|----------------|
| Small | 4,16,054.13 | 130.39 | 55.87% |
| Medium | 2,37,283.14 | 132.18 | 31.86% |
| High | 91,373.54 | 132.04 | 12.27% |

---

## 9. Sales by Location Tier

| City Tier | Total Sales (₹) | Avg Sale (₹) | Revenue Share % |
|-----------|----------------|-------------|----------------|
| Tier 3 | 2,92,015.53 | 131.04 | 39.21% |
| Tier 2 | 2,45,211.46 | 131.58 | 32.93% |
| Tier 1 | 2,07,483.82 | 130.55 | 27.86% |

**Key Finding:** Tier 3 cities lead in aggregate sales, suggesting strong rural/semi-urban market penetration opportunities.

---

## 10. Sales by Outlet Establishment Year

| Year | Total Sales (₹) | Avg Sale (₹) | # Outlets |
|------|----------------|-------------|----------|
| 1985 | 82,365.98 | 132.63 | 1 |
| 1987 | 80,341.40 | 129.58 | 1 |
| 1997 | 91,373.48 | 126.56 | 1 |
| 1998 | 45,937.76 | 124.15 | 1 |
| 1999 | 83,314.95 | 134.38 | 1 |
| 2002 | 80,865.64 | 130.85 | 1 |
| 2004 | 82,885.94 | 132.83 | 1 |
| 2007 | 1,64,870.06 | 134.10 | 2 |
| 2009 | 43,373.98 | 123.23 | 1 |

---

## 11. Top 15 Performing Products (SKUs)

| Rank | Item ID | Item Type | MRP (₹) | Total Sales (₹) | Transactions |
|------|---------|-----------|---------|----------------|-------------|
| 1 | FDP15 | Dairy | 255.53 | 1,879.98 | 8 |
| 2 | FDG28 | Frozen Foods | 243.91 | 1,647.91 | 7 |
| 3 | DRM11 | Drinks | 259.33 | 1,642.00 | 7 |
| 4 | NCQ29 | Non-Consumable | 258.83 | 1,622.47 | 7 |
| 5 | FDY58 | Snack Foods | 228.27 | 1,559.87 | 7 |
| 6 | FDK46 | Frozen Foods | 260.66 | 1,521.49 | 6 |
| 7 | FDU43 | Dairy | 239.46 | 1,516.31 | 7 |
| 8 | NCF06 | Non-Consumable | 258.50 | 1,502.25 | 6 |
| 9 | DRF48 | Soft Drinks | 188.39 | 1,465.49 | 8 |
| 10 | NCW30 | Non-Consumable | 260.70 | 1,439.56 | 6 |

**Key Finding:** Top-performing SKUs predominantly have MRP > ₹200, confirming the strong MRP–sales correlation (r = 0.97).

---

## 12. Correlation Analysis

| Relationship | Pearson r | Interpretation |
|-------------|-----------|---------------|
| Item_MRP ↔ Item_Outlet_Sales | 0.9701 | Very strong positive |
| Item_Visibility ↔ Item_Outlet_Sales | ~−0.05 | Near zero / weak negative |
| Item_Weight ↔ Item_MRP | ~0.02 | Negligible |

---

## 13. Skills Demonstrated (Level 3)

- ✅ Overall revenue and performance KPI calculation
- ✅ Multi-dimensional sales aggregation (category, outlet, location)
- ✅ Top/bottom product identification
- ✅ Revenue contribution / market share analysis
- ✅ Correlation analysis (MRP vs sales, visibility vs sales)
- ✅ Cross-tabulation (outlet type × item category)
- ✅ Temporal trend analysis (by establishment year)
- ✅ Business performance metrics generation

---

*Report generated by Sysslan IT Solutions Business Analytics Internship Pipeline*
