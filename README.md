# Fitness Level Classification using Machine Learning

This project focuses on classifying fitness levels using a machine learning model trained on structured data.


## Problem

Fitness assessment often requires manual evaluation. This project automates classification of fitness levels based on input features.


## Solution

A Logistic Regression model is trained to classify fitness levels and saved for reuse in predictions.


## Approach

### Data Processing
- Cleaned and structured dataset  
- Handled missing values  
- Prepared features for model training  

### Model
- Logistic Regression classifier  
- Trained on processed dataset  
- Saved model using `.pkl` for reuse  

### Usage
- Separate script (`fitness_classifier_use.py`) to load model  
- Performs predictions on new input data  


## Tech Stack

- Python  
- Pandas  
- Scikit-learn  


## Files

- `fitness_classifier.py` – Model training  
- `fitness_classifier_use.py` – Model usage/inference  
- `fitness_log_reg_final.pkl` – Trained model  


## Dataset

Dataset not included due to size constraints.


## My Contribution

- Built and trained logistic regression model  
- Processed dataset and handled missing values  
- Implemented model persistence using pickle  
- Developed inference script for real-world usage  


## How to Run

1. Install dependencies:
   pip install pandas scikit-learn  

2. Run training:
   python fitness_classifier.py  

3. Run prediction:
   python fitness_classifier_use.py  
