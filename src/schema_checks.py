EXPECTED_SCHEMA = {
    "transaction_id": "int64",
    "customer_id": "int64",
    "sale_amount": "float64",
    "transaction_date": "datetime64[ns]"
}

def check_schema(df):
    issues = []
    for col, dtype in EXPECTED_SCHEMA.items():
        if col not in df.columns:
            issues.append(f"Missing column: {col}")
        elif str(df[col].dtype) != dtype:
            issues.append(f"Column {col} expected {dtype}, got {df[col].dtype}")
    return issues

