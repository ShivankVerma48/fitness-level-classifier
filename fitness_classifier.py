# NOTE: Dataset not included in repository. Update path before running.


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
df = pd.read_csv("messy_realistic_fitness_dataset_1000.csv")
X = df[[
    "pullups_max",
    "pushups_1min",
    "situps_1min",
    "plank_time_sec",
    "run_time_1km"]]
y = df["fitness_level"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = LogisticRegression(
    C=1,
    penalty="l2",
    solver="lbfgs",
    max_iter=2000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
joblib.dump(model, "fitness_logreg_final.pkl")
print("Model saved as fitness_logreg_final.pkl")