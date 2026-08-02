
# Project 2: Python-Based Data Processing

## Overview
This project focuses on processing customer data using Python and Pandas. The goal is to clean the dataset, apply business rules, perform data transformations, and generate meaningful outputs that can be used for future data analysis and Machine Learning.

## Dataset
- **Name:** Telco Customer Churn Dataset
- **Source:** Kaggle
- **File:** WA_Fn-UseC_-Telco-Customer-Churn.csv

## Objectives
- Read and process the dataset using Python.
- Handle missing values and duplicate records.
- Convert data types where necessary.
- Apply business rules and data transformations.
- Generate meaningful insights from the data.
- Save a clean, processed dataset.

## Business Rules Applied
### Rule 1: Monthly Charges Category
Customers are categorized based on Monthly Charges:
- Low: Less than 35
- Medium: 35 to 69.99
- High: 70 or above

### Rule 2: Customer Tenure Category
Customers are categorized based on their tenure:
- New: 0–12 months
- Regular: 13–36 months
- Loyal: More than 36 months

## Data Processing Steps
- Loaded the dataset using Pandas.
- Checked dataset structure and summary.
- Identified and handled missing values.
- Removed duplicate records.
- Converted the `TotalCharges` column to numeric.
- Filled missing values using the median.
- Created new categorical columns based on business rules.
- Generated summary statistics.
- Exported the processed dataset.

## Output
The project generates:
- Cleaned dataset
- Processed dataset (`Processed_Telco_Customer_Churn.csv`)
- Customer charge categories
- Customer tenure categories
- Churn summary
- Average monthly charges
- Average customer tenure

## Technologies Used
- Python
- Pandas


## Future Scope
The processed dataset can be used to build a Machine Learning model to predict customer churn and support business decision-making.

## Author
Anisha Kumari
B.Tech CSE | AI & Machine Learning Enthusiast
