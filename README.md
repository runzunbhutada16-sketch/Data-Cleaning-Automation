#  Data Cleaning Automation and Data Quality Management System

A professional intermediate-to-advanced Python project that automates data cleaning, preprocessing, and data quality assessment for datasets from multiple file formats.

This project focuses on **Data Cleaning**, **Data Quality Management**, **Data Preprocessing**, **Exploratory Data Analysis (EDA)**, and **Business Intelligence** concepts using Python.

---

##  Project Overview

The **Data Cleaning Automation and Data Quality Management System** is designed to:

* Automatically clean raw datasets.
* Handle missing values and duplicate records.
* Detect and remove outliers.
* Standardize date and text columns.
* Assess overall data quality.
* Generate professional reports and visualizations.
* Export cleaned datasets for further analysis.

---

#  Objectives

* Automate repetitive data cleaning tasks.
* Improve data quality and consistency.
* Support multiple file formats (CSV, Excel, JSON).
* Generate insights about dataset quality.
* Provide reusable, production-style Python code.

---

# Project Structure

```text
data-cleaning-automation/
│
├── data_cleaner.py
│
├── datasets/
│   ├── raw_data.csv
│   ├── raw_data.xlsx
│   └── raw_data.json
│
├── cleaned_data/
│   └── cleaned_dataset.csv
│
├── reports/
│   ├── missing_value_report.csv
│   ├── duplicate_report.csv
│   ├── outlier_report.csv
│   └── data_quality_report.csv
│
├── visualizations/
│
├── requirements.txt
└── README.md
```

---

#  Features

##  Data Loading

Supports:

* CSV files
* Excel files (.xlsx)
* JSON files

---

## Automated Data Cleaning

The system automatically handles:

### Missing Values

* Mean Imputation
* Median Imputation
* Mode Imputation
* Forward Fill
* Backward Fill

### Duplicate Records

* Detect duplicates
* Remove duplicate rows
* Generate duplicate reports

### Date Processing

* Automatically detect date columns
* Convert invalid dates
* Standardize date formats

### Text Cleaning

* Remove extra spaces
* Convert text to lowercase/uppercase/title case
* Remove special characters
* Standardize categorical values

---

##  Outlier Detection

The system supports:

* IQR (Interquartile Range) Method
* Z-Score Method
* Outlier Removal Summary
* Winsorization

---

#  Data Quality Assessment

Calculate and analyze:

### Dataset Metrics

* Total Records
* Total Columns
* Missing Value Percentage
* Duplicate Record Percentage
* Null Value Distribution
* Unique Values Count
* Data Type Distribution
* Memory Usage
* Dataset Completeness Score

### Data Quality Metrics

* Accuracy Score
* Consistency Score
* Completeness Score
* Validity Score
* Overall Data Quality Index

---

#  Visualizations

Generate professional visualizations using:

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Missing Value Visualizations

* Heatmap of Missing Values
* Missing Percentage Chart
* Missing Value Bar Chart

### Outlier Visualizations

* Boxplots
* Histograms
* Scatter Plots

### Data Quality Visualizations

* Dataset Completeness Chart
* Data Type Distribution Pie Chart
* Quality Score Dashboard

### Cleaning Summary

* Before vs After Cleaning Comparison
* Records Removed Analysis
* Data Quality Improvement Chart

---

# Terminal Dashboard

The project includes an interactive menu:

```text
====================================================
 DATA CLEANING AUTOMATION SYSTEM
====================================================

1. Load Dataset
2. View Dataset Summary
3. Analyze Missing Values
4. Analyze Duplicates
5. Detect Outliers
6. Clean Dataset Automatically
7. View Data Quality Report
8. Generate Visualizations
9. Export Cleaned Dataset
10. Export Reports
11. Exit
```

---

#  Sample Dataset

Example:

| Name  | Age | City   | JoinDate     | Salary |
| ----- | --- | ------ | ------------ | -----: |
| John  | 25  | Mumbai | 2024-01-10   |  50000 |
| Alice | NaN | Delhi  | 2024-02-15   |  60000 |
| Bob   | 30  | Mumbai | invalid_date |  55000 |
| Emma  | 28  | Pune   | 2024-03-20   |    NaN |

---

#  Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/data-cleaning-automation.git

cd data-cleaning-automation
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python data_cleaner.py
```

---

#  Example Output

```text
============================================================
 DATA CLEANING AUTOMATION SYSTEM
============================================================

 Loaded 1000 records
 Total Columns: 8

 DATASET SUMMARY

+----------------------+-------+
| Metric               | Value |
+----------------------+-------+
| Total Records        | 1000  |
| Total Columns        | 8     |
| Missing Values       | 25    |
| Duplicate Records    | 10    |
| Memory Usage (MB)    | 0.45  |
+----------------------+-------+

 Handling Missing Values...

 Missing Before: 25
 Missing After : 0

 Removed 10 duplicate records

 Cleaning Date Columns...
 Standardized JoinDate

 Cleaning Text Columns...
 Cleaned 3 text columns

 Cleaned Dataset Saved:
 cleaned_data/cleaned_dataset.csv

 Cleaning Completed Successfully
```

---

# Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* OpenPyXL
* Tabulate
* Regular Expressions (re)

---

#  Future Enhancements

* Streamlit Web Dashboard
* Real-Time Data Cleaning Pipeline
* Data Validation Rules Engine
* Automated EDA Report Generation
* Integration with SQL Databases
* Machine Learning-based Anomaly Detection

---
AUTHOR: RUNZUN M.BHUTADA
INTERN-ID: CITS2504
