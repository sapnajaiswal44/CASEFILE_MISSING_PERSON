import streamlit as st
import sys
import os

# Get absolute path to the directory containing app_web.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'src' folder to the Python search path
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Import backend prediction module
from prediction import calculate_priority_scores
