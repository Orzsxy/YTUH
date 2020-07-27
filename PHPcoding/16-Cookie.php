<?php
/*cookie 常用于识别用户。cookie 是一种服务器留在用户计算机上的小文件。每当同一台计算机通过浏览器请求页面时，这台计算机将会发送 cookie。通过 PHP，您能够创建并取回 cookie 的值。*/
//setcookie() 函数用于设置 cookie。数必须位于 <html> 标签之前
//发送 cookie 时，cookie 的值会自动进行 URL 编码，在取回时进行自动解码。（为防止 URL 编码，请使用 setrawcookie() 
?>

<?php
// /创建名为 "user" 的 cookie，并为它赋值 "runoob"。我们也规定了此 cookie 在一小时后过期
setcookie("user", "runoob", time()+3600);
?>
<?php
// /取回 Cookie 的值
// 取回了名为 "user" 的 cookie 的值，并把它显示在了页面上
echo $_COOKIE["user"];
// 查看所有 cookie
print_r($_COOKIE);
//若应用程序需要与不支持 cookie 的浏览器交互可以使用表单在页面之间传递信息。
?>