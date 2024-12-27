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
        raise Exception(f"Required column '{column}' is missing from the dataset.")

# Convert timestamp to datetime object
try:
    data['timestamp'] = pd.to_datetime(data['timestamp'])
except Exception as e:
    raise Exception("Error parsing 'timestamp' column.") from e

# Set timestamp as index
data.set_index('timestamp', inplace=True)

# Resample data to daily average of PM2.5
daily_avg_pm25 = data['PM2.5'].resample('D').mean()

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(daily_avg_pm25, label='Daily Average PM2.5', color='blue')
plt.title('Daily Average PM2.5 Levels in Abu Dhabi (2020-Present)')
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('abu_dhabi_pm25_trends.png')
plt.show()