"""
Week 4 Data Analyst Capstone: Retail Sales Analysis
Dataset: reproducible synthetic sample (not actual company data).
Run: pip install pandas numpy scikit-learn matplotlib openpyxl
     python analysis.py
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("retail_sales_raw.csv", parse_dates=["Order_Date"])
print("Raw shape:", df.shape)
print("Missing values:\\n", df.isna().sum())
print("Duplicate Order_IDs:", df.duplicated("Order_ID").sum())

df = df.drop_duplicates(subset=["Order_ID"]).copy()
df["Region"] = df["Region"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median()).astype(int)
for col in ["Unit_Price", "Discount", "Sales", "Profit"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["Order_Date", "Sales"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Profit_Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], 0)

print("\\nDescriptive statistics:\\n", df[["Quantity","Unit_Price","Discount","Sales","Profit"]].describe())
print("\\nSales by category:\\n", df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\\nSales by region:\\n", df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
print("\\nMonthly trend:\\n", df.groupby("Month")["Sales"].sum())

features = ["Quantity","Unit_Price","Discount","Region","Category","Sub_Category","Segment","Channel"]
X, y = df[features], df["Sales"]
numeric = ["Quantity","Unit_Price","Discount"]
categorical = [c for c in features if c not in numeric]
preprocessor = ColumnTransformer([
    ("numeric","passthrough",numeric),
    ("categorical",OneHotEncoder(handle_unknown="ignore"),categorical)
])
pipeline = Pipeline([
    ("preprocessor",preprocessor),
    ("model",RandomForestRegressor(n_estimators=250,random_state=42,min_samples_leaf=2,n_jobs=-1))
])
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=42)
pipeline.fit(X_train,y_train)
pred = pipeline.predict(X_test)
print("\\nMAE:", mean_absolute_error(y_test,pred))
print("RMSE:", mean_squared_error(y_test,pred)**0.5)
print("R2:", r2_score(y_test,pred))
