import streamlit as st
import pandas as pd

st.set_page_config(page_title="CASEFILE AI System", layout="centered")
st.title("CASEFILE: AI Missing Person Investigation")
st.caption("Spatial-Temporal Search Area & Priority Score Analyzer")

st.divider()

# Input Panel
st.header("1. Investigation Context")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Missing Person Age", min_value=1, max_value=100, value=25)
    last_seen_day = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

with col2:
    weather = st.selectbox("Weather Condition", ["Clear", "Rainy", "Foggy", "Extreme Cold/Heat"])
    urban_density = st.selectbox("Location Type", ["Urban", "Suburban", "Rural/Dense Forest"])

st.divider()

# Priority Calculation Function
def get_priority_scores(age, weather, location):
    base_scores = {
        "Zone A (Primary Radius - 1km)": 45,
        "Zone B (Secondary Radius - 5km)": 30,
        "Zone C (Frequent Transit Hubs)": 15,
        "Zone D (Extended Outer Perimeter)": 10
    }
    
    if age < 12 or age > 65:
        base_scores["Zone A (Primary Radius - 1km)"] += 15
        base_scores["Zone D (Extended Outer Perimeter)"] -= 5
    if weather in ["Rainy", "Extreme Cold/Heat"]:
        base_scores["Zone A (Primary Radius - 1km)"] += 10
        base_scores["Zone C (Frequent Transit Hubs)"] -= 5

    total = sum(base_scores.values())
    
    data = []
    for zone, score in base_scores.items():
        percentage = round((score / total) * 100, 1)
        priority = "Very High" if percentage >= 40 else "High" if percentage >= 25 else "Medium" if percentage >= 15 else "Low"
        data.append({"Search Area": zone, "Priority Level": priority, "Priority Score (%)": percentage})
        
    return pd.DataFrame(data)

# Execution Button
if st.button("Run Search Area Analysis", type="primary"):
    results = get_priority_scores(age, weather, urban_density)
    
    st.header("2. Prioritized Search Zones")
    st.dataframe(results, use_container_width=True)
    
    top_zone = results.iloc[0]["Search Area"]
    st.success(f"**Recommended Focus:** Immediate deployment prioritized for **{top_zone}**.")
