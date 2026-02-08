# step3_supermarket_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load supermarket dataset
supermarket_df = pd.read_csv("data/supermarket_sales.csv")

# 1️⃣ Total Sales Distribution
plt.figure(figsize=(8,6))
sns.histplot(supermarket_df['Total'], bins=20, kde=True)
plt.title("Total Sales Distribution")
plt.savefig("supermarket_total_sales_distribution.png")
plt.close()

# 2️⃣ Total Sales by City
plt.figure(figsize=(8,6))
sns.barplot(data=supermarket_df.groupby('City')['Total'].sum().reset_index(), x='City', y='Total')
plt.title("Total Sales by City")
plt.savefig("total_sales_by_city.png")
plt.close()

# 3️⃣ Number of Transactions by Payment Mode
plt.figure(figsize=(8,6))
sns.countplot(data=supermarket_df, x='Payment')
plt.title("Number of Transactions by Payment Mode")
plt.savefig("transactions_by_payment_mode.png")
plt.close()

print("✅ Step 3: Supermarket analysis plots saved")
