# Customer Churn Prediction System

An end-to-end machine learning application for predicting customer churn and supporting retention decisions.

## Project Overview
This project predicts whether a customer is likely to churn based on telecom customer data.  
It includes:
- A trained machine learning model
- A FastAPI backend for prediction
- A Streamlit frontend for user interaction
- Risk level and recommendation output

## Features
- Customer churn prediction
- Probability score
- Risk level classification
- Retention recommendation
- Simple rule-based risk factors

## Technologies Used
- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

## Project Structure
```bash
customer-churn-system/
│
├── api/
│   └── main.py
├── app/
│   └── streamlit_app.py
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── models/
│   └── churn_model.pkl
├── notebooks/
│   └── churn_eda.ipynb
├── requirements.txt
└── README.md