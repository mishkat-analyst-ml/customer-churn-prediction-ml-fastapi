# customer-churn-prediction-ml-fastapi

# 🚀 End-to-End Customer Churn Prediction System

# Executive Summary

Subscription-based businesses lose revenue when customers stop using their services. This project develops a complete machine learning solution that identifies customers who are likely to churn before they leave.

The system begins with raw customer data, performs automated preprocessing through a Scikit-Learn Pipeline, trains and optimizes a Random Forest classifier using GridSearchCV, evaluates the model with multiple classification metrics, serializes the trained model using Joblib, and exposes predictions through a FastAPI REST API for real-time inference.

The project demonstrates an end-to-end machine learning workflow suitable for production-oriented applications.


# Business Problem

Customer churn directly impacts profitability because acquiring new customers is significantly more expensive than retaining existing ones.

The objective of this project is to predict customer churn using demographic information, subscription details, spending behavior, and product usage patterns, enabling organizations to take proactive retention actions.

# Dataset Overview

Category	Description

Records	Your dataset rows

Features	Customer profile and subscription information

Target Variable	Churn

Prediction Type	Binary Classification


# Data Quality Assessment

# The dataset was examined before model development to ensure reliable training.

Completed validation included:

Dataset inspection

Data type verification

Missing value analysis

Duplicate record detection

Statistical profiling

Feature distribution analysis

Target balance evaluation

Exploratory Data Analysis

EDA was performed to understand customer behavior and identify meaningful relationships between variables.

# Analysis included

Customer age distribution

Subscription type distribution

Contract length comparison

Customer spending analysis

Usage frequency analysis

Churn class distribution

Spending by subscription category

Usage frequency by contract type

Relationship between age and total spending

Outlier identification

These analyses helped validate data quality and provided insights into customer behavior before model training.

Machine Learning Pipeline

Instead of manually preprocessing the dataset, an automated Scikit-Learn Pipeline was implemented.

# The pipeline performs:

Median imputation for numerical features

Most frequent imputation for categorical features

Standardization of numerical variables

One-Hot Encoding of categorical variables

Feature transformation using ColumnTransformer

Model training using Random Forest


Using a Pipeline guarantees that identical preprocessing steps are applied during both training and prediction, reducing the risk of data leakage and improving reproducibility.

# Hyperparameter Optimization

Model performance was optimized using GridSearchCV with cross-validation.


Optimized parameters included:


Number of Trees

Maximum Tree Depth

Minimum Samples Split

Minimum Samples per Leaf


The best-performing model was automatically selected after cross-validation.
# Model Accuracy 

**Accuracy: 0.5880388349514563**

[[5516 1260]

 [4044 2055]
 
# REST API
# Available functionality:


GET /


Returns the API status.


POST /predict


Accepts customer information and returns a churn prediction.


Input Features

Age
Subscription Type

Contract Length

Usage Frequency

Total Spend


## Output
{
    "prediction": 1
}

# Technical Stack

Programming


Python


Data Analysis


Pandas

Matplotlib


Machine Learning

Scikit-Learn

Pipeline

ColumnTransformer

Random Forest

GridSearchCV


# Model Deployment

FastAPI

Joblib

# Project Outcome

This project demonstrates the complete lifecycle of a production-oriented machine learning application—from raw data analysis to deployment as a REST API.

# Key outcomes include:

Automated preprocessing with reusable pipelines

Robust model selection through cross-validation

Reliable prediction service via FastAPI

Reusable serialized model for deployment

Modular architecture suitable for future model upgrades



# Skills Demonstrated
Data Cleaning

Exploratory Data Analysis

Feature Engineering

Machine Learning

Hyperparameter Tuning

Classification Modeling

Model Evaluation

Model Serialization

API Development

Production-Oriented Workflow

Python Software Development

REST API Design


# 👨‍💻 Author

Mishkat Ullah

Data Analyst | Machine Learning Engineer

Python • SQL • Power BI • FastAPI • Scikit-Learn
