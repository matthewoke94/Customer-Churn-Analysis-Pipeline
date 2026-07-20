import pandas as pd

df = pd.read_csv("data/raw_churn.csv")

# Remove duplicates
df = df.drop_duplicates()

# Round numeric columns
df["monthly_charges"] = df["monthly_charges"].round(2)
df["total_charges"] = df["total_charges"].round(2)

# Save cleaned data
df.to_csv("data/clean_churn.csv", index=False)

print("Data transformed successfully!")