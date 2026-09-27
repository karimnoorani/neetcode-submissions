-- Write your query below

SELECT users.name, COALESCE(SUM(rides.distance), 0) as travelled_distance
FROM users
LEFT JOIN rides on users.id = rides.user_id
GROUP BY users.name
ORDER BY travelled_distance DESC, name ASC;