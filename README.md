# Sales & Demand Forecasting for Businesses

## 📌 Project Overview
This project is developed as part of the Future Interns Machine Learning Internship Task 1.

The objective of this project is to predict future sales using historical business sales data and Machine Learning techniques. The project demonstrates how forecasting can help bus                                                                                inesses make better decisions related to inventory management, staffing, and financial planning.

---

## 🎯 Objectives
- Analyze historical sales data
- Perform data cleaning and preprocessing
- Create time-based features for forecasting
- Visualize sales trends
- Build a Machine Learning forecasting model
- Evaluate model performance
- Generate business-friendly insights

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

FUTURE_ML_01/
│
├── data/
├── notebook/
├── screenshots/
├── README.md
├── requirements.txt


---

## 📊 Exploratory Data Analysis
The dataset was analyzed to understand:
- sales trends over time
- missing values
- date patterns
- seasonal behavior

Visualizations were created to better understand sales performance.

---

## ⚙️ Feature Engineering
The following time-based features were extracted from the order date:
- Year
- Month
- Day

These features helped the Machine Learning model learn sales patterns more effectively.

---

## 🤖 Machine Learning Model
Model Used:
- Linear Regression

The model was trained using:
- Year
- Month
- Day
- Quantity Ordered
- Price Each

Target Variable:
- Sales

---

## 📈 Model Evaluation
Evaluation metrics used:
- Mean Absolute Error (MAE)
- R² Score

The model achieved good prediction performance for a beginner-level forecasting system.

---

## 💡 Business Insights
This forecasting system can help businesses:
- predict future demand
- manage inventory efficiently
- reduce overstocking
- improve financial planning
- support better business decisions

The sales trend analysis also revealed fluctuations and seasonal-like patterns in customer purchasing behavior.

---

## 📷 Screenshots
Project screenshots and outputs are included inside the `screenshots` folder.

---

## 🌐 Interactive Dashboard

An interactive Streamlit dashboard (`app.py`) is included in this project for visualizing sales trends and forecasting results.

To run locally:

```bash
streamlit run app.py

---

## 🚀 Future Improvements
- Use advanced forecasting models
- Add seasonal decomposition
- Build interactive dashboards using Power BI or Tableau
- Deploy as a web application

---

## 👩‍💻 Author
Sowjanya Vadaboina

---

## 🔗 Internship
Future Interns — Machine Learning Internship Task 1