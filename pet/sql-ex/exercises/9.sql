SELECT DISTINCT p.maker
FROM Product as p
JOIN PC as pc ON p.model = pc.model
WHERE pc.speed >= 450
