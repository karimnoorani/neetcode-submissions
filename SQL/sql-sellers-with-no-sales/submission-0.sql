-- Write your query below

SELECT seller_name
FROM seller
WHERE NOT EXISTS (
    SELECT 1
    FROM orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020 AND orders.seller_id = seller.seller_id
)
ORDER BY seller_name;