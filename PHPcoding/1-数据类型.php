<!DOCTYPE html>
<html>
<body>
<h1> My first PHP page</h1>
<?php
echo "Hello World!";
?>
</body>
</html>

<?php
header("content-type:text/html;charset=utf-8");         //设置编码
?>

<?php
echo "PHP也有对应的四种变量:
			local
			global
			static
			parameter\n";
$x = 1;	//全局变量
$y = 2;
$z = $x + $y;
function Mytest()
{
	$k = 10; //局部变量
	echo "<p> 变量函数内部变量:<p>\n";
	echo "变量的x 值：$x"; // $x 变量在函数外定义，无法在函数内使用，如果要在一个函数中访问一个全局变量，需要使用 global 关键字。
	echo "<br>";
	echo "变量k为：$k";
}
Mytest();
echo "<p>测试函数外变量：<p>";
echo "变量x为：$x"; //不能输出 $y 的值，因为 $y 变量在函数中定义，属于局部变量。
echo "<br>";
echo "变量 y 值：$k";
//可以在不同函数中使用相同的变量名称，因为这些函数内定义的变量名是局部变量，只作用于该函数内
$x = 10;
$y = 15;
function Mytest1(){
	global $x,$y; //函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字
	echo "函数内调用函数外定义的全局变量:$x,$y";
	$GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y']; //PHP 将所有全局变量存储在一个名为 $GLOBALS[index] 的数组中。 index 保存变量的名称。这个数组可以在函数内部访问，也可以直接用来更新全局变量。
}
Mytest1();
/*
echo 和 print 区别:
echo - 可以输出多个字符串,使用的时候： echo 或 echo()。
print - 只允许输出一个字符串，返回值为 1
提示：echo 输出的速度比 print 快， echo 没有返回值，print有返回值1。
*/
$cars=array("Volvo","BMW","Toyota");
echo "我车的品牌是 {$cars[0]}<br>";
print "\n我车的品牌是 {$cars[0]}\n";

$name="runoob";
$a= <<<EOF
        "abc"$name
        123
        这之间的变量可以被正常解析，但是函数则不可以
EOF;
// EOF结束需要独立一行且前后不能空格.内容需加引号时（单引号或双引号），不需要加转义符
echo $a;
$name="变量会被解析";
$a=<<<EOF
$name<br><a>html格式会被解析</a><br/>双引号和Html格式外的其他内容都不会被解析
"双引号外所有被排列好的格式都会被保留"
"但是双引号内会保留转义符的转义效果,比如table:\t和换行：\n下一行"
EOF;
//EOF 中是会解析 html 格式内容的，并且在双引号内的内容也有转义效果。
echo $a;
?>


