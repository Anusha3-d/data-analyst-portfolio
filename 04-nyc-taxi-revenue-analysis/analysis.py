import duckdb
import pandas as pd

PROJECT_PATH = r"C:\Users\anuch\OneDrive\Documents\data-analyst-portfolio\04-taxi_project"

con = duckdb.connect(PROJECT_PATH + "\\taxi.db")

# Query 1 — Revenue and trip stats by pickup zone
zone_revenue = con.execute("""
    SELECT 
        z.Zone as pickup_zone,
        z.Borough as borough,
        COUNT(*) as total_trips,
        ROUND(SUM(t.total_amount), 2) as total_revenue,
        ROUND(AVG(t.total_amount), 2) as avg_revenue_per_trip,
        ROUND(AVG(t.trip_distance), 2) as avg_distance
    FROM yellow_trips t
    JOIN zone_lookup z ON t.PULocationID = z.LocationID
    WHERE t.total_amount > 0 
      AND t.trip_distance > 0
    GROUP BY z.Zone, z.Borough
    ORDER BY total_revenue DESC
""").fetchdf()

# Query 2 — Trips by hour of day
hourly_demand = con.execute("""
    SELECT 
        EXTRACT(HOUR FROM tpep_pickup_datetime) as hour_of_day,
        COUNT(*) as total_trips,
        ROUND(AVG(total_amount), 2) as avg_fare
    FROM yellow_trips
    WHERE total_amount > 0
    GROUP BY hour_of_day
    ORDER BY hour_of_day
""").fetchdf()

# Query 3 — Revenue by day of week
daily_revenue = con.execute("""
    SELECT 
        DAYNAME(tpep_pickup_datetime) as day_of_week,
        COUNT(*) as total_trips,
        ROUND(SUM(total_amount), 2) as total_revenue,
        ROUND(AVG(total_amount), 2) as avg_fare
    FROM yellow_trips
    WHERE total_amount > 0
    GROUP BY day_of_week
""").fetchdf()

# Save all outputs to CSV for Power BI
zone_revenue.to_csv(PROJECT_PATH + "\\output\\zone_revenue.csv", index=False)
hourly_demand.to_csv(PROJECT_PATH + "\\output\\hourly_demand.csv", index=False)
daily_revenue.to_csv(PROJECT_PATH + "\\output\\daily_revenue.csv", index=False)

print("=== TOP 10 ZONES BY REVENUE ===")
print(zone_revenue.head(10))

print("\n=== HOURLY DEMAND ===")
print(hourly_demand)

print("\n=== DAILY REVENUE ===")
print(daily_revenue)

print("\nSQL analysis complete! Files saved to output folder.")