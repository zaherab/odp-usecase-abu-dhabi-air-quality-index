# Abu Dhabi Air Quality Index Use Case

## Overview
This repository contains a Python implementation for analyzing and visualizing the Abu Dhabi Air Quality Index dataset from the Abu Dhabi Open Data Platform.

## Requirements
- Python 3.8+
- Dependencies listed in requirements.txt

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Code Description
```python
n
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
try:
    data = pd.read_csv('abu_dhabi_air_quality.csv')
except FileNotFoundError:
    raise Exception("Dataset file not found. Please ensure 'abu_dhabi_air_quality.csv' is available.")

# Check required columns exist
required_columns = ['timestamp', 'station', 'PM2.5']
for column in required_columns:
    if column not in data.columns:
        raise Exception(f"Required column '{column}' is mi... # (truncated for brevity)
```

## Generated on
2024-12-27 11:29:23
