<?php
header("content-type:text/html;charset=utf-8");         //设置编码
?>
<?php
echo "s你说的v";
echo '这是第 " '. __LINE__ .' " 行';		//文件中的当前行号
echo '该文件位于 " '  . __FILE__ . ' " ';	//__FILE__ 文件的完整路径和文件名。如果用在被包含文件中，则返回被包含的文件名。
echo '该文件位于 " '  . __DIR__ . ' " ';	//文件所在的目录。除非是根目录，否则目录中名不包括末尾的斜杠
function test() {
    echo  "\n函数名为：" . __FUNCTION__ ; // 函数名称   PHP 5 起本常量返回该函数被定义时的名字（区分大小写）。在 PHP 4 中该值总是小写字母的。
										  //  __CLASS__		类的名称
}
test();
function test1() {
    echo  '函数名为：' . __METHOD__ ;//类的方法名（PHP 5.0.0 新加）。返回该方法被定义时的名字（区分大小写）
}
test1();
$a = array(
    'a',
    9 => 'b',
    '1' => 'c',
    'd'
);
echo $a['1'];
echo $a[10]; # d的访问方式时出现的最大索引值+1
echo $a[0]; # a的访问方式还是索引0

?>