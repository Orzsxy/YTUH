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
# PHP注释 // /**/ # 都有效，从c c++ shell 中借用的
# 不区分大小写的关键字 NULL 用于没有定义值的情况。
FUNCTION T(){  //函数名、函数关键字、不区分大小写
	echo "不区分大小写";
}
t();
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
/*******************获取数据类型*/
$x = 12;
var_dump($x);
echo "<br>";
$x = 0x110;
var_dump($x);
$x = 0222;
var_dump($x);
$x = true;
// var_dump（$x); Error 因为布尔类型不是默认有的数据类型，但是可以判断使用
$x = array("volvo",2,1+4);
var_dump($x);
// 类对象
class Car{
	var $color;
	function __construct($color = "green"){
		$this -> $color = $color;
	}
	function get_color(){
		return $this->color;
	}
}
function prints_vars($c){
	foreach (get_object_vars($c) as $key => $var){
		//echo "\tkey:$key "."var=:$var\n";
		echo "\t$key = $var\n";
	}
}
$object = new car("white");
echo "attriubut object:\n";
prints_vars($object);
// foreach
$a = array('Tom','Mary','Peter','Jack');
foreach ($a as $value) {
  echo $value."<br>";
}
foreach ($a as $key => $value) {
  echo $key.','.$value."<br>";
}
// null NULL
$x =null;
echo "\n";
var_dump($x);
/***
类型比较：
松散比较：使用两个等号 == 比较，只比较值，不比较类型。
严格比较：用三个等号 === 比较，除了比较值，也比较类型。
// == 下 0 null false 的值都相同 
**/
if(42 == "42"){ //
	echo "1值相等";
}
if(42 ==="42"){ // Perl没有保留 判断数据类型的类型
	echo '2值相等';
}
print "\n 0 == false: ";var_dump(0 == false);
echo '0 ===false: ';
var_dump(0 === false);
echo PHP_EOL; // 也是一个换行，兼容的平台更大 
echo '0 ==null:'; var_dump(0==null);
/***
常量 (c++中const) 
bool define(string $name,$value [, bool $case_insensitive = false ])
name：必选参数，常量名称，即标志符。
value：必选参数，常量的值。
case_insensitive ：可选参数，如果设置为 TRUE，该常量则大小写不敏感。默认是大小写敏感的
 常量名不需要加 $ 修饰符 .在整个脚本中都可以使用
**/ 
define("ABC","个人博客:byteuler.cn");
echo ABC;
define("ABC","个人博客:byteuler.cn",true);
print "\n".ABC;
// 得到字符长度：
echo "\n".strlen("byteuler.cn");
// 换行
echo '<br>';  
// PHP7+ 版本新增整除运算符 intdiv()
echo "\n".  intdiv(7,2);
// a .= b 等价于 a = a.b
// 保留有单目运算符 py没有。 算数比较运算符和c一样，逻辑比较运算符和c也一样都有： and or  xor 
/***
PHP数组运算符:
+   两个数组的并集
==  相等
=== 恒等

!=
<>  这两个都是不相等

!== 不恒等
保有三目运算符： (expr1) ? (expr2) : (expr3) PHP 5.3 起，可以省略三元运算符中间那部分。
表达式 expr1 ?: expr3 在 expr1 求值为 TRUE 时返回 expr1，否则返回 expr3。
PHP7+ 版本多了一个 NULL 合并运算符 ??。 也就是不成立的意思
	$username = $_GET['user'] ?? 'nobody'; 如果 $_GET['user'] 不存在返回 'nobody'，否则返回 $_GET['user'] 的值
**/
//组合比较符(PHP7+)		<=>
$c = $a <=> $b;
echo $c;
/*
如果 $a > $b, 则 $c 的值为 1。
如果 $a == $b, 则 $c 的值为 0。
如果 $a < $b, 则 $c 的值为 -1。
*/
// 可以使用c++中对象改变优先级
// if ... elseif ... 和c++中一样
// switch(){ case .. : break; default:} 结构和c++相同

/***
数组:
普通数组：相当于c中的一样；
关联数组：和perl中的hash一样；
多维数组：
**/
//普通数组 
$array = array('A','B','C',1,2,3,1+3);
echo count($array)."\n"; //获取数组长度
$len = count($array);
for($i=0;$i<$len;++$i){
	echo $array[$i]."\n";
}
//关联数组
$hs = array("Perter" => "35","a"=>0,"Ben"=> 35,"JJ"=>1-1,"AA"=>35,"b"=>35);
echo $hs["Perter"].' '.$hs["Ben"].' '.$hs["JJ"]."\n";
//遍历关联数组
foreach($hs as $key => $value){
	echo "key:".$key." ".$value."\n";
}
/*应该有方法获取关联数组所有的键 和 值的集合
$keys = array_keys($hs);
$len = strlen($keys);
for($i =0;$i<array_keys($hs);++$i){
	printf("%s\n",$hs[$i]);
}
*/
/***
对数组的排序：
sort()  和c same
rsort() 降序
asort() 用在关联数组中，根据数组的值，升序排列。要是有多个值相同？？？(按照键在原先数组出现的顺序排列？
keys()  				根据数组的键，升序排列。
**/
asort($hs);
foreach($hs as $key => $value){
	echo "key:".$key." ".$value."\n";
}
?>