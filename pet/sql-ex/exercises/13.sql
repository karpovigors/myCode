SELECT AVG(pc.speed)
FROM PC AS pc
JOIN Product AS p
ON pc.model = p.model
WHERE p.maker = 'A'
