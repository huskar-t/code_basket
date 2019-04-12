-- 返回条数
-- limit 数量
-- limit 起始数量，返回数量
select * from persons LIMIT 1,3;

-- LIKE 操作符
-- SELECT column_name(s)
-- FROM table_name
-- WHERE column_name LIKE pattern
select * from persons where LastName LIKE "B%";
-- not like 不包含
select * from persons where LastName NOT LIKE "B%";

-- 通配符
-- %	替代一个或多个字符
-- _	仅替代一个字符
-- [charlist]	字符列中的任何单一字符
-- [^charlist]
-- 或者
-- [!charlist]
-- 不在字符列中的任何单一字符

-- 下面的这个写法在mysql不支持
SELECT * FROM Persons WHERE City LIKE "[ALN]%";
-- mysql中要用正则来使用[charlist]
SELECT * FROM Persons WHERE City REGEXP "[ALN]*";

-- IN 操作符
-- SELECT column_name(s)
-- FROM table_name
-- WHERE column_name IN (value1,value2,...)
SELECT * from persons WHERE City in ("London","Beijing")

-- BETWEEN 操作符
-- SELECT column_name(s)
-- FROM table_name
-- WHERE column_name
-- BETWEEN value1 AND value2

-- 不同数据库对between and 操作不同，有可能不包含两个边界
-- 使用之前先测试
-- 如需以 字母 顺序显示介于 "Adams"和 "Carter"之间的人，请使用下面的 SQL：
SELECT * FROM Persons
WHERE LastName
BETWEEN 'Adams' AND 'Carter';

-- NOT BETWEEN
SELECT * FROM Persons
WHERE LastName
NOT BETWEEN 'Adams' AND 'Carter';

-- Alias（别名）
-- SELECT column_name(s)
-- FROM table_name
-- AS alias_name
SELECT p.City from persons as p where id = 20;

