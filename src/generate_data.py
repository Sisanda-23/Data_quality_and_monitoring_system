import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = {
    "transaction_id": np.arange(1, n + 1),
    "customer_id": np.random.randint(1000, 1100, size=n),
    "sale_amount": np.random.normal(200, 50, size=n),
    "transaction_date": pd.date_range("2025-01-01", periods=n, freq="D"),
}

df = pd.DataFrame(data)

# Introduce missing values
df.loc[np.random.choice(df.index, 20), "sale_amount"] = np.nan

# Introduce duplicates
duplicates = df.sample(5)
df = pd.concat([df, duplicates], ignore_index=True)

# Introduce outliers
df.loc[np.random.choice(df.index, 5), "sale_amount"] = 5000

df.to_csv(r"C:\Users\thobi\Downloads/simulated_sales.csv", index=False)

