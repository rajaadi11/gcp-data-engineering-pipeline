-- =====================================================
-- GCP DATA ENGINEERING PIPELINE
-- BigQuery Sales Analytics
-- =====================================================


-- 1. TOTAL RECORDS
SELECT
    COUNT(*) AS total_records
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`;


-- 2. DATA QUALITY CHECK
SELECT
    COUNT(*) AS total_records,
    COUNTIF(quantity <= 0) AS invalid_quantity,
    COUNTIF(sales < 0) AS invalid_sales,
    COUNTIF(discount < 0 OR discount > 1) AS invalid_discount
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`;


-- 3. OVERALL KPIs
SELECT
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    AVG(discount) AS average_discount
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`;


-- 4. REGIONAL PERFORMANCE
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`
GROUP BY region
ORDER BY total_sales DESC;


-- 5. CATEGORY PERFORMANCE
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`
GROUP BY category
ORDER BY total_sales DESC;


-- 6. MONTHLY SALES TREND
SELECT
    DATE_TRUNC(date, MONTH) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`
GROUP BY month
ORDER BY month;


-- 7. TOP 10 PROFITABLE PRODUCTS
SELECT
    product,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    AVG(discount) AS average_discount
FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`
GROUP BY product
ORDER BY total_profit DESC
LIMIT 10;


-- 8. DISCOUNT VS PROFITABILITY
SELECT
    CASE
        WHEN discount = 0 THEN '0%'
        WHEN discount <= 0.10 THEN '1-10%'
        WHEN discount <= 0.20 THEN '11-20%'
        WHEN discount <= 0.30 THEN '21-30%'
        WHEN discount <= 0.40 THEN '31-40%'
        ELSE '41%+'
    END AS discount_range,

    COUNT(*) AS transactions,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(profit) AS average_profit

FROM `fluted-lambda-507018-p8.sales_dataset.sales_table`

GROUP BY discount_range
ORDER BY discount_range;

