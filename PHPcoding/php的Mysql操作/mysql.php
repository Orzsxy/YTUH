<?php 
#连接数据库：
#	成功链接到 MySQL 后返回连接标识，失败返回 FALSE 
#	mysqli_connect(host, username, password, dbname, port, socket);

# 断开连接：
# 通常不需要使用mysqli_close()，因为已打开的非持久连接会在脚本执行完毕后自动关闭
#	bool mysqli_close ( mysqli $link )；

# 创建数据库、删库、创建表、删除表、插入数据、：	
#	mysqli_query(connection,query,resultmode);
# 	connection 必需。规定要使用的 MySQL 连接。
#	query		 必需，规定查询字符串。
# 	resultmode 可选。一个常量。可以是下列值中的任意一个：MYSQLI_USE_RESULT（检索大量数据，请使用这个） MYSQLI_STORE_RESULT（默认）

# 选择数据库:
#	mysqli_select_db(connection,dbname);
# 	connection	必需。规定要使用的 MySQL 连接。
#	dbname	必需，规定要使用的默认数据库。

# 获取读取到的数据库内的数据：
# 返回的都是数组
# mysqli_fetch_array($obj, MYSQLI_ASSOC)   MYSQLI_ASSOC是用数据表字段名做索引
# mysqli_fetch_array($obj, MYSQLI_NUM)     MYSQLI_NUM 用0,1,2... 做索引
# mysqli_fetch_assoc($obj) 是用字段名做索引

# 释放游标内存：在执行完 SELECT 语句后，释放游标内存
# mysqli_free_result($obj);


	#连接服务
	$dbhost = 'localhost';  // mysql服务器主机地址
	$dbuser = 'root';            // mysql用户名
	$dbpass = '123456';          // mysql用户名密码
	$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
	if(! $conn )
	{
	    die('Could not connect: ' . mysqli_error());
	}
	echo '数据库连接成功！<br/>';
	#创库
	$sql = 'CREATE DATABASE databasename';
	$retval = mysqli_query($conn,$sql );
	if(! $retval )
	{
	    die('创建数据库失败: ' . mysqli_error($conn));
	}
	echo "数据库创建成功\n";

	$sql = 'SELECT runoob_id, runoob_title, 
        runoob_author, submission_date
        FROM runoob_tbl';

	# 设置编码，防止中文乱码
	mysqli_query($conn , "set names utf8");
	#选择数据库（直接指定，没有返回结果)：
	mysqli_select_db($conn, 'databasename' );
	# 查询（先选择数据库）
	$retval = mysqli_query( $conn, $sql );
	# 获取数据库数据 方式1
	while($row = mysqli_fetch_array($retval, MYSQLI_ASSOC)){
    echo "<tr><td> {$row['runoob_id']}</td> ".
         "<td>{$row['runoob_title']} </td> ".
         "<td>{$row['runoob_author']} </td> ".
         "<td>{$row['submission_date']} </td> ".
         "</tr>";
	}
	# 获取数据库数据 方式2
	while($row = mysqli_fetch_array($retval, MYSQLI_NUM)){
    echo "<tr><td> {$row[0]}</td> ".
         "<td>{$row[1]} </td> ".
         "<td>{$row[2]} </td> ".
         "<td>{$row[3]} </td> ".
         "</tr>";
	}
	# 获取数据库数据 方式3
	while($row = mysqli_fetch_assoc($retval)){
    echo "<tr><td> {$row['runoob_id']}</td> ".
         "<td>{$row['runoob_title']} </td> ".
         "<td>{$row['runoob_author']} </td> ".
         "<td>{$row['submission_date']} </td> ".
         "</tr>";
	}
	# 执行完 SELECT 语句后，释放游标内存内存,别的不用释放
	mysqli_free_result($retval);
	# 关闭连接
	mysqli_close($conn);



?>