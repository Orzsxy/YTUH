<?php
/*记录一些遇到的一些库函数*/
/*isset() 函数:
	检测变量是否已设置并且非 NULL。
unset() 可以释放一个变量，释放后再用isset()判断会返回false
unset($var1,$var2...$varn) 若传入多个参数，只有全部的参数都为Ture时，最后才返回空。
注意： null 字符（"\0"）并不等同于 PHP 的 NULL 常量。

*/
$var = '';
// 结果为 TRUE，所以后边的文本将被打印出来。
if (isset($var)) {
    echo "变量已设置。" . PHP_EOL;
}
$expected_array_got_string = 'somestring';
var_dump(isset($expected_array_got_string['some_key']));
echo $expected_array_got_string[0].' '. var_dump(isset($expected_array_got_string[0]));
echo $expected_array_got_string['0'].' '.var_dump(isset($expected_array_got_string['0']));
echo $expected_array_got_string[0.5].' '.var_dump(isset($expected_array_got_string[0.5]));
var_dump(isset($expected_array_got_string["0.5"]));
var_dump(isset($expected_array_got_string['0 Mostel'])); // echo的对应三个都是ture,都是索引0 
?>

