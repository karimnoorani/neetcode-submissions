-- Write your query below


SELECT name
FROM sales_person s
WHERE NOT EXISTS(
    SELECT 1
    FROM orders o
    JOIN company c on c.com_id = o.com_id
    WHERE s.sales_id = o.sales_id AND c.name = 'CRIMSON'
);
