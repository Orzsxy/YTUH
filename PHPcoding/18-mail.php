<?php
/*mail(to,subject,message,headers,parameters)
to	    必需。 email 接收者。
subject	必需。 email 的主题。注释：该参数不能包含任何新行字符。
message	必需。定义要发送的消息。应使用 LF (\n) 来分隔各行。每行应该限制在 70 个字符内。
headers	可选。规定附加的标题，比如 From、Cc 和 Bcc。应当使用 CRLF (\r\n) 分隔附加的标题。
parameters	可选。对邮件发送程序规定额外的参数。
*/
$to = "921560202@qq.com";         // 邮件接收者
$subject = "Email from hack team";                // 邮件标题
$message = "Hello! Dear Xin. \n\twe want to hack yours email.this`s email from byteuler \n\t\t\t\t\t-- a passion for world";  // 邮件正文
$from = "onebitgravel@163.com";   // 邮件发送者
$headers = "From:" . $from;         // 头部信息设置
mail($to,$subject,$message,$headers);
echo "邮件已发送";
/*
当出现：
warning: mail() [function.mail]: Failed to connect to mailserver at "127.0.0.1" port 25, verify your "SMTP" and "smtp_port" setting in php.ini or use ini_set() in E:\TOOL\Apache\htdocs\rzchina_beta\club\includes\mail.inc on line 193.
Unable to send e-mail. Please contact the site administrator if the problem persists.
或出现：
mail(): SMTP server response: 550 5.7.1 Unable to relay for错误。
解决办法：
安装IIS自带的SMTP，在SMTP虚拟服务器上点击右键，在弹出的属性窗口里进行如下设置：
点击访问选项卡，再点击中继，在弹出的窗口出点击添加，然后选单台计算机，添加IP地址为 127.0.0.1。然后一路确定返回。(不进行此项设置，可能会出现：SMTP server response: 550 5.7.1 Unable to relay for zf1315@sina.com。。。的错误)
测试一下：
<?php
mail("linchangfu@126.com","测试","测试是否收到");
?>
*/
?>