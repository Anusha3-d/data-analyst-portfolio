# Project 2: HR Analytics — Exploratory Data Analysis

## Overview
Analyzed IBM HR Analytics dataset with 1,470 employee 
records using Python (Pandas, Matplotlib, Seaborn).
Uncovered key insights about attrition, salary gaps 
and departmental performance.

## Tools Used
- Python 3.13
- Pandas — data cleaning & feature engineering
- Matplotlib — data visualization
- Seaborn — statistical charts
- Jupyter Notebook
- Dataset: Kaggle IBM HR Analytics

## Business Questions Answered
1. Which department has the highest attrition?
2. What is the age distribution of employees?
3. Which job roles earn the most and least?
4. What is the overall attrition rate?
5. How big is the salary gap across roles?

## Key Insights

### Insight 1 — R&D Attrition Crisis
R&D department has the highest number of employees 
leaving. These are the most skilled and hardest to 
replace employees in the company.
Recommendation: Invest in R&D retention programs.

### Insight 2 — Experienced Workforce Leaving
Average employee age is 37 years — experienced 
professionals in their prime. Yet 16.12% leave 
every year — above the 15% industry average.
Recommendation: Focus retention on 30-40 age group.

### Insight 3 — Salary Gap
Managers earn the most. Sales Representatives earn 
the least. 20x gap between minimum ($1,009) and 
maximum ($19,999) monthly salary.
Recommendation: Conduct urgent pay equity audit.

## Data Cleaning Steps
- Removed 4 useless columns (EmployeeCount, Over18,
  StandardHours, EmployeeNumber)
- Fixed 10 columns wrongly stored as numbers 
  (converted to category type)
- Created 3 new columns:
  * SalaryCategory (Low/Medium/High/Very High)
  * ExperienceCategory (Fresher/Junior/Mid/Senior)
  * AgeGroup (18-25/26-35/36-45/46-60)

## Charts Created
1. Attrition by Department — Bar chart
2. Age Distribution — Histogram with KDE curve
3. Monthly Income by Job Role — Horizontal bar chart

## Files
- hr_analytics_eda.ipynb — Full analysis notebook
- hr_analytics.csv — Original dataset
- hr_analytics_cleaned.csv — Cleaned dataset
- chart1_attrition_by_department.png
- chart2_age_distribution.png
- chart3_salary_by_jobrole.png

## Connect
- LinkedIn: linkedin.com/in/anusha-chowdary-d-843192295
- GitHub: github.com/Anusha3-d
