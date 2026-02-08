# step1_load_data.py

import pandas as pd

# Load datasets
house_df = pd.read_csv("data/house_prices.csv")
supermarket_df = pd.read_csv("data/supermarket_sales.csv")

# Show first 5 rows
print("House Dataset:")
print(house_df.head())
print("\nSupermarket Dataset:")
print(supermarket_df.head())

# Save loaded data to CSV (optional)
house_df.to_csv("data/house_df_loaded.csv", index=False)
supermarket_df.to_csv("data/supermarket_df_loaded.csv", index=False)
