import streamlit as st
import sys
import os

# Add both current directory and 'src' subdirectory explicitly to system path
base_path = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(base_path, "src")

if base_path not in sys.path:
    sys.path.insert(0, base_path)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Safe fallback import logic
try:
    from src.prediction import calculate_priority_scores
except ImportError:
    from prediction import calculate_priority_scores
