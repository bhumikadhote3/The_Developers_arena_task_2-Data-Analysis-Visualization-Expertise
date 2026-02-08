# step4_feature_engineering.py

import pandas as pd

# Load datasets
house_df = pd.read_csv("data/house_prices.csv")
supermarket_df = pd.read_csv("data/supermarket_sales.csv")

# --- House insights ---
house_insights = {
    "Avg_Price": house_df['Price'].mean(),
    "Median_Price": house_df['Price'].median(),
    "Max_Price": house_df['Price'].max(),
    "Min_Price": house_df['Price'].min(),
    "Avg_Price_per_Sqft": (house_df['Price'] / house_df['Area']).mean(),
    "Location_with_highest_avg_price": house_df.groupby('Location')['Price'].mean().idxmax(),
    "Property_Type_with_highest_avg_price": house_df.groupby('Property_Type')['Price'].mean().idxmax()
}
house_insights_df = pd.DataFrame([house_insights])

# --- Supermarket insights ---
supermarket_insights = {
    "Total_Sales": supermarket_df['Total'].sum(),
    "Avg_Sales_per_Transaction": supermarket_df['Total'].mean(),
    "City_with_highest_sales": supermarket_df.groupby('City')['Total'].sum().idxmax(),
    "Most_popular_Product_Line": supermarket_df['Product_Line'].mode()[0],
    "Payment_mode_most_used": supermarket_df['Payment'].mode()[0]
}
supermarket_insights_df = pd.DataFrame([supermarket_insights])

# Save insights to CSV (optional)
house_insights_df.to_csv("data/house_insights.csv", index=False)
supermarket_insights_df.to_csv("data/supermarket_insights.csv", index=False)

print("✅ Step 4: Insights extracted")
