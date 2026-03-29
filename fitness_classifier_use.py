import joblib
import pandas as pd
import tkinter as tk
from tkinter import messagebox
model = joblib.load("fitness_logreg_final.pkl")
def predict_fitness_gui():
    try:
        pullups = int(entry_pullups.get())
        pushups = int(entry_pushups.get())
        situps = int(entry_situps.get())
        plank = int(entry_plank.get())
        run = float(entry_run.get())
        data = pd.DataFrame([{
            "pullups_max": pullups,
            "pushups_1min": pushups,
            "situps_1min": situps,
            "plank_time_sec": plank,
            "run_time_1km": run}])
        result = model.predict(data)[0]
        messagebox.showinfo("Prediction Result", f"Predicted Fitness Level: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
root = tk.Tk()
root.title("Fitness Level Predictor")
root.geometry("350x350")
root.resizable(False, False)
tk.Label(root, text="Pull-ups (max):").pack()
entry_pullups = tk.Entry(root)
entry_pullups.pack()
tk.Label(root, text="Push-ups in 1 min:").pack()
entry_pushups = tk.Entry(root)
entry_pushups.pack()
tk.Label(root, text="Sit-ups in 1 min:").pack()
entry_situps = tk.Entry(root)
entry_situps.pack()
tk.Label(root, text="Plank time (sec):").pack()
entry_plank = tk.Entry(root)
entry_plank.pack()
tk.Label(root, text="1 km Run time (min):").pack()
entry_run = tk.Entry(root)
entry_run.pack()
predict_btn = tk.Button(root, text="Predict Fitness Level", command=predict_fitness_gui)
predict_btn.pack(pady=15)
root.mainloop()