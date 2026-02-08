# run_full_project.py
# ==========================================
# Complete pipeline: Load data, analyze, visualize, create Excel & PDF reports
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# -----------------------------
# 1️⃣ Setup folders
# -----------------------------
project_folder = os.getcwd()  # current folder
data_folder = os.path.join(project_folder, "data")
report_folder = os.path.join(project_folder, "Project_Report")
os.makedirs(report_folder, exist_ok=True)

# -----------------------------
# 2️⃣ Load datasets
# -----------------------------
house_df = pd.read_csv(os.path.join(data_folder, "house_prices.csv"))
supermarket_df = pd.read_csv(os.path.join(data_folder, "supermarket_sales.csv"))

# -----------------------------
# 3️⃣ House Dataset Analysis
# -----------------------------
# Price distribution
plt.figure(figsize=(8,5))
sns.histplot(house_df['Price'], bins=20, kde=True, color='skyblue')
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.savefig(os.path.join(report_folder, "house_price_distribution.png"))
plt.close()

# Price vs Area by Property Type
plt.figure(figsize=(8,5))
sns.scatterplot(data=house_df, x='Area', y='Price', hue='Property_Type')
plt.title("Price vs Area by Property Type")
plt.savefig(os.path.join(report_folder, "price_vs_area_property_type.png"))
plt.close()

# Price by Number of Bedrooms
plt.figure(figsize=(8,5))
sns.boxplot(data=house_df, x='Bedrooms', y='Price')
plt.title("Price Distribution by Number of Bedrooms")
plt.savefig(os.path.join(report_folder, "price_by_bedrooms.png"))
plt.close()

# Price by Location
plt.figure(figsize=(8,5))
sns.boxplot(data=house_df, x='Location', y='Price')
plt.title("Price Distribution by Location")
plt.savefig(os.path.join(report_folder, "price_by_location.png"))
plt.close()

# House insights
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

# -----------------------------
# 4️⃣ Supermarket Dataset Analysis
# -----------------------------
# Total sales distribution
plt.figure(figsize=(8,5))
sns.histplot(supermarket_df['Total'], bins=20, kde=True, color='orange')
plt.title("Distribution of Total Sales")
plt.xlabel("Total")
plt.ylabel("Count")
plt.savefig(os.path.join(report_folder, "supermarket_total_sales_distribution.png"))
plt.close()

# Total sales by City
plt.figure(figsize=(8,5))
sns.barplot(x='City', y='Total', data=supermarket_df.groupby('City')['Total'].sum().reset_index())
plt.title("Total Sales by City")
plt.savefig(os.path.join(report_folder, "total_sales_by_city.png"))
plt.close()

# Number of transactions by Payment Mode
plt.figure(figsize=(8,5))
sns.countplot(x='Payment', data=supermarket_df)
plt.title("Number of Transactions by Payment Mode")
plt.savefig(os.path.join(report_folder, "transactions_by_payment_mode.png"))
plt.close()

# Supermarket insights
supermarket_insights = {
    "Total_Sales": supermarket_df['Total'].sum(),
    "Avg_Sales_per_Transaction": supermarket_df['Total'].mean(),
    "City_with_highest_sales": supermarket_df.groupby('City')['Total'].sum().idxmax(),
    "Most_popular_Product_Line": supermarket_df['Product_Line'].mode()[0],
    "Payment_mode_most_used": supermarket_df['Payment'].mode()[0]
}
supermarket_insights_df = pd.DataFrame([supermarket_insights])

# -----------------------------
# 5️⃣ Generate Excel report
# -----------------------------
excel_file = os.path.join(report_folder, "Final_Report.xlsx")
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    house_insights_df.to_excel(writer, sheet_name="House_Insights", index=False)
    supermarket_insights_df.to_excel(writer, sheet_name="Supermarket_Insights", index=False)

print("✅ Excel report created:", excel_file)

# -----------------------------
# 6️⃣ Generate PDF report
# -----------------------------
pdf_file = os.path.join(report_folder, "Complete_Report.pdf")
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# House Insights
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "House Dataset Insights", ln=True)
pdf.set_font("Arial", '', 12)
for col in house_insights_df.columns:
    pdf.cell(0, 8, f"{col}: {house_insights_df[col][0]}", ln=True)
pdf.ln(5)

# Add House Plots
house_plots = ["house_price_distribution.png", "price_vs_area_property_type.png",
               "price_by_bedrooms.png", "price_by_location.png"]
for plot in house_plots:
    pdf.add_page()
    pdf.image(os.path.join(report_folder, plot), x=15, w=180)
    pdf.ln(5)

# Supermarket Insights
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Supermarket Dataset Insights", ln=True)
pdf.set_font("Arial", '', 12)
for col in supermarket_insights_df.columns:
    pdf.cell(0, 8, f"{col}: {supermarket_insights_df[col][0]}", ln=True)
pdf.ln(5)

# Add Supermarket Plots
supermarket_plots = ["supermarket_total_sales_distribution.png", "total_sales_by_city.png",
                     "transactions_by_payment_mode.png"]
for plot in supermarket_plots:
    pdf.add_page()
    pdf.image(os.path.join(report_folder, plot), x=15, w=180)
    pdf.ln(5)

pdf.output(pdf_file)
print("✅ Complete PDF report created:", pdf_file)

# -----------------------------
# 7️⃣ Finished
# -----------------------------
print("🎯 Project completed successfully!")
