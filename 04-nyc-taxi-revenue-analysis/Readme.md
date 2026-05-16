# NYC Taxi Revenue Analysis

## Overview
End-to-end data analysis of 3,066,766 NYC Yellow Taxi trips (January 2023)
identifying revenue patterns by zone, time, and distance.

## Tools Used
- SQL (DuckDB) — data loading and aggregation
- Python (Pandas) — data cleaning and feature engineering
- Power BI — interactive dashboard

## Key Findings
- JFK Airport is the highest revenue zone ($11.9M, avg fare $77)
- Peak demand occurs at 6PM–7PM (214,250 trips)
- 69,684 bad rows removed (2.3% of data)
- Very long trips (10+ miles) generate highest avg fare ($84.66)
- Tuesday is the highest revenue day ($13.4M)

## Dashboard Screenshots
![KPI Overview](screenshots/dashboard_page1.png)
![Demand Analysis](screenshots/dashboard_page2.png)

## Files
- `notebook/load_data.py` — loads parquet data into DuckDB
- `notebook/clean_data.py` — cleans data and engineers features
- `sql/analysis.py` — SQL aggregation queries