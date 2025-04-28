import pandas as pd
import os

# Load data
qualifying_data = pd.read_csv('data/qualifying.csv')
races_data = pd.read_csv('data/races.csv')
results_data = pd.read_csv('data/results.csv')
drivers_data = pd.read_csv('data/drivers.csv')
constructors_data = pd.read_csv('data/constructors.csv')

# Strip any leading or trailing spaces from the column names
qualifying_data.columns = qualifying_data.columns.str.strip()
races_data.columns = races_data.columns.str.strip()
results_data.columns = results_data.columns.str.strip()
drivers_data.columns = drivers_data.columns.str.strip()
constructors_data.columns = constructors_data.columns.str.strip()

# Merge datasets on common keys
merged_data = pd.merge(qualifying_data, races_data, on='raceId')
merged_data = pd.merge(merged_data, results_data, on=['raceId', 'driverId'])
merged_data = pd.merge(merged_data, drivers_data, on='driverId')

# Inspect columns before merging with constructors_data
print("Columns before merging with constructors_data:")
print(merged_data.columns)

# Merge with constructors data, handle duplicate columns
merged_data = pd.merge(merged_data, constructors_data, left_on='constructorId_y', right_on='constructorId', how='left')

# Drop the unwanted '_x' and '_y' suffix columns (duplicates)
merged_data.drop(['constructorId_x', 'constructorId_y', 'name_x', 'name_y', 'nationality_x', 'nationality_y', 'url_x', 'url_y'], axis=1, inplace=True)

# Rename columns for clarity (optional)
merged_data.rename(columns={'constructorId': 'constructorId', 'name': 'constructorName', 'nationality': 'constructorNationality', 'url': 'constructorUrl'}, inplace=True)

# For simplicity, fill missing values with 0
merged_data.fillna(0, inplace=True)

# Save the cleaned and merged data to a CSV file
merged_data.to_csv('data/merged_data.csv', index=False)

print("Merged data saved to 'merged_data.csv'.")
