# step5_generate_excel_pdf.py

import os
import pandas as pd
from fpdf import FPDF

report_folder = "data"
pdf_file = "Project_Report_Complete.pdf"

# Load insights
house_insights_df = pd.read_csv(os.path.join(report_folder, "house_insights.csv"))
supermarket_insights_df = pd.read_csv(os.path.join(report_folder, "supermarket_insights.csv"))

# --- Create Excel Report ---
with pd.ExcelWriter(os.path.join(report_folder, "Final_Report.xlsx")) as writer:
    house_insights_df.to_excel(writer, sheet_name="House_Insights", index=False)
    supermarket_insights_df.to_excel(writer, sheet_name="Supermarket_Insights", index=False)
print("✅ Excel report created: Final_Report.xlsx")

# --- Create PDF ---
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

# Add House plots
house_plots = [
    "house_price_distribution.png",
    "price_vs_area_property_type.png",
    "price_by_bedrooms.png",
    "price_by_location.png"
]
for plot in house_plots:
    pdf.add_page()
    pdf.image(plot, x=15, w=180)
    pdf.ln(5)

# Supermarket Insights
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Supermarket Dataset Insights", ln=True)
pdf.set_font("Arial", '', 12)
for col in supermarket_insights_df.columns:
    pdf.cell(0, 8, f"{col}: {supermarket_insights_df[col][0]}", ln=True)
pdf.ln(5)

# Add Supermarket plots
supermarket_plots = [
    "supermarket_total_sales_distribution.png",
    "total_sales_by_city.png",
    "transactions_by_payment_mode.png"
]
for plot in supermarket_plots:
    pdf.add_page()
    pdf.image(plot, x=15, w=180)
    pdf.ln(5)

# Save PDF
pdf.output(pdf_file)
print("✅ Complete PDF report created:", pdf_file)
