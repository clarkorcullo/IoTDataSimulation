# Import required libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations and random number generation
from datetime import datetime, timedelta  # For handling dates and times
import json  # For saving data in JSON format


def simulate_smart_logistics_data(num_records=100):
    """
    Simulate smart logistics IoT data.
    Args:
        num_records (int): Number of records to generate.
    Returns:
        pd.DataFrame: Simulated data as a pandas DataFrame.
    """
    data = []  # Initialize an empty list to store each record
    for _ in range(num_records):  # Loop to generate the specified number of records
        record = {
            # Generate a timestamp within the last 24 hours
            "timestamp": (datetime.now() - timedelta(minutes=np.random.randint(0, 1440))).strftime("%Y-%m-%d %H:%M:%S"),
            # Generate a random tracking ID for the package
            "tracking_id": f"PKG{np.random.randint(1000, 9999)}",
            # Generate a random device ID for the IoT device
            "device_id": f"DVC{np.random.randint(100, 999)}",
            # Generate a random latitude within a specific range (NYC area)
            "latitude": round(np.random.uniform(40.7128, 40.7300), 6),
            # Generate a random longitude within a specific range (NYC area)
            "longitude": round(np.random.uniform(-74.0060, -73.9352), 6),
            # Generate a random temperature value (°C for cold chain logistics)
            "temperature": round(np.random.uniform(2.0, 10.0), 2),
            # Generate a random humidity percentage
            "humidity": round(np.random.uniform(30.0, 70.0), 2),
            # Generate a random speed in km/h
            "speed_kmph": round(np.random.uniform(0, 100), 2),
            # Randomly select a status for the package
            "status": np.random.choice(["in_transit", "at_warehouse", "delivered", "delayed"])
        }
        data.append(record)  # Add the generated record to the list
    df = pd.DataFrame(data)  # Convert the list of records to a pandas DataFrame and return it
    df.insert(0, 'row_number', range(1, len(df) + 1))  # Add a row_number column starting from 1
    return df


def main():
    num_records = 100  # Number of records to generate (can be adjusted)
    df = simulate_smart_logistics_data(num_records)  # Generate the simulated data
    
    # Save the DataFrame as a CSV file (comma-separated values)
    df.to_csv("smart_tracking_data.csv", index=False)
    
    # Convert the DataFrame to a list of dictionaries for JSON output
    json_data = df.to_dict(orient='records')
    # Save the data as a JSON file with indentation for readability
    with open("smart_tracking_data.json", 'w') as f:
        json.dump(json_data, f, indent=2)
    
    # Print the first five rows of the DataFrame to the console (with row_number)
    print(df.head())


if __name__ == "__main__":  # Ensure this code runs only if the script is executed directly
    main()  # Call the main function to execute the simulation 