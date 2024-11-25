
# SQL Functions Explained

This document provides a description and examples of various SQL functions.

---

## DISTINCT
**Description:** Returns unique values in the result set.
**Example:**
```sql
SELECT DISTINCT Country FROM Customers;
```

---

## UNION
**Description:** Combines the results of two queries, removing duplicates.
**Example:**
```sql
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers;
```

---

## INTERSECT
**Description:** Returns the common records from two queries.
**Example:**
```sql
SELECT City FROM Customers
INTERSECT
SELECT City FROM Suppliers;
```

---

## EXISTS
**Description:** Checks if a subquery returns any records.
**Example:**
```sql
SELECT Name FROM Employees WHERE EXISTS (
    SELECT * FROM Orders WHERE Employees.ID = Orders.EmployeeID
);
```

---

## NOT IN
**Description:** Excludes rows that match values in a subquery or list.
**Example:**
```sql
SELECT Name FROM Employees WHERE ID NOT IN (SELECT EmployeeID FROM Orders);
```

---

## LIKE
**Description:** Matches patterns in strings using `%` and `_`.
**Example:**
```sql
SELECT * FROM Products WHERE ProductName LIKE '%Apple%';
```

---

## ALL / ANY
**Description:** Compares a value to all or any values in a list or subquery.
**Example:**
```sql
SELECT ProductName FROM Products WHERE Price > ALL (SELECT Price FROM Discounts);
```

---

## COALESCE
**Description:** Returns the first non-null value in a list.
**Example:**
```sql
SELECT COALESCE(NULL, NULL, 'DefaultValue');
```

---

## CAST
**Description:** Converts a value to a specified data type.
**Example:**
```sql
SELECT CAST(123.45 AS INT);
```

---

## IIF
**Description:** A shorthand for `CASE` to return conditional results.
**Example:**
```sql
SELECT IIF(Salary > 50000, 'High', 'Low') AS SalaryCategory FROM Employees;
```

---

## ISNULL
**Description:** Replaces null values with a specified value.
**Example:**
```sql
SELECT ISNULL(Commission, 0) FROM Sales;
```

---

## FULL JOIN
**Description:** Combines all rows from both tables, filling NULLs for missing matches.
**Example:**
```sql
SELECT * FROM TableA
FULL JOIN TableB ON TableA.ID = TableB.ID;
```

---

## CROSS JOIN
**Description:** Produces a Cartesian product of two tables.
**Example:**
```sql
SELECT * FROM Products CROSS JOIN Categories;
```

---

## LEN
**Description:** Returns the length of a string.
**Example:**
```sql
SELECT LEN(ProductName) FROM Products;
```

---

## SUBSTRING
**Description:** Extracts a portion of a string.
**Example:**
```sql
SELECT SUBSTRING(ProductName, 1, 5) FROM Products;
```

---

## CHARINDEX
**Description:** Returns the starting position of a substring in a string.
**Example:**
```sql
SELECT CHARINDEX('Apple', ProductName) FROM Products;
```

---

## PARTITION
**Description:** Divides the result set into partitions.
**Example:**
```sql
SELECT ProductID, RANK() OVER (PARTITION BY CategoryID ORDER BY Price) AS Rank FROM Products;
```

---

## TIES (Task 76)
**Description:** Ensures ties in a ranked query are included when using `TOP`.
**Example:**
```sql
SELECT TOP (5) WITH TIES * FROM Products ORDER BY Price DESC;
```

---

## CONVERT (Task 78)
**Description:** Converts data from one type to another with formatting options.
**Example:**
```sql
SELECT CONVERT(VARCHAR, GETDATE(), 101);
```

---

## DESC
**Description:** Sorts results in descending order.
**Example:**
```sql
SELECT * FROM Products ORDER BY Price DESC;
```

---

## ROW_NUMBER()
**Description:** Assigns a unique number to each row based on a specified order.
**Example:**
```sql
SELECT ROW_NUMBER() OVER (ORDER BY Price) AS RowNum, ProductName FROM Products;
```

---

## LEAD
**Description:** Returns the value of the next row in the result set.
**Example:**
```sql
SELECT ProductID, LEAD(Price) OVER (ORDER BY Price) AS NextPrice FROM Products;
```

---

## LAG
**Description:** Returns the value of the previous row in the result set.
**Example:**
```sql
SELECT ProductID, LAG(Price) OVER (ORDER BY Price) AS PrevPrice FROM Products;
```

---

## CASE WHEN ... THEN ... ELSE ... END
**Description:** Executes conditional logic in queries.
**Example:**
```sql
SELECT ProductName, 
       CASE 
           WHEN Price > 100 THEN 'Expensive'
           ELSE 'Affordable'
       END AS PriceCategory
FROM Products;
```

---

## Additional Examples
For more advanced examples, refer to tasks such as 75, 76, and 78.

