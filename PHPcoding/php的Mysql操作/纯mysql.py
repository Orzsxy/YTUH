# 创建数据库：
#	create DATABASE databasename;
#
# [root@host]# mysql -u root -p   
#	Enter password:******  # 登录后进入终端
#	mysql> create DATABASE databasename;
#root用户可以使用mysqladmin创建数据库:
# [root@host]# mysqladmin -u root -p create databasename
#	Enter password:******

# 删除库：
# drop database databasename;
# root用户：
# [root@host]# mysqladmin -u root -p drop databasename

#选择库：
# use databasename;

# 给表插入数据（如果主键不自增，需要指定主键字段）
#INSERT INTO table_name ( field1, field2,...fieldN )
#                       VALUES
#                       ( value1, value2,...valueN );

# WHERE字句：
# WHERE 可以运用于 DELETE 或者 UPDATE 命令
# WHERE子句默认不区分大小，使用：BINARY 来区分字段的大小写
#	 SELECT field1, field2,...fieldN FROM table_name1, table_name2...
#	 [WHERE condition1 [AND [OR]] condition2.....
#
# where：数据库中常用的是where关键字，用于在初始表中筛选查询。它是一个约束声明，用于约束数据，在返回结果集之前起作用。
# group by:对select查询出来的结果集按照某个字段或者表达式进行分组，获得一组组的集合，然后从每组中取出一个指定字段或者表达式的值。
# having：用于对where和group by查询出来的分组经行过滤，查出满足条件的分组结果。它是一个过滤声明，是在查询返回结果集以后对查询结果进行的过滤操作。
# 执行顺序:	select –>where –> group by–> having–>order by
 
# 更新: 
# UPDATE table_name SET field1=new-value1, field2=new-value2
# [WHERE Clause]
#
# UPDATE table_name SET field=REPLACE(field, 'old-string', 'new-string') 
# [WHERE Clause]
# 给已经存在的主键设置自增，如果不是主键还要为主键，因为自增只能用在主键,且为int型
# alter table tablename modify id int(长度)..属性  auto_increment;
# alter table tablename   auto_increment=10000; 

# 删除数据：
# DELETE FROM table_name [WHERE Clause]
# 不加WHERE子句就是删除整个表
# delete 是 DML(数据操纵语言) 语句，操作完以后如果没有不想提交事务还可以回滚，truncate 和 drop 是 DDL(数据定义语言) 语句，操作完马上生效，不能回滚，
# 速度上: drop>truncate>delete

# LIKE 子句,与 % _ [] 配合使用，不适使用的话相当于=
# %： *
#　_：表示任意单个字符。
# []: 其中的一个
# ^ ： 不是这些字符中的一个
# WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'

# UNION ：
# 连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据。
# SELECT expression1, expression2, ... expression_n
# FROM tables
# [WHERE conditions]
# UNION [ALL | DISTINCT]
# SELECT expression1, expression2, ... expression_n
# FROM tables
# [WHERE conditions];
# 
# expression1, expression2, ... expression_n: 要检索的列。
# tables: 要检索的数据表。
# WHERE conditions: 可选， 检索条件。
# DISTINCT: 可选，删除结果集中重复的数据。默认情况下 UNION 操作符已经删除了重复数据，所以 DISTINCT 修饰符对结果没啥影响！!!
# ALL: 可选，返回所有结果集，包含重复数据。


# ORDER BY 子句
# 设定你想按哪个字段哪种方式来进行排序
# SELECT field1, field2,...fieldN FROM table_name1, table_name2...
# ORDER BY field1 [ASC [DESC][默认 ASC]], [field2...] [ASC [DESC][默认 ASC]]
# 如果字符集采用的是 utf8(万国码)，需要先对字段进行转码然后排序：ORDER BY CONVERT(filed using gbk);


#  GROUP BY 语句
# 分组的列上可以使用 COUNT, SUM, AVG,等函数
# SELECT column_name, function(column_name)
# FROM table_name
# WHERE column_name operator value
# GROUP BY column_name;

# WITH ROLLUP 
# 实现在GROUP BY基础上再进行相同的统计（SUM,AVG,COUNT…）。
# mysql> SELECT name, SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
# +--------+--------------+
# | name   | singin_count |
# +--------+--------------+
# | 小丽 |            2 |
# | 小明 |            7 |
# | 小王 |            7 |
# | NULL   |           16 |
# +--------+--------------+
 #可以使用 coalesce 来设置一个可以取代 NUll 的名称，coalesce 语法：
# select coalesce(a,b,c);
# 参数说明：如果a==null,则选择b；如果b==null,则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（没意义）。
# 以下实例中如果名字为空我们使用总数代替：
# mysql> SELECT coalesce(name, '总数'), SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
#+--------------------------+--------------+
#| coalesce(name, '总数') | singin_count |
#+--------------------------+--------------+
#| 小丽                   |            2 |
#| 小明                   |            7 |
#| 小王                   |            7 |
#| 总数                   |           16 |
#+--------------------------+--------------+


# INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
# LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
# RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

# mysql> SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a INNER JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;
# mysql> SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a LEFT JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;

# mysql> SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a RIGHT JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;
#+-------------+-----------------+----------------+
#| a.runoob_id | a.runoob_author | b.runoob_count |
#+-------------+-----------------+----------------+
#| 1           | 菜鸟教程    | 10             |
#| 2           | 菜鸟教程    | 10             |
#| 3           | RUNOOB.COM      | 20             |
# | 4           | RUNOOB.COM      | 20             |
# | NULL        | NULL            | 22             |
# +-------------+-----------------+----------------+
# (上面a,b都是表的别名)

# NULL: 不能用 ==null !=null
# mysql> SELECT * FROM test_tbl WHERE count IS NULL;
# mysql> SELECT * from test_tbl WHERE count IS NOT NULL;


# 正则表达式  REGEXP:
# mysql> SELECT name FROM person_tbl WHERE name REGEXP '^st';name字段中以'st'为开头的所有数据
# mysql> SELECT name FROM person_tbl WHERE name REGEXP 'ok$';name字段中以'ok'为结尾的所有数据
# mysql> SELECT name FROM person_tbl WHERE name REGEXP 'mar';name字段中包含'mar'字符串的所有数据
# mysql> SELECT name FROM person_tbl WHERE name REGEXP '^[aeiou]|ok$';以元音字符开头或以'ok'字符串结尾的所有数据


#设置字段默认为0
#alter table wp_count modify times int(10) DEFAULT 0











SELECT * from runoob_tbl  WHERE runoob_author LIKE '%COM';
SELECT * from runoob_tbl ORDER BY submission_date ASC;


SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `employee_tbl`
-- ----------------------------
DROP TABLE IF EXISTS `employee_tbl`;
CREATE TABLE `employee_tbl` (
  `id` int(11) NOT NULL,
  `name` char(10) NOT NULL DEFAULT '',
  `date` datetime NOT NULL,
  `singin` tinyint(4) NOT NULL DEFAULT '0' COMMENT '登录次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- ----------------------------
--  Records of `employee_tbl`
-- ----------------------------
BEGIN;
INSERT INTO `employee_tbl` VALUES ('1', '小明', '2016-04-22 15:25:33', '1'), ('2', '小王', '2016-04-20 15:25:47', '3'), ('3', '小丽', '2016-04-19 15:26:02', '2'), ('4', '小王', '2016-04-07 15:26:14', '4'), ('5', '小明', '2016-04-11 15:26:40', '4'), ('6', '小明', '2016-04-04 15:26:54', '2');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

mysql> set names utf8;
mysql> SELECT * FROM employee_tbl;
+----+--------+---------------------+--------+
| id | name   | date                | singin |
+----+--------+---------------------+--------+
|  1 | 小明 | 2016-04-22 15:25:33 |      1 |
|  2 | 小王 | 2016-04-20 15:25:47 |      3 |
|  3 | 小丽 | 2016-04-19 15:26:02 |      2 |
|  4 | 小王 | 2016-04-07 15:26:14 |      4 |
|  5 | 小明 | 2016-04-11 15:26:40 |      4 |
|  6 | 小明 | 2016-04-04 15:26:54 |      2 |
+----+--------+---------------------+--------+

mysql> SELECT name, COUNT(*) FROM   employee_tbl GROUP BY name;
+--------+----------+
| name   | COUNT(*) |
+--------+----------+
| 小丽 |        1 |
| 小明 |        3 |
| 小王 |        2 |
+--------+----------+

