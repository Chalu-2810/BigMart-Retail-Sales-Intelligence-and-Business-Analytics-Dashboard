# Internship Project Presentation
## Business Analytics Internship — Retail Sales Dashboard
### Sysslan IT Solutions

---

## SLIDE 1 — Title

**Business Analytics Internship**
**BigMart Retail Sales Dashboard**

Presented by: [Your Name]
Internship Track: Business Analytics
Organization: Sysslan IT Solutions
Date: 2024

---

## SLIDE 2 — About the Project

**Project Title:** Retail Sales Dashboard — End-to-End Business Analytics

**Objective:** Analyse BigMart retail sales data to uncover meaningful business
insights and present them through a fully interactive dashboard.

**Dataset:** 5,681 transactions · 10 outlets · 1,543 SKUs · 16 categories

**Tech Stack:** Python · Pandas · NumPy · Plotly · Streamlit

**Levels Completed:** Level 1 → Level 2 → Level 3 → Level 4 → Level 5 ✅

---

## SLIDE 3 — Project Workflow

```
Raw Data → Data Understanding → Data Preparation
        → Sales Analysis → Visualisation → Dashboard & Insights
```

**Level 1 — Data Understanding**
- Loaded dataset (5,681 rows × 11 columns)
- Identified 2 columns with missing values (Item_Weight: 17.18%, Outlet_Size: 28.27%)
- Found 5 variants of Item_Fat_Content — standardisation required
- Detected 353 zero-visibility rows

**Level 2 — Data Preparation**
- Standardised fat content labels → 2 clean categories
- Imputed Item_Weight with per-item median
- Imputed Outlet_Size with mode per outlet type
- Fixed zero visibility with per-category median
- Engineered 4 new features: Outlet_Age, Item_Category, Item_Outlet_Sales, MRP_Band

---

## SLIDE 4 — Key KPIs

| Metric | Value |
|--------|-------|
| 💰 Total Revenue | ₹7,44,710.81 |
| 🧾 Total Transactions | 5,681 |
| 📦 Unique SKUs | 1,543 |
| 🏪 Total Outlets | 10 |
| 📈 Avg Transaction | ₹131.09 |
| 🏆 Top Category | Snack Foods (14.41%) |
| 🏬 Top Outlet Type | Supermarket Type1 (65.74%) |
| 📍 Top City Tier | Tier 3 (39.21%) |

---

## SLIDE 5 — Sales by Product Category

**Top 5 Categories by Revenue:**

1. 🥇 Snack Foods — ₹1,07,284 (14.41%)
2. 🥈 Fruits & Vegetables — ₹1,03,778 (13.94%)
3. 🥉 Household — ₹88,276 (11.85%)
4.  Frozen Foods — ₹70,763 (9.50%)
5.  Dairy — ₹60,984 (8.19%)

**Insight:** Food items dominate at ~76% of all revenue. Snack Foods and
Fruits & Vegetables alone contribute 28% of total sales.

---

## SLIDE 6 — Outlet Performance

**By Outlet Type:**
- Supermarket Type1: ₹4,89,585 (65.74%)
- Grocery Store: ₹91,373 (12.27%)
- Supermarket Type3: ₹82,885 (11.13%)
- Supermarket Type2: ₹80,865 (10.86%)

**By Location Tier:**
- Tier 3: ₹2,92,015 (39.21%) ← Highest
- Tier 2: ₹2,45,211 (32.93%)
- Tier 1: ₹2,07,483 (27.86%)

**Insight:** Tier 3 cities outperform Tier 1 in total revenue — a strong
signal for rural market expansion.

---

## SLIDE 7 — Data Visualisations Built (Level 4)

| Chart Type | Purpose |
|-----------|---------|
| Horizontal Bar | Sales by category (ranked) |
| Donut Pie | Revenue share breakdown |
| Treemap | Category size comparison |
| Grouped Bar | Outlet comparison |
| Line Chart | Sales trend by year |
| Scatter + OLS | MRP vs Sales correlation |
| Box Plot | Sales distribution per category |
| Violin | Outlet type distribution |
| Heatmap | Outlet type × category cross-tab |
| Funnel | Top 8 category sales funnel |
| Histogram | Sales frequency distribution |
| KPI Indicators | Total sales, avg, count, etc. |

---

## SLIDE 8 — Interactive Dashboard (Level 5)

**6-Page Streamlit Dashboard:**

1. 🏠 Executive Summary — KPIs + overview charts
2. 📊 Sales Analytics — Category, fat, MRP, year tabs
3. 🏪 Outlet Performance — By outlet, type, size, tier tabs
4. 📦 Product Performance — Top/bottom SKUs, price scatter
5. 💡 Business Insights — Findings + recommendations
6. 🔬 Data Quality Report — Level 1 & 2 documentation

**Sidebar Filters:** Store Type · City Tier · Outlet Size · Item Category ·
MRP Range · Fat Content

---

## SLIDE 9 — Business Insights

1. Snack Foods + F&V = 28% revenue → protect supply chain
2. Supermarket Type1 = 65.74% revenue → priority format to scale
3. Tier 3 cities lead → first-mover expansion opportunity
4. MRP↔Sales correlation = 0.97 → premiumisation strategy viable
5. Small outlets outperform → format efficiency matters more than size
6. Grocery Stores underperform → optimise for essentials, not volume
7. Low Fat = 63.8% of transactions → health labelling drives conversion
8. Older outlets lag by 3–6% → renovation ROI is positive

---

## SLIDE 10 — Conclusion & Future Scope

**Conclusion:**
This project delivered a complete analytics pipeline from raw data to a
business-ready dashboard. All 5 internship levels were completed with
production-quality Python code, 20+ interactive visualisations, and
8 actionable strategic recommendations.

**Future Scope:**
- Time-series demand forecasting (Prophet / LSTM)
- Customer RFM segmentation (with loyalty data)
- Price elasticity modelling per category
- Geo-spatial outlet site selection analysis
- Basket analysis with association rule mining (Apriori)
- A/B test framework for promotional impact measurement

---

## SLIDE 11 — Thank You

**Sysslan IT Solutions**

Thank you for this learning opportunity.

📧 info@sysslan.com
🌐 www.sysslan.com
LinkedIn: @sysslan-it-solutions

#SysslanITSolutions #SysslanProjects #SysslanInnovation
#BusinessAnalytics #DataAnalytics #RetailAnalytics
