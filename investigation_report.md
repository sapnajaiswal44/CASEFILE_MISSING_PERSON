# CASEFILE: An AI-Powered Missing Person Investigation and Probable Location Prediction System

**Project Type:** Individual Advanced Machine Learning Simulation Project  
**Author:** Sapna  
**Case File ID:** MP-2026-017  

---

## 1. Abstract
When a person goes missing, analyzing movement patterns manually under time constraints is challenging[cite: 1, 2]. This project implements an Machine Learning investigation-support system designed to evaluate historical GPS trajectories, spatial-temporal attributes, and environmental conditions to predict probable missing-person locations and rank search-priority areas[cite: 1, 2].

## 2. Problem Statement & Objectives
* **Core Question:** "Based on available historical and contextual evidence, which locations should be investigated first?"[cite: 2]
* **Objectives:**
  1. Process historical trajectories and movement patterns[cite: 3].
  2. Perform spatial clustering (hotspot analysis) and anomaly detection[cite: 3].
  3. Predict target geographical areas using probabilistic decision rules[cite: 3].
  4. Generate a Search Priority Score to assist search-and-rescue allocation[cite: 3].

## 3. Dataset Description
* **GPS Trajectory Source:** Synthetic trajectories structured after Microsoft GeoLife GPS Dataset standards.
* **Feature Schema:** Case_ID, Age_Group, Gender, Last_Latitude, Last_Longitude, Last_Seen_Time, Day, Weather, Usual_Area, Average_Distance, Average_Speed, Target_Area.

## 4. System Architecture & Methodology
* **Feature Engineering:** Extracted temporal indicators (day of week, time since last seen) and spatial indicators (distance from usual area).
* **Movement Pattern Clustering:** Grouped historical stay points into density-based hotspots.
* **Search Priority Scoring Mechanism:**
  $$\text{Priority Score} = (\text{Base Model Probability}) + (\text{Usual Area Weight}) + (\text{Weather Factor})$$
  Score Range: $0 - 100\%$ ($81-100\%$: Very High, $61-80\%$: High, $31-60\%$: Medium, $0-30\%$: Low).

## 5. Model Evaluation & Results
In simulated test runs for Case MP-2026-017:
* **Top-1 Accuracy:** High convergence towards primary historical stay-points.
* **Top-3 Accuracy:** Successfully captured secondary transition nodes.
* **Search Priority Breakdown:**
  1. Area A (Downtown) — Very High Priority
  2. Area E (Transit) — High Priority
  3. Area B (Suburbs) — Medium Priority

## 6. Ethical Considerations & Limitations
* **Non-Binding Output:** Predictions are strictly probabilistic and must never be treated as definitive proof of location.
* **Academic Simulation:** Constructed exclusively using synthetic case records without personally identifiable information (PII)[cite: 1].