import duckdb
import pandas as pd

PROJECT_PATH = r"C:\Users\anuch\OneDrive\Documents\data-analyst-portfolio\04-taxi_project"

con = duckdb.connect(PROJECT_PATH + "\\taxi.db")

# Load raw data into pandas
print("Loading data...")
df = con.execute("SELECT * FROM yellow_trips").fetchdf()

print(f"Raw rows: {len(df)}")

# ── CLEANING ──────────────────────────────────────────

# Remove zero or negative fares
df = df[df['total_amount'] > 0]

# Remove zero or negative distances
df = df[df['trip_distance'] > 0]

# Remove impossible speeds (over 100mph)
df['duration_mins'] = (
    pd.to_datetime(df['tpep_dropoff_datetime']) - 
    pd.to_datetime(df['tpep_pickup_datetime'])
).dt.total_seconds() / 60

df = df[df['duration_mins'] > 0]
df['speed_mph'] = (df['trip_distance'] / (df['duration_mins'] / 60))
df = df[df['speed_mph'] < 100]

# Remove extreme fare outliers (over $500)
df = df[df['total_amount'] < 500]

print(f"Clean rows: {len(df)}")
print(f"Rows removed: {3066766 - len(df)}")

# ── FEATURE ENGINEERING ───────────────────────────────

# Hour of day
df['hour'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.hour

# Day of week
df['day_of_week'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.day_name()

# Rush hour flag (7-9AM and 5-7PM on weekdays)
df['is_rush_hour'] = (
    (df['hour'].between(7, 9) | df['hour'].between(17, 19)) &
    (~df['day_of_week'].isin(['Saturday', 'Sunday']))
).astype(int)

# Trip distance bucket
df['distance_bucket'] = pd.cut(
    df['trip_distance'],
    bins=[0, 2, 5, 10, 50],
    labels=['Short (0-2mi)', 'Medium (2-5mi)', 'Long (5-10mi)', 'Very Long (10+mi)']
)

print("\n=== RUSH HOUR BREAKDOWN ===")
print(df.groupby('is_rush_hour')['total_amount'].agg(['count', 'mean']).round(2))

print("\n=== TRIPS BY DISTANCE BUCKET ===")
print(df.groupby('distance_bucket', observed=True)['total_amount'].agg(['count', 'mean']).round(2))

# Save clean data for Power BI
df.to_csv(PROJECT_PATH + "\\output\\clean_trips.csv", index=False)
print("\nClean data saved to output folder!")