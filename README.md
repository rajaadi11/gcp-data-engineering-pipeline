# 🚀 GCP Data Engineering Pipeline

<p align="center">

**An End-to-End Cloud Data Engineering & Analytics Pipeline**

Built with **Python · Pandas · SQL · Google BigQuery · GCP**

<br/>

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Google%20Cloud-GCP-orange?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Google Cloud"/>
<img src="https://img.shields.io/badge/BigQuery-Data%20Warehouse-4285F4?style=for-the-badge&logo=googlebigquery&logoColor=white" alt="BigQuery"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
<img src="https://img.shields.io/badge/SQL-Analytics-CC2927?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL"/>

<br/>

<img src="https://img.shields.io/badge/ETL-Pipeline-success?style=flat-square" alt="ETL"/>
<img src="https://img.shields.io/badge/Data%20Quality-Automated-success?style=flat-square" alt="Data Quality"/>
<img src="https://img.shields.io/badge/Cloud%20Analytics-BigQuery-blue?style=flat-square" alt="Cloud Analytics"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" alt="Status"/>

</p>

---

## 📌 Overview

**GCP Data Engineering Pipeline** is an end-to-end data engineering project that transforms raw retail sales data into a **clean, validated, analytics-ready dataset** and loads it into **Google BigQuery** for analytical processing.

The project demonstrates a practical data engineering workflow covering:

> **Data Ingestion → Exploration → Cleaning → Validation → Cloud Data Warehouse → SQL Analytics → Business Insights**

The pipeline is designed with a modular structure so individual stages can be developed, tested, and extended independently.

---

## ⚡ At a Glance

| Metric               |              Result |
| -------------------- | ------------------: |
| 📦 Records Processed |           **9,993** |
| 🧱 Columns           |               **9** |
| ❌ Missing Values     |               **0** |
| 🔁 Duplicate Records |               **0** |
| ☁️ Cloud Warehouse   | **Google BigQuery** |
| 🗃️ Dataset          | **`sales_dataset`** |
| 📊 Table             |   **`sales_table`** |
| 💰 Total Sales       |    **2,296,919.49** |
| 📈 Total Profit      |      **286,409.08** |
| 📦 Total Quantity    |          **37,871** |
| 🏷️ Avg. Discount    |        **≈ 15.62%** |

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │    RAW CSV DATA      │
                         │    sales_data.csv    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   DATA EXPLORATION   │
                         │     Python/Pandas    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    DATA CLEANING     │
                         │     Python/Pandas    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   DATA VALIDATION    │
                         │   Quality Checks     │
                         └──────────┬───────────┘
                                    │
                              PASS / FAIL
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │      CLEANED DATASET         │
                    │ cleaned_sales_data.csv       │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │    GOOGLE CLOUD      │
                         │       BigQuery       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    sales_dataset     │
                         │          ↓           │
                         │     sales_table      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    ANALYTICAL SQL    │
                         │    KPI & Analysis    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  BUSINESS INSIGHTS   │
                         └──────────────────────┘
```

---

# 🔄 Pipeline Flow

```text
01  Extract
     │
     ▼
02  Explore
     │
     ▼
03  Transform
     │
     ▼
04  Validate
     │
     ▼
05  Load → BigQuery
     │
     ▼
06  Analyze → SQL
     │
     ▼
07  Insights
```

### Pipeline stages

| Stage         | Purpose                         | Technology      |
| ------------- | ------------------------------- | --------------- |
| **Extract**   | Read raw retail data            | CSV             |
| **Explore**   | Understand structure & quality  | Python + Pandas |
| **Transform** | Clean & standardize records     | Python + Pandas |
| **Validate**  | Verify data quality             | Python          |
| **Load**      | Store analytics-ready data      | BigQuery        |
| **Analyze**   | Generate business metrics       | SQL             |
| **Insight**   | Understand business performance | SQL Analysis    |

---

# 🎯 Project Objectives

The project focuses on building a reliable and reproducible data pipeline capable of:

* Processing raw CSV sales data.
* Exploring dataset structure and distributions.
* Cleaning and standardizing records.
* Removing duplicate records.
* Handling missing values.
* Converting columns to appropriate data types.
* Validating data against business rules.
* Loading cleaned data into BigQuery.
* Managing an explicit BigQuery schema.
* Performing analytical SQL queries.
* Generating business KPIs.
* Analyzing regional performance.
* Analyzing category performance.
* Studying monthly sales trends.
* Identifying profitable products.
* Evaluating discount vs. profitability.
* Orchestrating the pipeline through a single Python entry point.

---

# 📊 Dataset

The pipeline processes a retail sales dataset containing transactional information.

### Dataset Dimensions

```text
Records before cleaning : 9,994
Records after cleaning  : 9,993
Columns                 : 9
```

One duplicate record was removed during the cleaning process.

### Dataset Schema

```text
order_id
date
region
category
product
sales
quantity
discount
profit
```

---

# 🧹 Data Engineering Workflow

## 1️⃣ Data Exploration

`data_exploration.py`

The exploration stage provides an initial understanding of the dataset.

It examines:

* Dataset shape.
* Column names.
* Data types.
* Numerical statistics.
* Unique values.
* Category distribution.
* Regional distribution.
* Potential data quality issues.

---

## 2️⃣ Data Cleaning

`data_cleaning.py`

The cleaning stage transforms raw data into a standardized dataset.

### Operations

```text
Raw CSV
   │
   ├── Standardize column names
   ├── Handle missing values
   ├── Remove duplicates
   ├── Convert data types
   ├── Standardize dates
   └── Save cleaned dataset
```

### Input

```text
data/sales_data.csv
```

### Output

```text
data/cleaned_sales_data.csv
```

---

## 3️⃣ Data Validation

`data_validation.py`

Before cloud ingestion, the cleaned dataset passes through automated quality checks.

### Validation checks

```text
✓ Schema Validation
✓ Missing Value Detection
✓ Duplicate Detection
✓ Quantity Validation
✓ Sales Validation
✓ Discount Validation
```

### Validation Result

```text
DATA QUALITY VALIDATION COMPLETE

Total records:       9993
Total columns:       9
Total missing:       0
Total duplicates:    0
Invalid quantities:  0
Invalid sales:       0
Invalid discounts:   0
```

---

# ☁️ Google Cloud Integration

The cleaned dataset is loaded into **Google BigQuery**, which acts as the analytical data warehouse.

```text
Google Cloud Project
        │
        ▼
     BigQuery
        │
        ▼
  sales_dataset
        │
        ▼
   sales_table
```

### BigQuery Table

```text
Dataset : sales_dataset
Table   : sales_table
Rows    : 9,993
Columns : 9
```

---

# 🗃️ BigQuery Schema

| Column     | Type    | Description             |
| ---------- | ------- | ----------------------- |
| `order_id` | STRING  | Unique order identifier |
| `date`     | DATE    | Transaction date        |
| `region`   | STRING  | Sales region            |
| `category` | STRING  | Product category        |
| `product`  | STRING  | Product name            |
| `sales`    | FLOAT   | Sales amount            |
| `quantity` | INTEGER | Quantity sold           |
| `discount` | FLOAT   | Discount applied        |
| `profit`   | FLOAT   | Profit generated        |

An explicit schema is used during the BigQuery loading process rather than relying completely on automatic schema detection.

---

# 📁 Project Structure

```text
gcp-data-engineering-pipeline/
│
├── 📂 data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv
│
├── 📂 scripts/
│   ├── data_exploration.py
│   ├── data_cleaning.py
│   ├── data_validation.py
│   └── load_to_bigquery.py
│
├── 📂 sql/
│   └── analysis_queries.sql
│
├── 📄 run_pipeline.py
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 .gitignore
```

---

# 🧩 Project Components

### 🔍 `data_exploration.py`

Performs exploratory analysis of the raw dataset.

---

### 🧹 `data_cleaning.py`

Handles:

* CSV ingestion.
* Column standardization.
* Missing-value handling.
* Duplicate removal.
* Data-type conversion.
* Basic consistency checks.
* Cleaned dataset generation.

---

### 🛡️ `data_validation.py`

Performs automated data quality validation.

```text
Schema
Missing Values
Duplicates
Quantity
Sales
Discount
```

---

### ☁️ `load_to_bigquery.py`

Handles:

* BigQuery authentication.
* Client creation.
* Cleaned CSV ingestion.
* Schema definition.
* BigQuery load job.
* Load verification.
* Row-count verification.

---

### ⚙️ `run_pipeline.py`

Acts as the pipeline orchestration layer.

Run the entire pipeline with:

```bash
python run_pipeline.py
```

Execution flow:

```text
run_pipeline.py
      │
      ├── Data Cleaning
      │
      ├── Data Validation
      │
      └── BigQuery Load
```

If a pipeline stage fails, execution stops and the failure is reported.

---

# 📈 Analytics Layer

The SQL analytics layer is maintained in:

```text
sql/analysis_queries.sql
```

The project performs the following analyses.

---

## 💰 1. Overall Business KPIs

Calculates:

```text
Total Records
Total Sales
Total Profit
Total Quantity
Average Discount
```

### Result

```text
Total Sales      = 2,296,919.49
Total Profit     =   286,409.08
Total Quantity   =    37,871
Avg. Discount    ≈       15.62%
```

---

# 🌍 2. Regional Performance

Regions are ranked according to total sales.

```text
1. West
2. East
3. Central
4. South
```

### Key Insight

**West** generated the highest total sales among the regions in the dataset.

---

# 🏷️ 3. Category Performance

The dataset contains three major categories:

```text
Technology
Furniture
Office Supplies
```

Sales ranking:

```text
1. Technology
2. Furniture
3. Office Supplies
```

### Key Insight

**Technology** generated the highest total sales and total profit among the categories.

---

# 📅 4. Monthly Sales Trends

Monthly aggregation is used to analyze:

* Sales trends.
* Profit trends.
* Seasonal behavior.
* High-performing periods.
* Low-performing periods.

Example:

```sql
SELECT
    DATE_TRUNC(date, MONTH) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM `YOUR_PROJECT_ID.sales_dataset.sales_table`
GROUP BY month
ORDER BY month;
```

---

# 🏆 5. Product Profitability

Product-level analysis calculates:

```text
Total Sales
Total Profit
Total Quantity
Average Discount
```

This helps identify:

* High-revenue products.
* High-profit products.
* High-volume products.
* Products affected by heavy discounting.

---

# 💸 6. Discount vs. Profitability

Transactions are grouped into discount ranges:

```text
0%
1–10%
11–20%
21–30%
31–40%
41%+
```

The analysis measures:

```text
Transaction Count
Total Sales
Total Profit
Average Profit
```

### Key Insight

Higher discount levels in this dataset are associated with substantially lower profitability, with some high-discount ranges producing negative total profit.

This demonstrates an important business principle:

> **High sales do not necessarily mean high profitability.**

---

# 📊 Key Findings

## 🥇 Regional Leader

```text
West
```

Highest total sales among the analyzed regions.

---

## 🥇 Category Leader

```text
Technology
```

Highest total sales and total profit among the categories.

---

## 💸 Discount Impact

Higher discount ranges show significantly weaker profitability.

This indicates that discounting should be evaluated using **profitability metrics**, not sales revenue alone.

---

# 🧪 Data Quality Summary

| Check              |    Result |
| ------------------ | --------: |
| Records            | **9,993** |
| Columns            |     **9** |
| Missing Values     |     **0** |
| Duplicates         |     **0** |
| Invalid Quantities |     **0** |
| Invalid Sales      |     **0** |
| Invalid Discounts  |     **0** |

### Quality Pipeline

```text
Raw Data
   │
   ▼
Cleaning
   │
   ▼
Validation
   │
   ├── ❌ FAIL → Stop Pipeline
   │
   └── ✅ PASS
          │
          ▼
       BigQuery
```

---

# 🛠️ Technology Stack

### Programming

* 🐍 Python
* 🗄️ SQL

### Python

* Pandas
* Google Cloud BigQuery Client

### Google Cloud

* Google Cloud Platform
* Google BigQuery
* Google Cloud CLI

### Data Engineering

* ETL
* Data Cleaning
* Data Transformation
* Data Validation
* Data Quality
* Data Warehouse
* Analytical SQL
* Pipeline Orchestration

### Development

* Visual Studio Code
* Git
* GitHub
* Google Cloud Console

---

# ⚙️ Getting Started

## Prerequisites

Make sure the following are installed:

```text
Python 3.x
Git
Google Cloud CLI
Google Cloud Account
```

---

## 1. Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd gcp-data-engineering-pipeline
```

---

## 2. Create Virtual Environment

### Windows PowerShell

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Google Cloud Authentication

Authenticate with Google Cloud:

```bash
gcloud auth login
```

Set your project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Configure Application Default Credentials:

```bash
gcloud auth application-default login
```

Verify:

```bash
gcloud config get-value project
```

---

# ▶️ Run the Pipeline

Execute:

```bash
python run_pipeline.py
```

Expected workflow:

```text
============================================================
        GCP DATA ENGINEERING PIPELINE
============================================================

[1] DATA CLEANING
        ↓
[2] DATA VALIDATION
        ↓
[3] BIGQUERY LOAD
        ↓
[✓] PIPELINE COMPLETED SUCCESSFULLY
```

---

# 🔎 Run SQL Analysis

After the BigQuery load completes:

1. Open Google Cloud Console.
2. Navigate to BigQuery.
3. Open `sales_dataset`.
4. Open `sales_table`.
5. Open the SQL workspace.
6. Use:

```text
sql/analysis_queries.sql
```

Replace:

```text
YOUR_PROJECT_ID
```

with your actual Google Cloud project ID.

---

# 🔒 Security

**Never commit credentials to GitHub.**

The repository must not contain:

```text
❌ Service account private keys
❌ application_default_credentials.json
❌ API keys
❌ Passwords
❌ Authentication tokens
❌ .env secrets
❌ Cloud credentials
```

The following should remain ignored:

```text
.venv/
.env
*.json
__pycache__/
```

> Always verify `.gitignore` before pushing the repository.

---

# 🧠 Data Engineering Concepts Demonstrated

This project demonstrates practical understanding of:

```text
                    DATA ENGINEERING
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
         ETL         DATA QUALITY      DATA WAREHOUSE
          │                │                │
          ▼                ▼                ▼
      Python/Pandas    Validation       BigQuery
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                     SQL ANALYTICS
                           │
                           ▼
                    BUSINESS INSIGHTS
```

### Core Concepts

* ETL architecture.
* Data ingestion.
* Data transformation.
* Data cleaning.
* Data quality validation.
* Schema management.
* Cloud data warehousing.
* Analytical SQL.
* Aggregations.
* Pipeline orchestration.
* Cloud authentication.
* Reproducibility.
* Version control.

---

# 🚀 Roadmap

The current project implements the core local-to-cloud pipeline.

Future development can evolve it into a more production-oriented data platform.

### Phase 1 — Current

```text
✅ CSV ingestion
✅ Data exploration
✅ Data cleaning
✅ Data validation
✅ BigQuery integration
✅ SQL analytics
✅ Pipeline orchestration
```

### Phase 2 — Visualization

```text
⬜ Looker Studio Dashboard
⬜ KPI Dashboard
⬜ Regional Visualizations
⬜ Category Analysis
⬜ Monthly Trends
⬜ Discount vs Profit Dashboard
```

### Phase 3 — Cloud-Native Ingestion

```text
⬜ Google Cloud Storage
⬜ Raw Data Landing Zone
⬜ Cloud-based ingestion
```

### Phase 4 — Orchestration

```text
⬜ Managed workflow orchestration
⬜ Scheduled execution
⬜ Pipeline triggers
```

### Phase 5 — Production Engineering

```text
⬜ Automated testing
⬜ Logging
⬜ Monitoring
⬜ Error handling
⬜ Data quality alerts
⬜ CI/CD
```

---

# 🏭 Future Production Architecture

The long-term architecture can evolve toward:

```text
                  ┌─────────────────┐
                  │   Data Source   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Cloud Storage   │
                  │   Raw Zone      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Data Processing │
                  │   & Cleaning    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Data Quality    │
                  │   Validation    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    BigQuery     │
                  │  Data Warehouse │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   SQL / BI      │
                  │    Analytics    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Dashboards &    │
                  │ Business Users  │
                  └─────────────────┘
```

---

# 📚 Learning Outcomes

By building this project, the following skills are demonstrated:

### Python

```text
Pandas
File Handling
Functions
Modules
Exception Handling
Pipeline Orchestration
```

### SQL

```text
SELECT
WHERE
GROUP BY
ORDER BY
Aggregations
Date Functions
Business Analytics
```

### Data Engineering

```text
ETL
Data Cleaning
Data Validation
Schema Design
Data Warehouse
Data Quality
Pipeline Design
```

### Cloud

```text
Google Cloud
BigQuery
Cloud Authentication
Cloud Data Warehousing
```

### Software Engineering

```text
Modular Architecture
Version Control
Project Structure
Documentation
Reproducibility
Error Handling
```

---

# 👨‍💻 Author

## Aditya Raj

**Software Engineering · Data Engineering · AI/ML**

B.Tech — Electronics & Communication Engineering

### Interests

```text
Software Engineering
Data Engineering
Cloud Computing
AI / ML
Data Science
System Design
```

---

# ⭐ Why This Project?

This project goes beyond simply uploading a CSV file to BigQuery.

It demonstrates the complete engineering lifecycle:

```text
             RAW DATA
                │
                ▼
          UNDERSTAND DATA
                │
                ▼
          CLEAN THE DATA
                │
                ▼
         VALIDATE THE DATA
                │
                ▼
          LOAD TO CLOUD
                │
                ▼
          QUERY WITH SQL
                │
                ▼
        GENERATE INSIGHTS
```

The emphasis is on **data reliability, modularity, reproducibility, and cloud integration**.

---

# 📌 Project Status

<p align="center">

### 🟢 Core Pipeline Completed

</p>

```text
████████████████████████████████████████  Core Pipeline

████████████████████████████████████████  Data Quality

████████████████████████████████████████  BigQuery

████████████████████████████████████████  SQL Analytics

████████████████████████████████████████  Documentation

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Dashboard

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Cloud Storage

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Monitoring

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  CI/CD
```

---

# 📄 License

This project is created for **educational, learning, and portfolio purposes**.

---

<p align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with Python 🐍 · SQL 🗄️ · BigQuery ☁️ · Curiosity 🚀**

</p>
