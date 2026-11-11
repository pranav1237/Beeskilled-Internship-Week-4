# Stakeholder Summary

The analysis covers **1,499 cleaned transactions** from a reproducible sample retail dataset spanning 2024-01-01 to 2025-12-30. The data is synthetic and is intended to demonstrate the end-to-end analytics workflow; it is not a record of an actual company.

- **Revenue:** total sales were 979,663.40, with total profit of 331,725.50 and an overall profit margin of 33.9%.
- **Order value:** average sales per order were 653.54.
- **Category:** Technology generated the highest sales (522,266.63). Technology had the lowest category-level profit margin (33.4%), indicating that revenue alone should not drive assortment decisions.
- **Region:** West led revenue (284,159.01); West generated the highest profit (99,394.76). Review both revenue and margin when allocating sales resources.
- **Monthly performance:** the strongest month was 2024-08, with sales of 56,459.54.
- **Prediction:** the Random Forest regression model achieved MAE 54.38, RMSE 187.25, and R² 0.977 on a held-out 20% test set.

## Recommendations
1. Protect profitable category and region combinations; evaluate profit margin alongside sales before increasing promotion or inventory.
2. Investigate discount-heavy transactions and monitor whether discounts increase volume enough to offset margin erosion.
3. Review monthly trends for seasonality and plan inventory and staffing ahead of stronger periods.
4. Use the regression model as a planning aid, not an automated pricing or financial decision system. Validate on fresh, real transaction data before operational use.
5. Replace the sample data with the official assignment Google Sheet before presenting the findings as business facts.

## Limitations
The dataset is synthetic, so the numerical insights are illustrative only. Sales is mathematically determined by quantity, unit price and discount in the generated data, which makes the prediction task demonstrative rather than a proof of real-world forecasting ability. A time-based validation split and external drivers (campaigns, stock availability, seasonality) should be considered with genuine data.
