<?php
/**
在一个脚本的全部作用域中都可用。 你不需要特别说明，就可以在函数及类中使用。
**/

//$GLOBALS 		是一个超级全局变量组,包含了全部变量的组合得到的数组。变量的名字就是数组的键。
$x = 75; 
$y = 25;
 
function addition() { 
    $GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y']; #z也是一$GLOBALS超级全局变量，同样在函数外可以访问
}
addition(); 
echo $z."\n"; 
// $_SERVER  :包含了诸信息(header)、路径(path)、及脚本位置(script locations)等内容的数组。
//数组中的项目由 Web 服务器创建。不能保证每个服务器都提供全部项目；
echo $_SERVER['PHP_SELF']."\n";		//当前执行脚本的文件名。如地址为 http://example.com/test.php/foo.bar 的脚本中使用 $_SERVER['PHP_SELF'] 将得到 /test.php/foo.bar。
echo $_SERVER['SERVER_NAME']."\n";
echo $_SERVER['HTTP_HOST']."\n";
echo $_SERVER['HTTP_REFERER']."\n";
echo $_SERVER['HTTP_USER_AGENT']."\n";
echo $_SERVER['SCRIPT_NAME']."\n";			//https://www.runoob.com/php/php-superglobals.html 咱们是还没有用到
// PHP $_REQUEST  用于收集HTML表单提交的数据。
<html>
<body>
 
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
Name: <input type="text" name="fname">
<input type="submit">
</form>
 
<?php 
$name = $_REQUEST['fname']; 
echo $name; 

?>
 
</body>
</html>

?>
