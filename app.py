import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.prediction import SimplePredictor

predictor = SimplePredictor()

root = tk.Tk()
root.title("CASEFILE: AI Missing Person Investigation System")
root.geometry("600x520")

tk.Label(root, text="CASEFILE: Missing Person System", font=("Arial", 16, "bold"), fg="#1a252f").pack(pady=12)

frame = tk.LabelFrame(root, text=" Case Investigation Parameters ", font=("Arial", 10, "bold"), padx=10, pady=10)
frame.pack(pady=5, padx=15, fill="x")

tk.Label(frame, text="Age Group:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
age_combo = ttk.Combobox(frame, values=["18-25", "26-40", "41-60", "60+"], state="readonly")
age_combo.current(0)
age_combo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Day of Week:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
day_combo = ttk.Combobox(frame, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], state="readonly")
day_combo.current(4)
day_combo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Weather Condition:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
weather_combo = ttk.Combobox(frame, values=["Clear", "Rain", "Fog", "Snow"], state="readonly")
weather_combo.current(1)
weather_combo.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Frequently Visited Area:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
area_combo = ttk.Combobox(frame, values=predictor.areas, state="readonly")
area_combo.current(0)
area_combo.grid(row=3, column=1, padx=5, pady=5)

tree = ttk.Treeview(root, columns=("Area", "Priority Score", "Priority Level"), show="headings", height=5)
tree.heading("Area", text="Search Area")
tree.heading("Priority Score", text="Priority Score (%)")
tree.heading("Priority Level", text="Priority Rating")
tree.pack(pady=15, fill="x", padx=15)

def execute_prediction():
    for item in tree.get_children():
        tree.delete(item)
        
    predictions = predictor.predict(age_combo.get(), day_combo.get(), weather_combo.get(), area_combo.get())
    sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
    
    for area, score in sorted_predictions:
        if score >= 35.0:
            level = "Very High"
        elif score >= 20.0:
            level = "High"
        elif score >= 12.0:
            level = "Medium"
        else:
            level = "Low"
            
        tree.insert("", "end", values=(area, f"{score}%", level))

btn = tk.Button(root, text="Run Priority Score Analysis", command=execute_prediction, bg="#007bff", fg="white", font=("Arial", 11, "bold"), pady=5)
btn.pack(pady=5)

root.mainloop()
