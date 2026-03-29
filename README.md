# Fitness Level Classification using Machine Learning

This project predicts a user's fitness level using a machine learning model and provides a graphical interface for real-time predictions.

---

## Problem

Assessing fitness levels manually can be subjective and inconsistent. This project automates fitness classification using measurable physical performance data.

---

## Solution

A Logistic Regression model is trained on fitness-related features and deployed through a GUI application that allows users to input their data and receive predictions instantly.

---

## Features

- Machine learning-based fitness classification  
- Logistic Regression model with tuned parameters  
- Model evaluation using accuracy, classification report, and confusion matrix  
- Saved model using joblib for reuse  
- GUI application (Tkinter) for real-time predictions  

---

## Technical Implementation

### Model Training
- Loaded dataset using Pandas  
- Selected key features:
  - Pull-ups (max)
  - Push-ups (1 min)
  - Sit-ups (1 min)
  - Plank time (seconds)
  - 1 km run time  

- Split dataset into training and testing sets  
- Trained Logistic Regression model (`max_iter=2000`)  
- Evaluated using:
  - Accuracy score  
  - Classification report  
  - Confusion matrix  

### Model Deployment
- Saved trained model as `fitness_logreg_final.pkl`  
- Loaded model using `joblib`  
- Built GUI using Tkinter  
- Users input values → model predicts fitness level  

---

## Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- Tkinter  
- Joblib  

---

## Project Structure

- `fitness_classifier.py` – Model training and evaluation  
- `fitness_classifier_use.py` – GUI application for predictions  
- `fitness_logreg_final.pkl` – Saved trained model  
- `messy_realistic_fitness_dataset_1000.csv` – Dataset used for training  

---

## Dataset

The dataset is included in this repository and used for training the model.

---

## My Contribution

- Built and trained Logistic Regression model  
- Performed feature selection and evaluation  
- Implemented model saving using joblib  
- Developed GUI-based prediction system  

---

## How to Run

1. Install dependencies:
   pip install pandas scikit-learn joblib  

2. Train the model:
   python fitness_classifier.py  

3. Run the application:
   python fitness_classifier_use.py  

4. Enter fitness metrics in the GUI to get prediction  

---

## Insight

This project demonstrates how machine learning models can be integrated into user-friendly applications for practical use.
