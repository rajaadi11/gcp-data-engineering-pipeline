CREATE OR REPLACE VIEW
`fluted-lambda-507018-p8.sales_dataset.sales_summary`
AS

SELECT
    COUNT(*) AS total_line_items,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    AVG(sales) AS average_line_value,
    AVG(discount) AS average_discount,
    SAFE_DIVIDE(SUM(profit), SUM(sales)) AS profit_margin

FROM
    `fluted-lambda-507018-p8.sales_dataset.sales_table`;