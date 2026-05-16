import duckdb

PROJECT_PATH = r"C:\Users\anuch\OneDrive\Documents\data-analyst-portfolio\04-taxi_project"

con = duckdb.connect(PROJECT_PATH + "\\taxi.db")

con.execute(f"""
    CREATE OR REPLACE TABLE yellow_trips AS
    SELECT * FROM read_parquet('{PROJECT_PATH}\\data\\yellow_tripdata_2023-01.parquet')
""")

con.execute(f"""
    CREATE OR REPLACE TABLE zone_lookup AS
    SELECT * FROM read_csv_auto('{PROJECT_PATH}\\data\\taxi_zone_lookup.csv')
""")

print("=== ROW COUNT ===")
print(con.execute("SELECT COUNT(*) as total_rows FROM yellow_trips").fetchdf())

print("\n=== FIRST 5 ROWS ===")
print(con.execute("SELECT * FROM yellow_trips LIMIT 5").fetchdf())

print("\n=== ZONE TABLE PREVIEW ===")
print(con.execute("SELECT * FROM zone_lookup LIMIT 5").fetchdf())

print("\nData loaded successfully!")