<?php
/**
��һ���ű���ȫ���������ж����á� �㲻��Ҫ�ر�˵�����Ϳ����ں���������ʹ�á�
**/

//$GLOBALS 		��һ������ȫ�ֱ�����,������ȫ����������ϵõ������顣���������־�������ļ���
$x = 75; 
$y = 25;
 
function addition() { 
    $GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y']; #zҲ��һ$GLOBALS����ȫ�ֱ�����ͬ���ں�������Է���
}
addition(); 
echo $z."\n"; 
// $_SERVER  :����������Ϣ(header)��·��(path)�����ű�λ��(script locations)�����ݵ����顣
//�����е���Ŀ�� Web ���������������ܱ�֤ÿ�����������ṩȫ����Ŀ��
echo $_SERVER['PHP_SELF']."\n";		//��ǰִ�нű����ļ��������ַΪ http://example.com/test.php/foo.bar �Ľű���ʹ�� $_SERVER['PHP_SELF'] ���õ� /test.php/foo.bar��
echo $_SERVER['SERVER_NAME']."\n";
echo $_SERVER['HTTP_HOST']."\n";
echo $_SERVER['HTTP_REFERER']."\n";
echo $_SERVER['HTTP_USER_AGENT']."\n";
echo $_SERVER['SCRIPT_NAME']."\n";			//https://www.runoob.com/php/php-superglobals.html �����ǻ�û���õ�
// PHP $_REQUEST  �����ռ�HTML���ύ�����ݡ�
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
