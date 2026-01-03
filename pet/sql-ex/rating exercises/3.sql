SELECT maker,
       IIF(pc > 0, 'yes(' + CAST(pc_cnt AS VARCHAR) + ')', 'no') AS pc,
       IIF(laptop > 0, 'yes(' + CAST(laptop_cnt AS VARCHAR) + ')', 'no') AS laptop,
       IIF(printer > 0, 'yes(' + CAST(printer_cnt AS VARCHAR) + ')', 'no') AS printer
FROM (
    SELECT tab.maker,
           tab.pc,
           (SELECT COUNT(DISTINCT pc.model)
            FROM PRODUCT pr
            JOIN PC ON pc.model = pr.model
            WHERE pr.maker = tab.maker) AS pc_cnt,
           tab.laptop,
           (SELECT COUNT(DISTINCT l.model)
            FROM PRODUCT pr
            JOIN LAPTOP l ON l.model = pr.model
            WHERE pr.maker = tab.maker) AS laptop_cnt,
           tab.printer,
           (SELECT COUNT(DISTINCT p.model)
            FROM PRODUCT pr
            JOIN PRINTER p ON p.model = pr.model
            WHERE pr.maker = tab.maker) AS printer_cnt
    FROM (
        SELECT DISTINCT prod.maker,
               (SELECT COUNT(*)
                FROM PRODUCT pr
                WHERE pr.maker = prod.maker AND pr.type = 'pc') AS pc,
               (SELECT COUNT(*)
                FROM PRODUCT pr
                WHERE pr.maker = prod.maker AND pr.type = 'laptop') AS laptop,
               (SELECT COUNT(*)
                FROM PRODUCT pr
                WHERE pr.maker = prod.maker AND pr.type = 'printer') AS printer
        FROM PRODUCT prod
    ) tab
) tab
