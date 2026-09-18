import numpy as np
import pandas as pd

def predict_next_route(start_area):
    areas = ['Area A (Downtown)', 'Area B (Suburbs)', 'Area C (Industrial)', 'Area D (Park)', 'Area E (Transit)']
    
    # Example transition probability matrix
    transition_matrix = np.array([
        [0.1, 0.4, 0.2, 0.2, 0.1],
        [0.3, 0.1, 0.1, 0.4, 0.1],
        [0.2, 0.2, 0.1, 0.1, 0.4],
        [0.4, 0.1, 0.2, 0.1, 0.2],
        [0.1, 0.3, 0.3, 0.2, 0.1]
    ])
    
    if start_area in areas:
        idx = areas.index(start_area)
        probs = transition_matrix[idx]
        next_step = areas[np.argmax(probs)]
        return next_step, probs
    return "Area A (Downtown)", [0.2]*5