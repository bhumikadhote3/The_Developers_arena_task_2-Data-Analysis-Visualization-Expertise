# step2_house_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load house dataset
house_df = pd.read_csv("data/house_prices.csv")

# 1️⃣ House Price Distribution
plt.figure(figsize=(8,6))
sns.histplot(house_df['Price'], bins=20, kde=True)
plt.title("House Price Distribution")
plt.savefig("house_price_distribution.png")
plt.close()

# 2️⃣ Price vs Area by Property Type
plt.figure(figsize=(8,6))
sns.scatterplot(data=house_df, x='Area', y='Price', hue='Property_Type')
plt.title("Price vs Area by Property Type")
plt.savefig("price_vs_area_property_type.png")
plt.close()

# 3️⃣ Price Distribution by Bedrooms
plt.figure(figsize=(8,6))
sns.boxplot(data=house_df, x='Bedrooms', y='Price')
plt.title("Price Distribution by Number of Bedrooms")
plt.savefig("price_by_bedrooms.png")
plt.close()

# 4️⃣ Price Distribution by Location
plt.figure(figsize=(8,6))
sns.boxplot(data=house_df, x='Location', y='Price')
plt.title("Price Distribution by Location")
plt.savefig("price_by_location.png")
plt.close()

print("✅ Step 2: House analysis plots saved")
