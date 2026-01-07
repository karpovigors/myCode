SELECT s.class, s.name, c.country
FROM Ships AS s
JOIN Classes AS c ON c.class = s.class
WHERE c.numGuns >= 10
