CREATE OR REPLACE VIEW
`fluted-lambda-507018-p8.sales_dataset.top_products`
AS

SELECT
    product,
    total_line_items,
    total_orders,
    total_sales,
    total_profit,
    total_quantity,
    average_discount,
    profit_margin

FROM
    `fluted-lambda-507018-p8.sales_dataset.product_performance`

ORDER BY
    total_profit DESC
LIMIT 20;