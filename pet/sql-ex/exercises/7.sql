SELECT DISTINCT p.model, x.price
FROM Product p
JOIN (
    SELECT model, price FROM PC
    UNION ALL
    SELECT model, price FROM Laptop
    UNION ALL
    SELECT model, price FROM Printer
) x ON x.model = p.model
WHERE p.maker = 'B'
