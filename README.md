# Vendor Performance Analysis : Retail Inventory & Sales

> Most retail businesses know which vendors they buy from but very few know which vendors are actually worth buying from  and which ones are quietly draining profit through slow-moving stock, inflated unit costs, and underperforming brands.
This project answers that question by building a full data pipeline across sales, purchase, vendor and inventory data, it identifies exactly where money is being made, where it is being lost, and where bulk purchasing can cut unit costs by up to 72%  with a Power BI dashboard that makes the findings accessible to anyone in the business without touching a spreadsheet.
---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Methods](#methods)
- [Data Cleaning & Preparation](#data-cleaning--preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Key Insights](#key-insights)
- [Dashboard](#dashboard)
- [Project Structure](#project-structure)
- [How to Run This Project](#how-to-run-this-project)
- [Final Recommendations](#final-recommendations)
- [Author & Contact](#author--contact)

---

## Overview

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing and inventory optimization. A complete data pipeline was built using SQL for ETL, Python for analysis and hypothesis testing, and Power BI for data visualization.

---

## Problem Statement

Effective inventory and sales management are critical in the retail sector. This project aims to:

- Identify underperforming brands that need pricing and promotional adjustments
- Determine vendor contributions to sales and profit
- Analyze the cost-benefit of bulk purchasing
- Investigate inventory turnover inefficiencies
- Statistically validate differences in vendor profitability

---

## Dataset

- Multiple CSV files loaded in `/Data/` folder (sales, purchase, vendors, inventory)
- A summary table is created from ingested data and used for analytics

---

## Tools & Technologies

- **SQL** — Joins, filters, Common Table Expressions (CTEs)
- **Python** — Big data ingestion into database; visualization using Matplotlib, Seaborn, Pandas
- **Power BI** — Interactive dashboards and visualizations
- **GitHub** — Version control and project hosting

---

## Methods

- Data is ingested into an SQLite database
- Unwanted files and erroneous records are removed during the data cleaning process
- Final summary file `vendor_invoice_summary` is created for all further analysis
- Using Matplotlib and Seaborn, various charts are drawn: scatter plot, histogram, bar plot, pie chart, heatmap
- Analysis is performed by filtering on numerical variables such as profit margin, gross profit, and total sales dollars
- Key findings derived:
  - Top vendors and brand counts
  - Purchase contribution of vendors
  - Low-performing vendors and brands
  - Top vendors by sales performance
  - Impact of bulk purchasing on unit price
  - Low inventory turnover products
  - Unsold inventory items

---

## Data Cleaning & Preparation

Records were filtered and removed based on the following conditions:

- Gross Profit < 0
- Profit Margin < 0
- Sales Quantity = 0

A consolidated summary table named `vendor_invoice_summary` was created for downstream analysis.

---

## Exploratory Data Analysis

**Negative or Zero Values Detected:**

- **Gross Profit:** Loss-making sales detected (Min: −52,000)
- **Profit Margin:** Sales at zero or below cost
- **Unsold Inventory:** Indicating slow-moving stock

**Outliers Identified:**

- High freight costs (up to 257K)
- Unusually large purchase quantities

**Correlation Analysis:**

- **Heatmap Insights:** Strong positive correlation between total sales dollars, total purchase dollars, and gross profit
- **Negative Correlation:** Between sales price and profit margin

---

## Key Insights

- **Heatmap Correlation:** Strong relation between total sales dollars and total purchase dollars with gross profit
- **Purchase Contribution:** Top 10 vendors account for 65.69% of total purchases
- **Bulk Purchasing Impact:** 72% cost saving per unit on large orders, reducing the average unit purchase price significantly
- **Vendor Performance:** Low-performing vendors show higher profit margins but low sales volume — potentially due to premium pricing or lower operational costs
- **Hypothesis Testing:** A statistically significant difference in profit margins exists between top and low sales vendors

---

## Dashboard

Power BI dashboard covers:

- Purchase contribution by vendor
- Top vendors by sales
- Top brands by sales
- Low-performing vendors
- Top 10 low-performing brands

![Dashboard Screenshot 1](<c:\Vendor project\Images\Dashboard_overview_1.png>)
![Dashboard Screenshot 2](<c:\Vendor project\Images\Dashboard_overview_2.png>)

---

## Project Structure

```
vendor-performance-analysis/
│
│── README.md
│── .gitignore
│── requirements.txt
│── Vendor Performance Report.pdf
│
├── notebooks/                        # Jupyter notebooks
│   ├── exploratory_data_analysis.ipynb
│   └── vendor_performance_analysis.ipynb
│
├── scripts/                          # Python scripts for processing
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── dashboard/                        # Power BI dashboard files
│   └── vendor_performance_dashboard.pbix
│
├── dataset/                          # Raw and cleaned datasets
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
└── images/                           # Dashboard screenshots
    └── dashboard_preview.png
```

---

## How to Run This Project

**1. Clone the repository:**

```bash
git clone https://github.com/yourusername/vendor-performance-analysis.git
```

**2. Install required libraries:**

```bash
pip install -r requirements.txt
```

**3. Load the CSVs and ingest into database:**

```bash
python scripts/ingestion_db.py
```

**4. Create the vendor summary table:**

```bash
python scripts/get_vendor_summary.py
```

**5. Open and run the notebooks in order:**

```
notebooks/Ingesting_data.ipynb
notebooks/Exploratory_data_analysis.ipynb
notebooks/Data_visualization.ipynb
```

**6. Open Power BI Dashboard:**

```
dashboard/vendor_performance_dashboard.pbix
```

---

## Final Recommendations

- **Diversify vendor base** to reduce concentration risk
- **Optimize bulk order strategies** to maximize the 72% unit cost saving
- **Reprice slow-moving, high-margin brands** to stimulate sales volume
- **Clear unsold inventory strategically** through promotions or markdowns
- **Improve marketing support** for underperforming vendors to lift sales

---

## Author & Contact

**Harshavardhan Gurav**

- 📧 Email: harshavardhangurav839@gmail.com
- 💼 LinkedIn: *(https://www.linkedin.com/in/harshavardhan-gurav-3284601a2/#:~:text=www.linkedin.com/in/harshavardhan%2Dgurav%2D3284601a2)*
