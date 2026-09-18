import math

class SimplePredictor:
    def __init__(self):
        self.areas = ["Area A (Downtown)", "Area B (Suburbs)", "Area C (Industrial)", "Area D (Park)", "Area E (Transit)"]
    
    def predict(self, age_group, day, weather, usual_area):
        # Deterministic probabilistic scoring without C-extensions
        base_scores = {area: 10.0 for area in self.areas}
        
        if usual_area in base_scores:
            base_scores[usual_area] += 40.0
            
        if weather == "Rain":
            base_scores["Area E (Transit)"] += 20.0
            base_scores["Area A (Downtown)"] += 15.0
        elif weather == "Clear":
            base_scores["Area D (Park)"] += 25.0
            
        total = sum(base_scores.values())
        return {area: round((score / total) * 100, 1) for area, score in base_scores.items()}

if __name__ == "__main__":
    predictor = SimplePredictor()
    res = predictor.predict("18-25", "Friday", "Rain", "Area A (Downtown)")
    print("Pure Python Prediction System Ready:")
    for area, score in res.items():
        print(f" - {area}: {score}%")
