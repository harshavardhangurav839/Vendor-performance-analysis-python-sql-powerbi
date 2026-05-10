# Vendor performance analysis :Retail inventory & sales

_ Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL,Python and Power BI.
---
## Table of contents 
- <a herf="#Overview"> Overview</a>
- <a href="#problem-statement">Problem Statement</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="methods">Methods</a>
- <a href="#data-cleaning--preparation">Data cleaning & preparation</a>
- <a href="#exploratary-data-analysis">Exploratary data analysis</a>
- <a href="#key-insights">Key Insights</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#project-structure">Project structure</a>
- <a href="how-to-run-this-project">How to run this project</a>
- <a href="#final-recommendation">Final recommendation</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2> <a  class="anchor" id="Overview" <> /a> Overview </h2>

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing 
and inventory optimization. A complete data pipeline was built using SQL for ETL ,Python for analysis and hypothesis testing and 
Power BI for data visualization.

---
<h2> <a  class="anchor" id="problem-statement" <> /a> Problem Statement </h2>

Effective inventory and sales management are critical in the retail sector .This reject aim to:
-Identify underperforming brands needs pricing and promotional adjustments
-Determine vendor contributions to sales and profit
-Analyze the cost-benefit of bulk purchasing 
-Investigate inventory turnover inefficiencies 
-Statistically validate differences in vendor profitability

---
<h2> <a  class="anchor" id="dataset" <> /a> Dataset </h2>

-Multiple CSV files is loaded in  '/Data/' folder (sales,purchase,vendors,inventory)
-Summary table is created from ingested data and used for analytics

---
<h2> <a  class="anchor" id="tools--technologies" <> /a> Tools & Technologies </h2>

-SQL(Joins, filters, Common table  )
-Python(big data ingesting in database, Visualization modules like mathplot, seaborn,Pandas)
-Power BI(Interactive visualization)
-Github

---
<h2> <a  class="anchor" id="methods" <> /a> Methods </h2>

-Data get ingested in sqlite database 
-In EDA, the unwanted files and data from files got removed by data cleaning process.
-Final file "Vendor_invoice_summary" is formed on which further analysis is done
-Using modules matplot and seaborn various charts like scatterplot, histogram,barplot,pie chart,heatmap is drawn
-Analysis is done by filtering using numerical variables like profit margin,gross profit, total sales dollars.
-Then we find out top vendors and brands count, purchase contribution of vendors,low performing vendors and brands,
top vendors by sale performance,impact of bulk purchasing on unit price , low inventory turnover, Unsold inventory.

---
<h2> <a  class="anchor" id="data-cleaning--preparation" <> /a> Data cleaning & preparation </h2>

-Filter data with:
  -Gross profit< 0
  -Profit margin <0
  -Sales quantity =0
-Created summary table name as vendor_invoice_summary to make analysis on it.

---
<h2> <a  class="anchor" id="exploratary-data-analysis" <> /a> Exploratary data analysis </h2>

**Negative or zero values detected**
- Gross Profit: Loss making sales (Min -52000)
-Profit margin: Sales at zero or below cost 
-Unsold Inventory: Indicating slow-moving stock

**Outliers Identified**
-High freight costs(Upto 257K)
-Large purchase 

**Coorelation analysis**
-Heatmap coorelation Insights:strong relation between the totla sales dollars and total purchase dollars with the gross profit
-Negative between sales price and profit margin


---
<h2> <a  class="anchor" id="key-insights" <> /a> Key Insights </h2>

-**Heatmap coorelation Insights**:strong relation between the totla sales dollars and total purchase dollars with the gross profit
-**Purchase contribution** of top 10 vendors is 65.69%
-**Bulk purchasing impact**:72% cost saving per units in large order so it reduces the average unit purchase price
-**Vendor performance** Low performing vendors with higher profit margin and low sales volume potentially due to premium pricing or lower operational costs
-**Hypothesis testing**:There is significant difference in profit margins between top and low sales vendors find out through hypothesis testing.

---
<h2> <a  class="anchor" id="dashboard" <> /a> Dashboard </h2>

-Power BI dashboard shows:
  -Purchase contribution
  -Top vendors for sales
  -Top brands for sales
  -Low performing vendors
  -Top 10 low performing brands
  -


![alt text](<Screenshot (11).png>)
![alt text](<Screenshot (12).png>)

---
<h2> <a  class="anchor" id="project-structure" <> /a Project structure </h2>



```bash
vendor-performance-analysis/

│── README.md
│── .gitignore
│── requirements.txt
│── Vendor Performance Report.pdf

│
├── notebooks/                     # Jupyter notebooks
│   ├── exploratory_data_analysis.ipynb
│   └── vendor_performance_analysis.ipynb

│
├── scripts/                       # Python scripts for processing
│   ├── ingestion_db.py
│   └── get_vendor_summary.py

│
├── dashboard/                     # Power BI dashboard files
│   └── vendor_performance_dashboard.pbix

│
├── dataset/                       # Raw and cleaned datasets
│   ├── raw_data.csv
│   └── cleaned_data.csv

│
└── images/                        # Dashboard screenshots
    └── dashboard_preview.png
```

---
<h2> <a  class="anchor" id="how-to-run-this-project"<> /a How to run this project </h2>

## How to Run This Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/vendor-performance-analysis.git
```

2. Install required libraries:

```bash
pip install -r requirements.txt
```

3. Load the CSVs and ingest into database:

```bash
python scripts/ingestion_db.py
```

4. Create vendor summary table:

```bash
python scripts/get_vendor_summary.py
```

5. Open and run notebooks:

- notebooks/Ingesting_data.ipynb
- notebooks/Exploratory_data_analysis.ipynb
- notebooks/Data_visualization.ipynb

6. Open Power BI Dashboard:

- dashboard/vendor_performance_dashboard.pbix



---
<h2> <a  class="anchor" id="final-recommendation"<> /a Final recommendation </h2>

-Diversify vendor base to reduce risk
-Optimize bulk order strategies
-Reprice slow moving, high margin brands
-Clear unsold inventory strategically
-Improve marketing for underperforming vendors

---
<h2> <a  class="anchor" id="author--contact"<> /a Author & Contact </h2>

**Harshavardhan Gurav**
-Email:harshavardhangurav839@gmail.com
-Linkdedin:[]



