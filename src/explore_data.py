import pandas as pd
import os

DATA_FOLDER = "data/"

# List CSV files you have downloaded
csv_files = [
    'circuits.csv',
    'constructors.csv',
    'constructor_results.csv',
    'constructor_standings.csv',
    'drivers.csv',
    'driver_standings.csv',
    'lap_times.csv',
    'pit_stops.csv',
    'qualifying.csv',
    'races.csv',
    'results.csv',
    'seasons.csv',
    'status.csv'
]

# Load each CSV into a DataFrame
dataframes = {}

for file in csv_files:
    df_name = file.replace('.csv', '')
    df_path = os.path.join(DATA_FOLDER, file)
    df = pd.read_csv(df_path)
    dataframes[df_name] = df
    print(f"\n==== {df_name.upper()} ====")
    print(df.info())
    print(df.head())
