import pandas as pd
import os

DATA_FOLDER = "data/"

# List files in data folder
print("Files in data folder:")
print(os.listdir(DATA_FOLDER))
print("-" * 40)

#load drivers dataset
drivers_path = os.path.join(DATA_FOLDER, "drivers.csv")
drivers = pd.read_csv(drivers_path)

#Display some basic information
print("Drivers dataset:")
print(drivers.head())
print("-" * 40)

#Display basic stats
print("Summary statistics")
print(drivers.describe(include='all'))
print("-" * 40)

#Check for missing values
print("Missing values per column:")
print(drivers.isnull().sum())