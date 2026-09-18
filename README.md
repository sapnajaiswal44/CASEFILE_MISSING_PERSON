# CASEFILE: AI-Powered Missing Person Investigation System

## Overview
CASEFILE is a Machine Learning investigation-support framework designed to assist law enforcement 
and search-and-rescue teams during critical early hours. By analyzing historical movement profiles, 
spatial stays, and contextual indicators (weather, time, location history), the platform calculates 
actionable Search Priority Scores (%) for surrounding target areas.

## Architecture
- **Backend Engine:** Pure Python probabilistic inference engine (`src/prediction.py`)
- **Desktop Client:** Lightweight Tkinter GUI interface (`app/pure_app.py`)
- **Documentation:** Formal case report and viva presentation deck (`reports/`)