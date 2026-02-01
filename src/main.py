import pandas as pd
from quality_checks import check_missing, check_duplicates, detect_outliers
from schema_check import check_schema

df = pd.read_csv(r"C:\Users\thobi\Downloads/simulated_sales.csv", parse_dates=["transaction_date"])

report = []

# Missing values
missing = check_missing(df)
report.append(f"Missing Values:\n{missing}\n")

# Duplicates
duplicates = check_duplicates(df)
report.append(f"Duplicate Rows: {duplicates}\n")

# Outliers
outliers = detect_outliers(df, "sale_amount")
report.append(f"Outliers Detected: {len(outliers)}\n")

# Schema
schema_issues = check_schema(df)
if schema_issues:
    report.append("Schema Issues:\n" + "\n".join(schema_issues))
else:
    report.append("Schema Check: PASSED")

# Alert logic
if duplicates > 0 or missing.sum() > 0:
    report.append("\n ALERT: Data quality threshold breached!")

with open("reports/data_quality_report.txt", "w") as f:
    f.write("\n".join(report))
