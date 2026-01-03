SELECT DISTINCT k.model
FROM
    (SELECT prod.maker, l.hd, l.screen
     FROM PRODUCT prod
     JOIN LAPTOP l ON l.model = prod.model) d,
    (SELECT prod.maker, pc.speed, pc.price
     FROM PRODUCT prod
     JOIN PC pc ON pc.model = prod.model) m,
    (SELECT color, type, price
     FROM PRINTER) t,
    (SELECT model, color, type, price
     FROM PRINTER) v,
    (SELECT model, ram, screen
     FROM LAPTOP) o,
    (SELECT model, speed, ram, hd, price
     FROM PC) k
WHERE
    d.maker = m.maker
    AND t.type <> v.type
    AND t.color = v.color
    AND d.screen = o.screen + 3
    AND m.price = 4 * t.price
    AND STUFF(v.model, 3, 1, '') = STUFF(o.model, 3, 1, '')
    AND k.speed = m.speed
    AND k.hd = d.hd
    AND k.ram = o.ram
    AND k.price = v.price
