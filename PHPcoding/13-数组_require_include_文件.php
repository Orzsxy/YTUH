<?php
// 二维数组:
	$vars = array(
			array(1,2,3),
			array('A','B','C'),
			array('svd','sfvbdf','hygt')
	);
//bool print_r ( mixed $expression [, bool $return ] )
//$return: 可选，如果为 true 则不输出结果，而是将结果赋值给一个变量，false 则直接输出结果、默认。
	print"<pre>";
		print_r($vars);//打印变量，以更容易理解的形式展示
	print"</pre>";
//二维数组内数组还可以是一个数组：
$sites = array(
    "runoob"=>array(
        "菜鸟",
        "http://www.runoob.com"
    ),
    "google"=>array(
        "Google 搜索",
        "http://www.google.com"
    ),
    "taobao"=>array(
        "淘宝",
        "http://www.taobao.com"
    )
);
print("<pre>"); // 格式化输出数组
print_r($sites);
print("</pre>");
echo "键:".$sites['runoob'][0]." 对应的值:".$sites['runoob'][1]."<br>";
// data()格式化时间： string date ( string $format [, int $timestamp ] ),$timestamp时间戳，可选
// 更多的时间信息 ：https://www.runoob.com/php/php-date.html 
echo date("Y/m/d",131400) . "<br>";
echo date("Y.m.d") . "<br>";
echo date("Y-m-d");
// requre include:在服务器执行当前PHP文件之前在该文件中插入一个文件的内容
/*
include 和 require 除了处理错误的方式不同之外，在其他方面都是相同的：
require 生成一个致命错误（E_COMPILE_ERROR），在错误发生后脚本会停止执行。 
include 生成一个警告（E_WARNING），在错误发生后脚本会继续执行。
假设有一个标准的页头文件，名为 "header.php"。需在页面中引用这个页头文件，
<?php include 'header.php'; ?>
<h1>欢迎来到我的主页!</h1>
<p>一些文本。</p>
*/
/*文件:
r	只读。在文件的开头开始。
r+	读/写。在文件的开头开始。
w	只写。打开并清空文件的内容；如果文件不存在，则创建新文件。
w+	读/写。打开并清空文件的内容；如果文件不存在，则创建新文件。
a	追加。打开并向文件末尾进行写操作，如果文件不存在，则创建新文件。
a+	读/追加。通过向文件末尾写内容，来保持文件内容。
x	只写。创建新文件。如果文件已存在，则返回 FALSE 和一个错误。
x+	读/写。创建新文件。如果文件已存在，则返回 FALSE 和一个错误。
*/
//如果 fopen() 不能打开文件使用 or exit输出错误信息：
// $file=fopen("welcome.txt","r") or exit("Unable to open file!");
//关闭文件：fclose($file);
//检测是否到了文件末尾（在循环遍历未知长度的数据时很有用)：feof()
//从文件中逐行读取文件:fgets() 
/*逐行读取文件的实例:
	$file = fopen("welcome.txt", "r") or exit("无法打开文件!");
	while(!feof($file)){
    echo fgets($file). "<br>";
	}
	fclose($file);
每次读取一个字符:
	while (!feof($file)){
    echo fgetc($file);
	}
	fclose($file);
*/

?>