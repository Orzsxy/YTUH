<!DOCTYPE HTML> 
<html> html文件
<head>
<meta charset="utf-8">
<title>表单验证</title>
<style>
	.error {color: #FF0000;} <!--*题型设置为红色-->
</style>
</head>
<body>
<?php
	//定义变量为空并且设置为空值
$nameErr = $emailErr = $genderErr = $websiteErr = "";
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    if (empty($_POST["name"])){
        $nameErr = "名字是必需的";
    }
    else{
        $name = test_input($_POST["name"]);
        // 检测名字是否只包含字母跟空格
        if (!preg_match("/^[a-zA-Z ]*$/",$name)){
            $nameErr = "只允许字母和空格"; 
        }
    }
   
    if (empty($_POST["email"])){
      $emailErr = "邮箱是必需的";
    }
    else{
        $email = test_input($_POST["email"]);
        // 检测邮箱是否合法
        if (!preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/",$email)){
            $emailErr = "非法邮箱格式"; 
        }
    }
    
    if (empty($_POST["website"])){
        $website = " ";
    }
    else{
        $website = test_input($_POST["website"]);
        // 检测 URL 地址是否合法
        if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)){
            $websiteErr = "非法的 URL 的地址"; 
        }
    }
    
    if (empty($_POST["comment"])){
        $comment = "";
    }
    else{
        $comment = test_input($_POST["comment"]);
    }
    
    if (empty($_POST["gender"])){
        $genderErr = "性别是必需的";
    }
    else{
        $gender = test_input($_POST["gender"]);
    }
}

function test_input($data){
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
/*1、trim() 函数去除用户输入数据中不必要的字符 
  2、stripslashes()函数去除用户输入数据中的反斜杠 (\)
  3、正则表达式匹配函数：int preg_match ( string $pattern , string $subject [, array $matches [, int $flags ]] )
	在 subject 字符串中搜索与 pattern 给出的正则表达式相匹配的内容。如果提供了matches,$matches[i] 将包含与i个捕获的括号中的子模式所匹配的文本，以此类推。
*/
?>

<h2>表单验证例子：</h2>
<p><span class="error">*必需字段</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
	姓名:<input type="text" name="name" value="<?php echo $name; ?>">
		<span class="error">* <?php echo $nameErr; ?> </span>
	<br><br>
	Email: <input type="text" name="email" value="<?php echo $email; ?>">
		<span class="error">* <?php echo $emailErr; ?></span>
	<br><br>
	Website:<input type="text" name="website" value="<?php echo $name; ?>">
		<span class="error"><?php echo $websiteErr; ?></span>
	<br><br>
	性别:
   		<input type="radio" name="gender" <?php if (isset($gender) && $gender=="female") echo "checked";?>  value="female">女
   		<input type="radio" name="gender" <?php if (isset($gender) && $gender=="male") echo "checked";?>  value="male">男
   		<span class="error">* <?php echo $genderErr;?></span>
   		<br><br>
	备注:<textarea type="text" name="comment" rows="5" cols = "20"><?php echo $comment; ?></textarea> 
	<br><br>
	<input type="submit" name="submit" value="Submit"> 
</form>
<?php
echo "<h2>您输入的内容是:</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $website;
echo "<br>";
echo $comment;
echo "<br>";
echo $gender;
/**
1、在表单中 $_SERVER["PHP_SELF"]是超级全局变量，返回当前正在执行脚本的文件名，与文件路径相关 所以$_SERVER["PHP_SELF"] 会发送表单数据到当前页面，而不是跳转到不同的页面。
2、htmlspecialchars() 函数把一些预定义的字符转换为 HTML 实体。
3、表单中需引起注重的地方，
	a.当黑客使用跨网站脚本的HTTP链接来攻击时，$_SERVER["PHP_SELF"]服务器变量也会被植入脚本。原因就是跨网站脚本是附在执行文件的路径后面的，
	因此$_SERVER["PHP_SELF"]的字符串就会包含HTTP链接后面的JavaScript程序代码。好吧我不是hacker.(CSS,跨站脚本攻击。恶意攻击者往Web页面里插入恶意html代码，当用户浏览该页之时，嵌入其中Web里面的html代码会被执行，从而达到恶意用户的特殊目的)
	b.如何避免 $_SERVER["PHP_SELF"] 被利用.  通过 htmlspecialchars() 函数来避免被利用:字符转换为 HTML 实体

**/
?>
</body>
</html>