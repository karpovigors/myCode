WITH TAB AS (
    SELECT DISTINCT
           YEAR(DATE)  AS YR,
           MONTH(DATE) AS MNTH,
           DATEFROMPARTS(YEAR(DATE), MONTH(DATE), 1) AS FST,
           DATEADD(DD, -1,
                   DATEADD(MM, 1, DATEFROMPARTS(YEAR(DATE), MONTH(DATE), 1))) AS LST
    FROM BATTLES
),
CTE AS (
    SELECT
        YR,
        MNTH,
        FST AS DATE
    FROM TAB
    UNION ALL
    SELECT
        A.YR,
        A.MNTH,
        DATEADD(DD, 1, A.DATE)
    FROM CTE A
    WHERE DATE < (
        SELECT LST
        FROM TAB T
        WHERE T.YR = A.YR
          AND T.MNTH = A.MNTH
    )
),
TOTAL AS (
    SELECT
        T.YR,
        T.MNTH,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 0) AS MON,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 1) AS TUE,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 2) AS WED,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 3) AS THU,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 4) AS FRI,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 5) AS SAT,
        (SELECT COUNT(*)
         FROM CTE C
         WHERE C.YR = T.YR
           AND C.MNTH = T.MNTH
           AND (@@DATEFIRST + DATEPART(DW, C.DATE) - 2) % 7 = 6) AS SUN
    FROM TAB T
)
SELECT
    SUBSTRING(CAST(DATEFROMPARTS(YR, MNTH, 1) AS VARCHAR), 1, 7) AS M,
    MON, TUE, WED, THU, FRI, SAT, SUN
FROM TOTAL;
