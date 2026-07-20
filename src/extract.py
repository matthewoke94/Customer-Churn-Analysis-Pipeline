from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

rows = []

for i in range(500):
    rows.append({
        "customer_id": f"CUST{i+1:05}",
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "tenure": random.randint(1, 72),
        "monthly_charges": round(random.uniform(20, 120), 2),
        "total_charges": round(random.uniform(200, 9000), 2),
        "contract": random.choice(["Month-to-month","One year","Two year"]),
        "payment_method": random.choice([
            "Credit Card",
            "Bank Transfer",
            "Electronic Check"
        ]),
        "internet_service": random.choice([
            "Fiber Optic",
            "DSL",
            "None"
        ]),
        "churn": random.choice(["Yes","No"])
    })

os.makedirs("data", exist_ok=True)

pd.DataFrame(rows).to_csv("data/raw_churn.csv", index=False)

print("500 Customer Records Generated")