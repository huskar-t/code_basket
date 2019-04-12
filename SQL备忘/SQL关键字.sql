-- SQL JOIN
-- JOIN/ INNER JOIN: 如果表中有至少一个匹配，则返回行(同时满足返回)
-- LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行(返回左表)
-- RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行(返回右表)
-- FULL JOIN: 只要其中一个表中存在匹配，就返回行(返回全部) mysql不支持

SELECT p.LastName, p.FirstName, o.OrderNo
FROM Npersons as p
INNER JOIN Norders as o
ON p.Id_P = o.Id_P
ORDER BY p.LastName

SELECT p.LastName, p.FirstName, o.OrderNo
FROM Npersons as p
LEFT JOIN Norders as o
ON p.Id_P = o.Id_P
ORDER BY p.LastName

SELECT p.LastName, p.FirstName, o.OrderNo
FROM Npersons as p
RIGHT JOIN Norders as o
ON p.Id_P = o.Id_P
ORDER BY p.LastName
-- mysql不支持，我们可以使用union来达到目的
SELECT p.LastName, p.FirstName, o.OrderNo
FROM Npersons as p
FULL JOIN Norders as o
ON p.Id_P = o.Id_P
ORDER BY p.LastName

-- union实现fulljoin
select * FROM 
(SELECT p.LastName, p.FirstName, o.OrderNo
FROM Npersons as p
LEFT JOIN Norders as o
ON p.Id_P = o.Id_P
UNION
SELECT p.LastName, p.FirstName, o.OrderNo
FROM Npersons as p
RIGHT JOIN Norders as o
ON p.Id_P = o.Id_P) as a
ORDER BY a.LastName

-- UNION 操作符(去重)
-- SELECT column_name(s) FROM table_name1
-- UNION
-- SELECT column_name(s) FROM table_name2

-- UNIONALL 操作符(不去重)
-- SELECT column_name(s) FROM table_name1
-- UNION ALL
-- SELECT column_name(s) FROM table_name2

-- IS NULL
-- IS NOT NULL

-- GROUP BY 语句
-- 按照customer字段计算sum(OrderPrice)
SELECT Customer,SUM(OrderPrice) FROM Morders
GROUP BY Customer
-- 不使用groupby会使所有sum计算所有数据
SELECT Customer,SUM(OrderPrice) FROM Morders

-- 多列orderby
-- 同时按照Customer,OrderDate分组
SELECT Customer,OrderDate,SUM(OrderPrice) FROM Morders
GROUP BY Customer,OrderDate

-- HAVING 子句
-- 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。
SELECT Customer,SUM(OrderPrice) FROM Morders
GROUP BY Customer
HAVING SUM(OrderPrice)<2000