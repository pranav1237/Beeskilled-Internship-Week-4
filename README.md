# Week 4 Data Analyst Capstone – Retail Sales

## Important data note
The Google Sheets URL embedded in the supplied assignment PDF was not accessible during preparation. To provide a complete runnable demonstration, this project uses a reproducible **synthetic** retail transaction dataset (seed 42). It is not actual company data. Replace the CSV with the official assignment data and rerun the notebook/script before treating any findings as business facts.

## Files
- `Week4_Capstone_Final_Report.pdf` – formatted final report.
- `Week4_Retail_Sales_Analysis.ipynb` – Jupyter notebook for EDA and regression.
- `analysis.py` – standalone runnable analysis script.
- `retail_sales_raw.csv` – raw sample data with controlled quality issues.
- `retail_sales_cleaned.csv` – cleaned dataset for Power BI.
- `Week4_Retail_Sales_Analysis.xlsx` – raw/cleaned data, summaries, model metrics and charts.
- `PowerBI_Measures.dax`, `PowerBI_Theme.json`, `PowerBI_Dashboard_Guide.md` – Power BI setup assets.
- `Stakeholder_Summary.md` – concise stakeholder findings.

## Run
```bash
pip install pandas numpy scikit-learn matplotlib openpyxl
python analysis.py
```
Open the notebook in Jupyter and run cells top-to-bottom. Keep the CSV in the same directory.

## Power BI
Import `retail_sales_cleaned.csv`, add measures from `PowerBI_Measures.dax`, follow `PowerBI_Dashboard_Guide.md`, and save the native report as `Week4_Retail_Sales_Dashboard.pbix`.

## Metric definitions
- MAE: mean absolute prediction error.
- RMSE: square root of mean squared prediction error.
- R²: proportion of test-target variance explained by the fitted model.
