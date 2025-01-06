n
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import logging

# Set up logging for debug
logging.basicConfig(level=logging.INFO)

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path, parse_dates=['timestamp'])
        logging.info("Data loaded successfully.")
    except FileNotFoundError:
        logging.error("The file was not found.")
        return None
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None
    return data

def preprocess_data(data):
    """Preprocess the data by handling missing values and converting timestamp."""
    if data is not None:
        # Fill missing values with median value of the column
        data.fillna(data.median(), inplace=True)
        logging.info("Data preprocessing completed.")
    else:
        logging.warning("No data to preprocess.")
    return data

def visualize_data(data):
    """Visualize air quality data for key pollutants."""
    if data is not None:
        sns.set(style="whitegrid")
        plt.figure(figsize=(15, 10))

        # Create a line plot for each pollutant
        pollutants = ["PM2.5", "PM10", "NO2", "SO2", "O3", "CO"]
        for pollutant in pollutants:
            sns.lineplot(x='timestamp', y=pollutant, data=data, label=pollutant)
        
        plt.title('Air Quality Index Trends (Abu Dhabi)')
        plt.xlabel('Time')
        plt.ylabel('Concentration (µg/m³)')
        plt.legend(title='Pollutants')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.show()
    else:
        logging.warning("No data to visualize.")

def main():
    file_path = 'path_to_abu_dhabi_air_quality_data.csv'  # Update with the correct path
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    visualize_data(processed_data)

if __name__ == "__main__":
    main()