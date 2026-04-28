-- ================================================
-- SUPERSTORE SALES ANALYSIS
-- Analyst: Anusha Chowdary
-- Dataset: Superstore Sales (9,994 orders)
-- Tool: SQLite / DB Browser
-- ================================================

-- Query 1: First look at the data
SELECT *
FROM superstore_sales
LIMIT 10;

-- Query 2: Total number of orders
SELECT COUNT(*) AS total_orders
FROM superstore_sales;

-- Query 3: Total Sales and Profit
SELECT 
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore_sales;

-- Query 4: Profit by Region
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore_sales
GROUP BY Region
ORDER BY total_profit DESC;

-- Query 5: Sales by Category
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    COUNT(*) AS total_orders
FROM superstore_sales
GROUP BY Category
ORDER BY total_sales DESC;

-- Query 6: Loss making Sub-Categories
SELECT 
    `Sub-Category`,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore_sales
GROUP BY `Sub-Category`
ORDER BY total_profit ASC;

-- Query 7: Top 5 most profitable products
SELECT 
    `Product Name`,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore_sales
GROUP BY `Product Name`
ORDER BY total_profit DESC
LIMIT 5;

-- Query 8: Sales trend by Year
SELECT 
    CASE 
        WHEN LENGTH(`Order Date`) = 10 THEN SUBSTR(`Order Date`, 7, 4)
        WHEN LENGTH(`Order Date`) = 9 THEN '20' || SUBSTR(`Order Date`, 7, 2)
        WHEN LENGTH(`Order Date`) = 8 THEN '20' || SUBSTR(`Order Date`, 7, 2)
    END AS year,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    COUNT(*) AS total_orders
FROM superstore_sales
GROUP BY year
ORDER BY year ASC;

-- Query 9: Top 10 customers by Sales
SELECT 
    `Customer Name`,
    COUNT(*) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore_sales
GROUP BY `Customer Name`
ORDER BY total_sales DESC
LIMIT 10;

-- Query 10: Worst performing States
SELECT 
    State,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    COUNT(*) AS total_orders
FROM superstore_sales
GROUP BY State
ORDER BY total_profit ASC
LIMIT 10;

-- Query 11: How Discounts impact Profit
SELECT 
    CASE
        WHEN Discount = 0 THEN '0% No Discount'
        WHEN Discount <= 0.1 THEN '1-10% Low Discount'
        WHEN Discount <= 0.2 THEN '11-20% Medium Discount'
        WHEN Discount <= 0.3 THEN '21-30% High Discount'
        ELSE 'Above 30% Very High Discount'
    END AS discount_range,
    COUNT(*) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Profit), 2) AS avg_profit
FROM superstore_sales
GROUP BY discount_range
ORDER BY total_profit DESC;

-- Query 12: Average Order Value
SELECT 
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(MIN(Sales), 2) AS min_order_value,
    ROUND(MAX(Sales), 2) AS max_order_value,
    ROUND(SUM(Sales), 2) AS total_sales,
    COUNT(*) AS total_orders
FROM superstore_sales;

-- Query 13: Shipping Mode Analysis
SELECT 
    `Ship Mode`,
    COUNT(*) AS total_orders,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM superstore_sales), 2) AS percentage,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore_sales
GROUP BY `Ship Mode`
ORDER BY total_orders DESC;