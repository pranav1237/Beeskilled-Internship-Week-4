# Power BI Dashboard Build Guide

1. Open Power BI Desktop → Get Data → Text/CSV → select `retail_sales_cleaned.csv`.
2. Confirm `Order_Date` is Date, `Sales` and `Profit` are Decimal Number, `Quantity` is Whole Number, and `Discount` is Decimal Number.
3. Create a date table (Modeling → New table):
   `Date = CALENDAR(MIN(SalesData[Order_Date]), MAX(SalesData[Order_Date]))`
   Mark it as the date table and relate `Date[Date]` to `SalesData[Order_Date]`.
4. Add measures from `PowerBI_Measures.dax` (adjust the table name if you rename it).
5. Suggested one-page report:
   - KPI cards: Total Sales, Total Profit, Total Orders, Average Order Value, Profit Margin.
   - Line chart: Date[Date] by month on axis; Total Sales as value.
   - Clustered bar: Category by Total Sales and Total Profit.
   - Bar: Region by Total Sales.
   - Donut: Segment by Total Sales.
   - Scatter: Discount vs Profit, size by Sales, legend by Category.
   - Slicers: Date, Region, Category, Segment, Channel.
6. Add a title and a short text insight panel. Use consistent currency formatting and sort month labels chronologically.
7. Save as `Week4_Retail_Sales_Dashboard.pbix`.

**Important:** A native `.pbix` file must be created and saved in Power BI Desktop. This environment cannot author or validate a Power BI binary file; the cleaned data, measures and build instructions are provided for completing that final application-specific step.
