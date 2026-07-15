# 🛒 Olist Brazilian E-Commerce Sales Analysis & Sales Prediction using Power BI & Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![License](https://img.shields.io/badge/License-MIT-red)

A complete end-to-end Data Analytics and Machine Learning project built using the **Olist Brazilian E-Commerce Public Dataset**.

The project combines **Business Intelligence**, **Data Analysis**, and **Machine Learning** to help businesses understand customer purchasing behaviour, identify sales trends, and accurately predict future sales.

---

# 📌 Table of Contents

- Project Overview
- Business Problem
- Objectives
- Dataset Information
- Project Architecture
- Technologies Used
- Data Cleaning
- Exploratory Data Analysis
- Power BI Dashboard
- Machine Learning
- Model Performance
- Business Insights
- Repository Structure
- Installation
- Future Improvements
- Limitations
- Author

---

# 📖 Project Overview

E-commerce businesses generate enormous amounts of transactional data every day.

Without proper analysis, companies struggle to understand:

- Customer buying behaviour
- Sales trends
- Regional performance
- Product demand
- Future revenue

This project demonstrates how Business Intelligence and Machine Learning can transform raw transactional data into meaningful business insights.

The project contains three complete phases:

✔ Data Cleaning

✔ Interactive Dashboard Development

✔ Sales Prediction using Machine Learning

---

# 🎯 Business Problem

Businesses need answers to questions such as:

- Which products generate the highest revenue?
- Which regions have the highest sales?
- Which customers purchase most frequently?
- How do sales change over time?
- Can future sales be predicted accurately?

This project answers these questions using real-world e-commerce data.

---

# 🎯 Project Objectives

The main objectives are:

- Clean and preprocess raw e-commerce data
- Perform Exploratory Data Analysis (EDA)
- Build an interactive Power BI dashboard
- Discover business trends
- Compare multiple Machine Learning models
- Predict future sales
- Generate actionable business insights

---

# 📂 Dataset

## Dataset Name

**Olist Brazilian E-Commerce Public Dataset**

### Source

Kaggle

Dataset includes information about:

- Customers
- Orders
- Sellers
- Products
- Payments
- Reviews
- Delivery
- Geolocation

---

# 📊 Dataset Features

The cleaned dataset contains information such as:

- Customer ID
- Order ID
- Purchase Date
- Product Category
- Price
- Freight Value
- Payment Type
- Seller Information
- Customer State
- Delivery Time

---

# 🏗 Project Architecture

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Power BI Dashboard
      │
      ▼
Machine Learning
      │
      ▼
Sales Prediction
```

---

# 🧹 Data Cleaning

Several preprocessing techniques were applied:

- Removed duplicate records
- Handled missing values
- Converted data types
- Removed unnecessary columns
- Feature engineering
- Date formatting
- Outlier inspection

The cleaned dataset was exported as

```
final_cleaned_dataset.csv
```

---

# 📈 Exploratory Data Analysis (EDA)

EDA was performed to understand:

- Sales distribution
- Monthly revenue trends
- Customer purchasing behaviour
- Product category performance
- Payment preferences
- Regional sales
- Order delivery performance

---

# 📊 Power BI Dashboard

The Power BI dashboard enables users to interactively explore sales data.

## Dashboard Features

- 💰 Total Revenue
- 📦 Total Orders
- 👥 Customer Analysis
- 🌎 Regional Sales
- 📅 Monthly Sales Trend
- 🛍 Product Category Analysis
- 💳 Payment Analysis
- 🚚 Delivery Performance
- KPI Cards
- Interactive Filters
- Drill-down Analysis

---

# 📷 Dashboard Preview

## Executive Dashboard

```
images/dashboard1.png
```

## Sales Analysis Dashboard

```
images/dashboard2.png
```

---

# 🤖 Machine Learning

Four regression algorithms were trained and compared.

### Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

The objective was to predict future sales based on historical transaction data.

---

# 📊 Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was selected based on prediction accuracy.

Example comparison:

| Model | MAE | RMSE | R² Score |
|------|------|------|------|
| Linear Regression | XX | XX | XX |
| Decision Tree | XX | XX | XX |
| Random Forest | XX | XX | XX |
| XGBoost | XX | XX | **Best** |

*(Replace XX with your actual results.)*

---

# 💡 Business Insights

Some important insights obtained from the analysis include:

- Certain product categories contribute significantly more revenue.
- Sales show clear seasonal patterns.
- A small percentage of customers generate a large share of total revenue.
- Some regions consistently outperform others.
- Delivery delays negatively impact customer satisfaction.
- Machine Learning models can effectively estimate future sales trends.

---

# 🛠 Technologies Used

## Programming

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Jupyter Notebook

## Visualization

- Microsoft Power BI

---

# 📁 Repository Structure

```
📦 Olist-Sales-Analysis
│
├── data
│   ├── raw_dataset.csv
│   └── final_cleaned_dataset.csv
│
├── notebooks
│   └── model_training.ipynb
│
├── dashboard
│   └── olist_bi.pbix
│
├── images
│   ├── dashboard1.png
│   └── dashboard2.png
│
├── README.md
│
└── requirements.txt
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/olist-sales-analysis.git
```

Move into the project folder

```bash
cd olist-sales-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

Open

```
model_training.ipynb
```

---

# 🚀 Future Improvements

Possible future enhancements include:

- Deep Learning models
- Time-series forecasting
- Real-time Power BI dashboards
- Customer segmentation using clustering
- Sales recommendation system
- Streamlit web application deployment

---

# ⚠ Limitations

- Dataset represents only one marketplace.
- External economic factors are not included.
- Model accuracy depends on historical data quality.
- Real-world deployment would require continuous model retraining.

---

# 👨‍💻 Author

**Tulasiram Reddy Pagadala**

Master's in Data Science & Business Development

EDC Paris Business School

### Connect with me

GitHub

https://github.com/yourusername

LinkedIn

https://linkedin.com/in/yourprofile

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
