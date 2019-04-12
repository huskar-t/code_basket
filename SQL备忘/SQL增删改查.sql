-- 查询全部
SELECT * from persons;

-- 查询不重复值
-- SELECT DISTINCT 列名称 FROM 表名称
SELECT DISTINCT company FROM Orders;

-- 排序order by
SELECT company,ordernumber from orders ORDER BY company;
-- 以字母顺序显示公司名称（Company），并以数字顺序显示顺序号（OrderNumber）：
SELECT company,ordernumber from orders ORDER BY company,ordernumber;
-- 以字母顺序显示公司名称（Company），并以数字逆序显示顺序号（OrderNumber）：
SELECT company,ordernumber from orders ORDER BY company,ordernumber DESC;

-- INSERT INTO 语句
-- INSERT INTO 表名称 VALUES (值1, 值2,....)
-- 我们也可以指定所要插入数据的列：
-- INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
INSERT INTO persons VALUES(20,"Gates","Bill","xuanwumen 10","Beijing");
INSERT INTO Persons (LastName, Address) VALUES ('Wilson', 'Champs-Elysees');

-- Update 语句
-- UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
update persons set FirstName = "new" where LastName = "Bush";
-- 更新多个字段
update persons set FirstName = "news", City = "Nanjing" where LastName = "Bush" ;

-- DELETE 语句
-- DELETE FROM 表名称 WHERE 列名称 = 值
DELETE from persons where LastName = "Wilson";
-- 删除所有行
DELETE from persons;
-- 或
delete * from persons;