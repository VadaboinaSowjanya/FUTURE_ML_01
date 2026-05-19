import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Page Title
st.title("📈 Sales & Demand Forecasting Dashboard")

st.write("Interactive Machine Learning Dashboard for Sales Forecasting")

# Load Dataset
df = pd.read_csv("data/sales_data_sample.csv", encoding='latin1')

# Convert Date
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Dataset Preview
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Sales Trend
sales_by_date = df.groupby('ORDERDATE')['SALES'].sum()

st.subheader("📉 Sales Trend Over Time")

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(sales_by_date)
ax.set_xlabel("Order Date")
ax.set_ylabel("Sales")
ax.set_title("Sales Trend Over Time")

st.pyplot(fig)

# Feature Selection
X = df[['QUANTITYORDERED', 'PRICEEACH']]
y = df['SALES']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Show Metrics
st.subheader("📌 Model Performance")

st.write(f"✅ Mean Absolute Error: {mae:.2f}")
st.write(f"✅ R2 Score: {r2:.4f}")

# Actual vs Predicted
st.subheader("📈 Actual vs Predicted Sales")

fig2, ax2 = plt.subplots(figsize=(12,5))

ax2.plot(y_test.values[:50], label='Actual Sales')
ax2.plot(predictions[:50], label='Predicted Sales')

ax2.legend()

st.pyplot(fig2)

# Business Insights
st.subheader("💡 Business Insights")

st.write("""
- Sales show fluctuations over time.
- The model can help businesses estimate future sales.
- Businesses can use forecasts for inventory and staffing decisions.
- Visualization helps stakeholders understand trends clearly.
""")