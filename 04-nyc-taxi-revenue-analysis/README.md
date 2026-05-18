# Project 4: NYC Taxi January 2023 — End-to-End Data Pipeline

## Overview
A complete end-to-end data analytics pipeline analyzing 3M+ 
NYC Yellow Taxi trip records from January 2023. Built using 
Python scripts for data loading and cleaning, SQLite for 
SQL analysis, and Power BI for interactive visualization.

## Pipeline Architecture
Raw Parquet Data
↓
load_data.py (Python + SQLite)
↓
clean_data.py (Python + Pandas)
↓
analysis.py (SQL via SQLite)
↓
Power BI Dashboard

## Business Problem
NYC taxi operators face a critical challenge:
- When should drivers be on the road?
- Which days generate the most revenue?
- What hours have the highest fare potential?
- Which pickup zones drive the most revenue?

Without data — these are guesses.
With data — they become decisions.

## Project Structure
04-taxi_project/
│
├── notebook/
│   ├── load_data.py        # Loads parquet files into SQLite
│   ├── clean_data.py       # Cleans and validates trip data
│   └── README.md           # Notebook documentation
│
├── sql/
│   └── analysis.py         # SQL queries via Python SQLite
│
├── output/
│   ├── clean_trips.csv     # Cleaned dataset
│   ├── hourly_demand.csv   # Trips and avg fare by hour
│   ├── daily_revenue.csv   # Revenue and trips by day
│   └── zone_revenue.csv    # Revenue by pickup zone
│
├── taxi.db                 # SQLite database
└── NYC_Taxi_Analysis.pbix  # Power BI dashboard

## Pipeline Stages

### Stage 1 — load_data.py
- Loaded raw NYC Taxi parquet files into SQLite database
- Created structured table for efficient SQL querying
- Handled large file ingestion at 3M+ row scale

### Stage 2 — clean_data.py
- Removed invalid fare amounts (negative or zero fares)
- Removed invalid trip distances (zero or negative)
- Fixed data type inconsistencies
- Exported clean_trips.csv for downstream analysis

### Stage 3 — analysis.py
SQL queries written via Python (SQLite) to extract:
- Hourly demand patterns across all 24 hours
- Daily revenue breakdown by day of week
- Average fare and trip count per time period
- Pickup zone revenue ranking

### Stage 4 — Power BI Dashboard
- Interactive dashboard built on analysis outputs
- KPI cards, trend charts and location visuals
- Slicers for dynamic filtering

## Key Insights

### Peak Hour Analysis
| Hour | Total Trips | Avg Fare |
|------|-------------|----------|
| 18:00 (6pm) | 214,250 | $26.82 |
| 17:00 (5pm) | 207,852 | $28.73 |
| 04:00 (4am) | 17,472 | $32.09 ← Highest fare! |

💡 **Insight:** 6pm is the busiest hour but 4am has the 
highest average fare — airport runs dominate late night!

### Daily Revenue Analysis
| Day | Total Trips | Total Revenue |
|-----|-------------|---------------|
| Tuesday | 487,000 | $13,423,705 ← Highest! |
| Thursday | 438,536 | $12,046,435 |
| Sunday | 432,635 | $12,324,757 |
| Saturday | 437,764 | $11,207,003 |

💡 **Insight:** Tuesday beats Friday and Saturday for 
revenue — business travel dominates NYC taxi demand!

💡 **Insight:** Sunday has higher avg fare ($28.49) vs 
Saturday ($25.60) — longer, more expensive routes!

## Business Recommendations
✅ Max fleet deployment at 6pm every weekday
✅ Premium driver incentives on Tuesday for peak revenue  
✅ Keep drivers available at 4am — fewer trips, higher fares
✅ Target Sunday for high-fare long-distance routes
✅ Use January 2023 as performance baseline for future months

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python | Data pipeline scripting |
| Pandas | Data cleaning and transformation |
| SQLite | Database storage and SQL queries |
| Power BI | Interactive dashboard |
| Parquet | Raw data format |

## Dataset
- Source: NYC Taxi & Limousine Commission (TLC)
- Period: January 2023
- Size: 3M+ trip records
- Format: Parquet files
- Download: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## How to Run
1. Clone this repository
2. Install requirements:
pip install pandas sqlalchemy pyarrow
3. Run the pipeline in order:
python notebook/load_data.py
python notebook/clean_data.py
python sql/analysis.py
4. Open `NYC_Taxi_Analysis.pbix` in Power BI Desktop

## Project Series
This is Project 4 of my 4-project Data Analyst Portfolio:
- ✅ Project 1: Superstore Sales Analysis (SQL)
- ✅ Project 2: HR Analytics EDA (Python)  
- ✅ Project 3: HR Analytics Dashboard (Power BI)
- ✅ Project 4: NYC Taxi Pipeline (SQLite + Python + Power BI)

## Connect
- LinkedIn: linkedin.com/in/anusha-chowdary-d-843192295
- GitHub: github.com/Anusha3-d
