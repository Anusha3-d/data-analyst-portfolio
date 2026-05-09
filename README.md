# Anusha Chowdary — Data Analyst Portfolio

👋 Hi! I'm a data analytics fresher from Bengaluru, passionate about
turning raw data into clear, actionable business insights.

## 🛠️ Tools & Skills
- **SQL** — data extraction, joins, aggregations, subqueries, CASE WHEN
- **Python** (Pandas, Matplotlib, Seaborn) — EDA, data cleaning, visualization
- **Power BI / Tableau** — dashboards & data storytelling.
- **Excel** — pivot tables, charts, VLOOKUP, analysis

## 📁 Projects

| # | Project | Tools | Status | Key Insight |

| 1 | [Superstore Sales Analysis](./01-sql-sales-analysis) | SQL, SQLite | ✅ Complete | Discounts above 20% = negative profit |
| 2 | [HR Analytics EDA](./02-python-eda) | Python, Pandas, Matplotlib, Seaborn | ✅ Complete | 16.12% attrition — above industry average |
| 3 | HR Analytics Dashboard | Power BI |  ✅ Complete
| 4 | End-to-End Pipeline | SQL + Python + Power BI | ⏳ Upcoming | Coming soon |

## 📊 Project 1 — Superstore Sales Analysis (SQL)

**Dataset:** Kaggle Superstore Sales — 9,994 orders  
**Tools:** SQL, SQLite, DB Browser for SQLite

### Key Findings:
- 💰 Total Sales: $2.29M | Total Profit: $286K | Margin: **12.47%**
- 🔴 Tables & Bookcases have **negative profit** despite high sales
- 🔴 Any discount above **20% generates losses** — every single time
- 🔴 Texas is the **worst performing state** due to excessive discounting
- ✅ West region is the **most profitable** across all markets
- ✅ Canon imageCLASS Copier is the **#1 profit-making product**
- ✅ Business grew **consistently from 2014 to 2017**

### SQL Concepts Used:
SELECT, FROM, WHERE, GROUP BY, ORDER BY, LIMIT, COUNT, SUM, AVG,
MIN, MAX, ROUND, AS, CASE WHEN, SUBSTR, LENGTH, Subqueries

---

##  Project 2 — HR Analytics EDA (Python)

**Dataset:** Kaggle IBM HR Analytics — 1,470 employees, 35 columns  
**Tools:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

### Key Findings:
- 🔴 Attrition rate: **16.12%** — above industry average of 15%
- 🔴 **R&D department** has the highest employee attrition
- 🔴 **20x salary gap** — minimum $1,009 to maximum $19,999
- 🔴 **Sales Representatives** are the lowest paid role
- ✅ Average employee age: **37 years**
- ✅ **Managers** are the highest paid role

### Data Cleaning Steps:
- Removed 4 useless columns (EmployeeCount, Over18, StandardHours, EmployeeNumber)
- Fixed 10 columns incorrectly typed as numeric → converted to category
- Engineered 3 new insight columns:
  - `SalaryCategory` — Low / Medium / High / Very High
  - `ExperienceCategory` — Fresher / Junior / Mid / Senior
  - `AgeGroup` — 18-25 / 26-35 / 36-45 / 46-60

### Charts Built:
1. Attrition by Department — bar chart
2. Age Distribution — histogram with KDE curve
3. Monthly Income by Job Role — horizontal bar chart

### Python Concepts Used:
import, pd.read_csv, df.shape, df.info(), df.describe(),
value_counts(), df.drop(), astype(), pd.cut(), groupby(),
matplotlib, seaborn, savefig()

---

##  30-Day Challenge Progress

> I am currently completing a 30-day data analyst portfolio challenge —
> building 4 real-world projects and posting daily on LinkedIn.

| Day | Achievement |
|-----|------------|
| Day 1-2 | GitHub setup + Kaggle + environment setup |
| Day 3-5 | Project 1 — SQL Sales Analysis complete |
| Day 6-7 | LinkedIn posts + networking |
| Day 8-11 | Project 2 — Python HR EDA complete |
| Day 12-14 | LinkedIn posts + profile updates |
| Day 15-18 | Project 3 — Power BI Dashboard Complete |
| Day 22-26 | Project 4 — End-to-End Pipeline (upcoming) |
| Day 27-30 | Final posts + job applications |

---

## 📈 LinkedIn
Follow my daily data analytics journey:
**linkedin.com/in/anusha-chowdary-d-843192295**

---

## 🔗 Connect
- 💼 LinkedIn: [Anusha Chowdary](https://linkedin.com/in/anusha-chowdary-d-843192295)
- 🐙 GitHub: [Anusha3-d](https://github.com/Anusha3-d)
- 📊 Kaggle: [anushachowdary](https://kaggle.com/anushachowdary)

---

 **Star this repo if you find it helpful!**
> "Turning raw data into actionable insights — one project at a time."
