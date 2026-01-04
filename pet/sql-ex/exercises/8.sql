SELECT DISTINCT p.maker
FROM Product p
WHERE p.type = 'PC'
  AND NOT EXISTS (
      SELECT 1
      FROM Product x
      WHERE x.maker = p.maker
        AND x.type = 'Laptop'
);