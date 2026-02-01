# Automated Data Quality Monitoring System

## Problem
Business decisions are often based on incomplete or inconsistent data.

## Solution
This project simulates a business sales dataset and implements an automated
data quality monitoring pipeline that checks:

- Missing values
- Duplicate records
- Outliers
- Schema changes

## Tech Stack
- Python (pandas, numpy)
- SQL
- Basic automation

## How to Run
1. Generate data:
   python src/generate_data.py
2. Run quality checks:
   python src/main.py

## Output
- Data quality report
- Alerts for threshold breaches
