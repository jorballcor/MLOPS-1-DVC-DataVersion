import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
})

df.to_csv("data/people.csv", index=False)
print("✅ CSV saved in 'data/people.csv'")
