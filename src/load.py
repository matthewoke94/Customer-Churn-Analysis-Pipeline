import pandas as pd
from src.database import engine

df = pd.read_csv("data/clean_churn.csv")

df.to_sql(
    "customer_churn",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded Successfully")