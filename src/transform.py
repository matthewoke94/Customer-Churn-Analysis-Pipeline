import pandas as pd

df = pd.read_csv("data/raw_churn.csv")

df.drop_duplicates(inplace=True)

df["MonthlyCharges"] = df["MonthlyCharges"].round(2)

df.to_csv("data/clean_churn.csv", index=False)

print("Transformation Complete")