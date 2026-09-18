import streamlit as st
import sys
import os

# Import your core logic backend
sys.path.append(os.path.abspath("src"))
from prediction import calculate_priority_scores

st.title("CASEFILE: AI Missing Person Investigation")
st.write("Decision-support system for missing person search area prioritization.")

# Simple interactive UI controls
age = st.slider("Select Missing Person Age", 1, 100, 25)
if st.button("Run Priority Score Analysis"):
    # Run backend function
    results = calculate_priority_scores(age) 
    st.dataframe(results)