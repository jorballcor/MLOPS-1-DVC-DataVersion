import pandas as pd
import os

os.makedirs("data", exist_ok=True)

"""df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
})
"""

#df.to_csv("data/people.csv", index=False)
#print("✅ CSV saved in 'data/people.csv'")


"""df = pd.read_csv("data/people.csv")
new_row = {"name": "David", "age": 40}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


df.to_csv("data/people.csv", index=False)


print("✅ Added new row to CSV")
"""

df = pd.read_csv("data/people.csv")
new_row = {"name": "Emma", "age": 28}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


df.to_csv("data/people.csv", index=False)
print("✅ Added new row to CSV")