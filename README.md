# 🛒 BigMart Retail Sales Intelligence & Business Analytics Dashboard 📊

### 🎓 Business Analytics Internship Project | 🏢 Sysslan IT Solutions

<p align="center">
  <strong>🚀 Turning Retail Data into Meaningful Business Insights!</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
</p>

<p align="center">
  <a href="(https://bigmart-retail-sales-intelligence-and-business-analytics-dashb.streamlit.app/)">
    <strong>🌐 LIVE DASHBOARD | EXPLORE THE PROJECT 🚀</strong>
  </a>
</p>

---

## 🌟 1. Project Overview

Welcome to **BigMart Retail Sales Intelligence & Business Analytics Dashboard**! 🛍️

This project was developed as part of my **Business Analytics Internship at Sysslan IT Solutions**, with the objective of transforming raw retail data into meaningful analytical insights and interactive business intelligence visualizations.

Using Python and modern data analytics technologies, this project demonstrates an end-to-end analytical workflow, covering:

- 📥 Raw data ingestion and understanding.
- 🧹 Data cleaning and preprocessing.
- 🔍 Exploratory Data Analysis (EDA).
- 📊 Statistical analysis and KPI development.
- 📈 Interactive data visualization.
- 🏬 Product and outlet performance analysis.
- 💡 Business insight generation.
- 🖥️ Interactive dashboard development.

The application brings these capabilities together in a Streamlit dashboard, allowing users to explore retail data through interactive charts, metrics, and analytical views.

### 🎯 Project Highlights

| ⭐ Feature | 📝 Description |
|---|---|
| 📊 Data Analytics | End-to-end analytical workflow |
| 🧹 Data Preparation | Cleaning, transformation, and feature engineering |
| 🔍 EDA | Statistical and exploratory analysis |
| 📈 Visualization | Interactive Plotly charts |
| 🖥️ Dashboard | Streamlit-based analytical interface |
| 🧪 Testing | Automated tests using pytest |
| ⚙️ CI Pipeline | GitHub Actions integration |
| 🐳 Containerization | Docker support |

---

## 🎯 2. Business Problem

Retail organizations work with large volumes of product and outlet data. However, raw datasets do not automatically provide the insights needed for informed business decisions.

This project explores several important business questions:

- 🛒 Which product categories contribute the largest share of the calculated sales metric?
- 🏬 How do different outlet types compare?
- 🌍 Which location tiers show stronger aggregate performance?
- 💰 How are product prices distributed?
- 📦 What patterns can be identified across product categories?
- 📉 Which outlet characteristics deserve further investigation?

**Our goal:** Transform raw retail data into structured information and interactive business insights. 🚀

---

## 🌐 3. Live Dashboard

<kbd>🚀 EXPLORE THE DEPLOYED APPLICATION</kbd>

🔗 **Live Application:**  
(https://bigmart-retail-sales-intelligence-and-business-analytics-dashb.streamlit.app/)

📊 Explore the dashboard and interact with its analytical visualizations.

---

## 🖥️ 4. Dashboard Modules

The application brings together multiple analytical views.

| 📌 Module | ✨ Capabilities |
|---|---|
| 📊 Executive Summary | Key metrics and analytical overview |
| 🛍️ Product Analysis | Product category comparisons |
| 🏬 Outlet Analysis | Outlet types and location analysis |
| 💰 Pricing Analysis | MRP distributions and price bands |
| 🧹 Data Quality | Data quality assessment and methodology |
| 💡 Business Insights | Analytical observations and findings |

---

## 🏗️ 5. Project Architecture

The project follows a modular data analytics pipeline.

```text
             📥 RAW DATASET
                    |
                    ▼
          🔍 DATA UNDERSTANDING
                    |
                    ▼
           🧹 DATA PREPARATION
                    |
                    ▼
        📊 EXPLORATORY ANALYSIS
                    |
                    ▼
         📈 DATA VISUALIZATION
                    |
                    ▼
          🖥️ STREAMLIT DASHBOARD
                    |
                    ▼
          💡 BUSINESS INSIGHTS
```

Each stage is implemented through dedicated Python modules, supporting maintainability, testing, and reusability.

---

## 📂 6. Repository Structure

```text
📁 Retail_Sales_Dashboard/
│
├── 🐍 app.py
├── 📦 requirements.txt
├── 🧪 requirements-dev.txt
├── 🐳 Dockerfile
├── 📖 README.md
├── 📄 RESUME.md
├── ⚖️ LICENSE
│
├── 📁 data/
│   ├── 📄 raw_dataset.csv
│   └── 📄 cleaned_dataset.csv
│
├── 📁 src/
│   ├── 🐍 __init__.py
│   ├── 🧹 data_cleaning.py
│   ├── 📊 analysis.py
│   ├── 📈 visualization.py
│   └── 🖥️ dashboard_utils.py
│
├── 📁 tests/
│   ├── 🧪 conftest.py
│   ├── 🧪 test_data_cleaning.py
│   └── 🧪 test_analysis.py
│
├── 📁 reports/
│   ├── 📄 Data_Understanding_Report.md
│   ├── 📄 Analysis_Report.md
│   └── 📄 Business_Insights_Report.md
│
├── 📁 notebooks/
│   └── 📓 analysis.ipynb
│
├── 📁 assets/
│   └── 📊 workflow_diagram.mermaid
│
├── 📁 presentation/
│   └── 📽️ Internship_Project_PPT.md
│
└── 📁 .github/
    └── 📁 workflows/
        └── ⚙️ ci.yml
```

---

## 📊 7. Dataset Description

The project uses the public **BigMart Sales dataset**.

The dataset contains product-level and outlet-level attributes that support retail analytics and exploratory investigation.

### 📋 Dataset Features

| 🔑 Feature | 📝 Description |
|---|---|
| Item_Identifier | Unique product identifier |
| Item_Weight | Product weight |
| Item_Fat_Content | Product fat-content classification |
| Item_Visibility | Product shelf visibility |
| Item_Type | Product category |
| Item_MRP | Maximum Retail Price |
| Outlet_Identifier | Unique outlet identifier |
| Outlet_Establishment_Year | Outlet establishment year |
| Outlet_Size | Outlet size |
| Outlet_Location_Type | Outlet location tier |
| Outlet_Type | Outlet classification |

### 📦 Dataset Dimensions

| Dataset | 📏 Rows | 📊 Columns |
|---|---:|---:|
| Raw Dataset | 5,681 | 11 |
| Cleaned Dataset | 5,681 | 15 |

### ⚙️ Engineered Features

The preprocessing pipeline generates additional analytical features:

- 🏬 `Outlet_Age`
- 🛍️ `Item_Category`
- 💰 `Item_Outlet_Sales`
- 🏷️ `MRP_Band`

---

## ⚠️ 8. Data & Methodology: Important Transparency Note

🔍 **Understanding the sales metric is essential when interpreting the results.**

The public BigMart dataset split used in this project does not contain the original `Item_Outlet_Sales` target column.

To demonstrate the complete analytics workflow, the project generates a reproducible synthetic sales proxy using the following documented formula:

```python
Item_Outlet_Sales = (
    Item_MRP
    * (1 - Item_Visibility)
    * noise
)
```

Where:

- 💰 `Item_MRP` represents the product's maximum retail price.
- 👁️ `Item_Visibility` represents shelf visibility.
- 🎲 `noise` is generated within the range 0.85 to 1.15.
- 🔁 A fixed random seed of 42 ensures reproducibility.

### 📌 Important Considerations

- The generated metric is **not actual BigMart revenue**.
- Dashboard sales-related figures are calculated using this synthetic proxy.
- Product and outlet comparisons are exploratory results based on the proxy.
- The MRP–sales relationship is influenced by the formula itself.
- The findings must not be interpreted as verified real-world financial performance.

The synthetic metric generation is documented in the preprocessing code, README, and dashboard's Data Quality section.

### 🔮 Future Data Integration

The pipeline can be adapted to use the official BigMart training dataset containing genuine `Item_Outlet_Sales` values.

This would allow the analytical findings to be recalculated and validated against actual sales observations.

---

## 📈 9. Key Analytical Findings

The following results were calculated using the cleaned dataset and synthetic sales proxy.

| 📊 Metric | 🏆 Observed Result |
|---|---:|
| 💰 Calculated Sales Proxy Total | ₹7,44,710.81 |
| 🥇 Top Product Category | Snack Foods |
| 📈 Snack Foods Share | 14.41% |
| 🏬 Leading Outlet Type | Supermarket Type1 |
| 📊 Supermarket Type1 Share | 65.74% |
| 🌍 Leading Location Tier | Tier 3 |
| 🏆 Highest Calculated Outlet Metric | OUT049 |
| 🔗 MRP–Proxy Correlation | 0.97 |

> ⚠️ These are exploratory results derived from the synthetic sales proxy, not actual BigMart financial results. The correlation is expected to be high because MRP is an input to the proxy formula.

---

## 🛠️ 10. Technology Stack

| 💻 Technology | 🎯 Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🐼 Pandas | Data manipulation and analysis |
| 🔢 NumPy | Numerical computation |
| 📈 Plotly | Interactive visualizations |
| 🖥️ Streamlit | Dashboard development |
| 🤖 Scikit-learn | Supporting analytical utilities |
| 📊 Statsmodels | Statistical analysis |
| 🧪 pytest | Automated testing |
| 📉 pytest-cov | Test coverage |
| 🧹 Flake8 / Black | Code quality and formatting |
| 🐙 Git & GitHub | Version control |
| ⚙️ GitHub Actions | Continuous integration |
| 🐳 Docker | Containerization |

---

## ⚙️ 11. Installation & Local Setup

Want to run the dashboard on your own computer? Follow these steps! 💻

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/bigmart-retail-sales-analytics-dashboard.git
```

```bash
cd bigmart-retail-sales-analytics-dashboard
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Environment

**🪟 Windows:**

```powershell
venv\Scripts\activate
```

**🐧 macOS / Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### 5️⃣ Launch the Dashboard 🚀

```bash
streamlit run app.py
```

🌐 Open your browser:

```text
http://localhost:8501
```

🎉 Your BigMart analytics dashboard is ready!

---

## 🐳 12. Docker Deployment

Containerize and run the application using Docker.

### 🔨 Build the Docker Image

```bash
docker build -t bigmart-dashboard .
```

### ▶️ Run the Container

```bash
docker run -p 8501:8501 bigmart-dashboard
```

🌐 Access the application:

```text
http://localhost:8501
```

---

## 🧪 13. Testing & Quality Assurance

Quality and reliability are supported through an automated testing workflow.

### 🔬 Run Unit Tests

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

```bash
pytest tests/ -v
```

### 📊 Generate Test Coverage

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

### 🧹 Run Code Quality Checks

```bash
flake8 src tests app.py
```

### ⚙️ Continuous Integration

GitHub Actions automatically runs the configured linting and test workflow on pushes and pull requests.

The configured workflow covers:

- 🐍 Python 3.10
- 🐍 Python 3.11
- 🐍 Python 3.12

The test suite includes checks for:

- 🧹 Missing-value handling.
- 🏷️ Category standardization.
- 🔁 Synthetic sales reproducibility.
- 📊 KPI correctness.
- 📈 Aggregation and sorting logic.

---

## 🎓 14. Internship Levels Completed

The project is organized into five development levels.

| 🎯 Level | 📚 Work Completed | 🚦 Status |
|---|---|---|
| 1️⃣ | Data Understanding | ✅ Completed |
| 2️⃣ | Data Preparation | ✅ Completed |
| 3️⃣ | Sales Analysis | ✅ Completed |
| 4️⃣ | Data Visualization | ✅ Completed |
| 5️⃣ | Dashboard & Business Insights | ✅ Completed |

---

## 💡 15. Skills Demonstrated

### 📊 Data Analytics
- 🔍 Data profiling and quality assessment.
- 🧹 Data cleaning and preprocessing.
- 📈 Exploratory Data Analysis.
- ⚙️ Feature engineering.
- 📉 Statistical analysis and correlation.
- 🎯 KPI development and aggregation.

### 🏢 Business Intelligence
- 🛍️ Retail analytics.
- 🏬 Product and outlet comparisons.
- 📊 Business performance analysis.
- 💡 Business insight generation.
- 🖥️ Interactive dashboard development.

### 💻 Technical Skills
- 🐍 Python, Pandas, and NumPy.
- 📈 Streamlit and Plotly.
- 🧪 Unit testing with pytest.
- 🐙 Git and GitHub.
- ⚙️ GitHub Actions.
- 🐳 Docker.
- 📝 Technical documentation.

---

## 🔭 16. Future Enhancements

The project can be extended with additional analytical and predictive capabilities.

- 📥 Integrate genuine BigMart sales data.
- 📊 Revalidate all business findings against real sales values.
- 🤖 Introduce a demand forecasting model.
- 🏬 Add advanced outlet-level drill-down analysis.
- 🛍️ Develop deeper product-level insights.
- 🗄️ Introduce a database-backed analytics layer.
- 🧪 Expand automated testing and dashboard validation.

---

## 🤝 17. Contributions

Ideas, suggestions, and constructive feedback are welcome! 💬

You can contribute by:

- 🐛 Reporting bugs.
- 💡 Suggesting improvements.
- 🔧 Enhancing analytical functionality.
- 📈 Improving visualizations.
- 🔀 Submitting pull requests.

---

## 📄 18. License

⚖️ This project is released under the **MIT License**.

Refer to the `LICENSE` file for additional information.

---

## 👩‍💻 19. Project Information

| 📌 Detail | 📝 Information |
|---|---|
| 🚀 Project | BigMart Retail Sales Intelligence & Business Analytics Dashboard |
| 🏢 Organization | Sysslan IT Solutions |
| 🎓 Internship Track | Business Analytics |
| 📊 Domain | Retail Analytics & Business Intelligence |
| 💻 Programming Language | Python |
| 🖥️ Framework | Streamlit |
| 📈 Visualization | Plotly |


---

<p align="center">
  <strong>📊 Turning Data into Insights. 💡 Turning Insights into Better Decisions. 🚀</strong>
</p>

<p align="center">
  ⭐ If you find this project interesting, consider giving the repository a star!
</p>

<p align="center">
  💙 Built with Python, curiosity, and a data-driven mindset.
</p>
