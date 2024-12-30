n
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
import requests

def fetch_data():
    """
    Function to fetch the air quality data from a provided API endpoint or URL.
    In this example, it's shown with a static file method.
    """
    try:
        # For demonstration, replace the URL with an actual data source URL or file path
        url = "https://example.com/adel_qual_index.json"
        
        # Load data
        response = requests.get(url)
        data = json.loads(response.text)
        
        # Convert the JSON data into a Pandas DataFrame
        df = pd.DataFrame(data)
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def preprocess_data(df):
    """
    Function to preprocess the air quality data.
    This includes handling missing values, formatting datetime, and filtering relevant columns.
    """
    try:
        # Ensure datetime is in proper format
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Filtering the desired parameters
        df = df[['timestamp', 'station_id', 'PM2.5', 'PM10']]

        # Handle missing values by forward filling
        df = df.fillna(method='ffill')

    except KeyError as e:
        print(f"Data is missing expected columns: {e}")
    
    return df

def visualize_data(df):
    """
    Function to visualize PM2.5 and PM10 levels over time.
    Uses seaborn for a better aesthetic.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 7))
    
    try:
        # Plot PM2.5 and PM10 levels
        sns.lineplot(data=df, x='timestamp', y='PM2.5', hue='station_id', palette='tab10', label='PM2.5', linestyle='-')
        sns.lineplot(data=df, x='timestamp', y='PM10', hue='station_id', palette='tab20', label='PM10', linestyle='--')
        
        plt.title("PM2.5 and PM10 Levels Over Time in Abu Dhabi")
        plt.xlabel("Date")
        plt.ylabel("Concentration (µg/m³)")
        plt.legend(title='Parameter Levels')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error during visualization: {e}")

def main():
    # Initial data fetch
    df = fetch_data()
    
    if df.empty:
        print("No data available to analyze.")
        return

    # Preprocess the data
    df_clean = preprocess_data(df)
    
    if not df_clean.empty:
        # Visualization
        visualize_data(df_clean)
    else:
        print("No clean data available for analysis.")

if __name__ == "__main__":
    main()