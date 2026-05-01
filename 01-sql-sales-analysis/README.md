# Project 1: Superstore Sales Analysis

## Overview
Analyzed 9,994 real sales orders from the Superstore dataset using SQL.
Uncovered key business insights around profitability, discounting strategy,
regional performance and customer behaviour.

## Tools Used
- SQL (SQLite)
- DB Browser for SQLite
- Dataset: Superstore Sales (Kaggle)

## Business Questions Answered
1. What is the overall sales and profit performance?
2. Which region generates the most profit?
3. Which product categories and sub-categories are losing money?
4. Who are the top 10 most valuable customers?
5. Which states are underperforming?
6. How do discounts impact profit?
7. What is the average order value?
8. Which shipping mode is most popular and profitable?

## Key Insights Found

### Insight 1 — The Discount Danger Line
Discounts above 20% consistently generate negative profit.
Recommendation: Cap all discounts at 20% maximum.

### Insight 2 — The Furniture Trap
Furniture is the highest selling category but Tables and Bookcases
have negative profit. High sales volume is masking serious losses.
Recommendation: Review pricing strategy for Tables and Bookcases.

### Insight 3 — The Texas Problem
Texas generates significant sales but is the worst performing state
for profit — likely due to excessive discounting.
Recommendation: Reduce discount approvals in Texas region.

### Insight 4 — Top Customer
Sean Miller is the #1 customer by sales volume.
Average order value across all customers: $229.86

### Insight 5 — Consistent Growth
Business grew consistently year on year from 2014 to 2017.
West region leads all regions in profitability.

## Files
- superstore_analysis.sql — All 13 SQL queries
- superstore_sales.csv — Raw dataset (source: Kaggle)

## How to Run
1. Download DB Browser for SQLite (free): https://sqlitebrowser.org
2. Open superstore.db in DB Browser
3. Go to Execute SQL tab
4. Copy any query from superstore_analysis.sql and run it

## Connect
- LinkedIn:linkedin.com/in/anusha-chowdary-d-843192295
- GitHub: github.com/Anusha3-d
