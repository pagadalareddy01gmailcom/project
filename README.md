# 📊 Olist Brazilian E-Commerce Sales Analysis & Sales Prediction using Power BI & Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![License](https://img.shields.io/badge/License-MIT-green)

A complete **Data Analytics and Machine Learning** project built using the **Olist Brazilian E-Commerce Public Dataset**. This project combines **data preprocessing, business intelligence, exploratory data analysis, and machine learning** to generate actionable business insights and predict future sales.

---

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Project Objectives](#-project-objectives)
- [Dataset](#-dataset)
- [Project Workflow](#-project-workflow)
- [Project Structure](#-project-structure)
- [Data Cleaning & Preprocessing](#-data-cleaning--preprocessing)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Machine Learning](#-machine-learning)
- [Model Evaluation](#-model-evaluation)
- [Business Insights](#-business-insights)
- [Technologies Used](#-technologies-used)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)
- [Limitations](#-limitations)
- [Author](#-author)

---

# 🚀 Project Overview

This project presents an end-to-end **Business Intelligence** and **Machine Learning** solution using the **Olist Brazilian E-Commerce Public Dataset**.

The project demonstrates how raw e-commerce transaction data can be transformed into meaningful business insights through:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Interactive Power BI Dashboard
- Machine Learning Sales Prediction

The primary objective is to help businesses understand customer purchasing behavior, monitor sales performance, identify profitable regions and products, and accurately predict future sales.

---

# 🎯 Business Problem

Modern e-commerce companies generate millions of transactions every year.

Without effective analytics, businesses struggle to answer important questions such as:

- Which products generate the highest revenue?
- Which regions perform best?
- Which customers purchase most frequently?
- How do sales change over time?
- Can future sales be predicted accurately?

This project answers these questions using **Business Intelligence** and **Machine Learning** techniques.

---

# 🎯 Project Objectives

The objectives of this project are:

- Clean and preprocess raw e-commerce data
- Perform Exploratory Data Analysis (EDA)
- Build an interactive Power BI dashboard
- Analyze customer purchasing behavior
- Identify sales trends and regional performance
- Train multiple Machine Learning regression models
- Compare model performance
- Predict future sales

---

# 📂 Dataset

## Dataset Used

**Olist Brazilian E-Commerce Public Dataset**

The dataset contains information about:

- Customers
- Orders
- Products
- Sellers
- Payments
- Customer Reviews
- Delivery Information
- Geolocation

This publicly available dataset contains over **100,000 Brazilian e-commerce orders** and is widely used for data analytics and machine learning projects.

---

# ⚙️ Project Workflow

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
Model Evaluation
      │
      ▼
Business Insights
```

---

# 📁 Project Structure

```
Olist-Sales-Analysis
│
├── data
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
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🧹 Data Cleaning & Preprocessing

Several preprocessing techniques were applied before analysis:

- Removed duplicate records
- Handled missing values
- Converted data types
- Cleaned inconsistent data
- Feature engineering
- Formatted date columns
- Removed unnecessary columns
- Exported cleaned dataset

The final processed dataset was saved as:

```
final_cleaned_dataset.csv
```

---

# 📊 Power BI Dashboard

The Power BI dashboard provides interactive business insights through dynamic visualizations and KPIs.

### Dashboard Features

- 💰 Total Revenue
- 📦 Total Orders
- 👥 Customer Analysis
- 🛍 Product Category Performance
- 📈 Monthly Revenue Trends
- 🌎 Regional Sales Distribution
- 💳 Payment Analysis
- 🚚 Delivery Performance
- 📌 KPI Cards
- 🎛 Interactive Filters & Slicers

The dashboard allows users to filter sales by customer, region, payment method, product category, and purchase date.

---

# 📸 Dashboard Preview

## Executive Dashboard

```
images/dashboard1.png
```

## Sales Dashboard

```
images/dashboard2.png
```

> Replace the placeholders above with actual screenshots from your Power BI dashboard.

---

# 🤖 Machine Learning

To predict future sales, multiple regression algorithms were trained and compared.

### Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

The objective was to determine the most accurate model for predicting sales using historical transaction data.

---

# 📈 Model Evaluation

Each regression model was evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Example comparison:

| Model | MAE | RMSE | R² Score |
|-------|------|------|----------|
| Linear Regression | XX | XX | XX |
| Decision Tree | XX | XX | XX |
| Random Forest | XX | XX | XX |
| XGBoost | XX | XX | **Best** |

> Replace **XX** with your actual model results.

---

# 💡 Business Insights

The analysis generated several valuable business insights:

- Sales vary significantly across different Brazilian states.
- Certain product categories generate considerably higher revenue.
- Credit Card is the most frequently used payment method.
- Monthly sales exhibit seasonal trends.
- A small percentage of customers contribute a large portion of total revenue.
- Machine Learning models can effectively estimate future sales using historical transaction data.

---

# 🛠 Technologies Used

## Programming Language

- Python

## Python Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Jupyter Notebook

## Business Intelligence

- Microsoft Power BI

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/olist-sales-analysis.git
```

## Navigate to the Project

```bash
cd olist-sales-analysis
```

## Install Required Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib
```

## Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
model_training.ipynb
```

---

# 🚀 Future Improvements

Potential enhancements for this project include:

- Deploy the model using Streamlit
- Time Series Sales Forecasting
- Customer Segmentation using Clustering
- Recommendation System
- Deep Learning Models
- Real-time Dashboard Integration

---

# ⚠️ Limitations

- The dataset represents one Brazilian marketplace only.
- Predictions are based on historical transaction data.
- External economic and seasonal factors were not included.
- Model performance depends on data quality and feature selection.

---

# 📄 License

This project is developed for **educational** and **portfolio** purposes.

You may use it for learning and research.

---

# 👤 Author

**Tulasiram Reddy Pagadala**

Master's in Data Science & Business Development

EDC Paris Business School

### GitHub

https://github.com/yourusername

### LinkedIn

https://linkedin.com/in/yourprofile

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback and suggestions are always welcome.
