/*
Схема БД состоит из четырех таблиц:
Product(maker, model, type)
PC(code, model, speed, ram, hd, cd, price)
Laptop(code, model, speed, ram, hd, price, screen)
Printer(code, model, color, type, price)

Описание таблиц:
Таблица Product представляет производителя (maker), номер модели (model) и 
тип ('PC' - ПК, 'Laptop' - ПК-блокнот или 'Printer' - принтер). 

Предполагается, что номера моделей в таблице Product уникальны для всех производителей и типов продуктов. 

В таблице PC для каждого ПК, однозначно определяемого уникальным кодом – code, 
указаны модель – model (внешний ключ к таблице Product), 
скорость - speed (процессора в мегагерцах), 
объем памяти - ram (в мегабайтах), 
размер диска - hd (в гигабайтах), 
скорость считывающего устройства - cd (например, '4x') 
и цена - price (в долларах). 

Таблица Laptop аналогична таблице РС за исключением того, что вместо скорости CD содержит размер экрана -screen (в дюймах). 

В таблице Printer для каждой модели принтера указывается, является ли он цветным - color ('y', если цветной), 
тип принтера - type (лазерный – 'Laser', струйный – 'Jet' или матричный – 'Matrix') и цена - price.

*/


/*
1. Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 долларов.
Вывести: model, speed, hd.
*/
SELECT 
    pc.model,
    pc.speed,
    pc.hd
FROM 
    PC pc
WHERE 
    pc.price < 500;

/*
2. Найдите производителей принтеров. Вывести: maker.
*/
SELECT DISTINCT 
    p.maker
FROM 
    Product p
WHERE 
    p.type = 'Printer';

/*
3. Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 долларов.
Вывести: model, ram, screen.
*/
SELECT 
    l.model,
    l.ram,
    l.screen
FROM 
    Laptop l
WHERE 
    l.price > 1000;

/*
4. Найдите все записи таблицы Printer для цветных принтеров.
*/
SELECT 
    *
FROM 
    Printer pr
WHERE 
    pr.color = 'y';

/*
5. Найдите номер модели, скорость и размер жесткого диска ПК, имеющих CD 12x или 24x, и цену менее 600 долларов.
Вывести: model, speed, hd.
*/
SELECT 
    pc.model,
    pc.speed,
    pc.hd
FROM 
    PC pc
WHERE 
    (pc.cd = '12x' OR pc.cd = '24x') 
    AND pc.price < 600;

/*
6. Для каждого производителя, выпускающего ПК-блокноты с объемом жесткого диска не менее 10 ГБ,
найдите скорости таких ПК-блокнотов. 
Вывести: maker, speed.
*/
SELECT DISTINCT 
    p.maker,
    l.speed
FROM 
    Product p
JOIN 
    Laptop l 
    ON p.model = l.model
WHERE 
    l.hd >= 10;

/*
7. Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B.
Вывести: model, price.
*/
SELECT 
    p.model,
    pc.price
FROM 
    Product p
JOIN 
    PC pc 
    ON p.model = pc.model
WHERE 
    p.maker = 'B'

UNION

SELECT 
    p.model,
    l.price
FROM 
    Product p
JOIN 
    Laptop l 
    ON p.model = l.model
WHERE 
    p.maker = 'B'

UNION

SELECT 
    p.model,
    pr.price
FROM 
    Product p
JOIN 
    Printer pr 
    ON p.model = pr.model
WHERE 
    p.maker = 'B';

/*
8. Найдите производителя, выпускающего ПК, но не ПК-блокноты.
*/
SELECT DISTINCT 
    p.maker
FROM 
    Product p
WHERE 
    p.type = 'PC'
    AND p.maker NOT IN (
        SELECT DISTINCT 
            p2.maker
        FROM 
            Product p2
        WHERE 
            p2.type = 'Laptop'
    );

/*
9. Найдите производителей ПК с процессором не менее 450 МГц.
Вывести: maker.
*/
SELECT DISTINCT 
    p.maker
FROM 
    Product p
JOIN 
    PC pc 
    ON p.model = pc.model
WHERE 
    pc.speed >= 450;

/*
10. Найдите модели принтеров, имеющих самую высокую цену. 
Вывести: model, price
*/
SELECT
    model, price
FROM
    Printer
WHERE 
    price = (
        SELECT 
            MAX(price)
        FROM 
            Printer
    )
