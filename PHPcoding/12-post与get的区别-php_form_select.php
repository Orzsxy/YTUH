<?php
// 因为表单的名字也是 q
$q = isset($_GET["q"])? htmlspecialchars($_GET['q']) : ''; // 处理成html页面的固定格式后给 $q
if($q) {
    //echo "".$q.' '.$_GET['q']."<br>";
        if($q =='RUNOOB') {
                echo '菜鸟教程<br>http://www.runoob.com';
        } else if($q =='GOOGLE') {
                echo 'Google 搜索<br>http://www.google.com';
        } else if($q =='TAOBAO') {
                echo '淘宝<br>http://www.taobao.com';
        }
} 
else {
?>

<form action="" method="get"> 
    <select name="q"> 
    <option value="">选择一个站点:</option>
    <option value="RUNOOB">Runoob</option>
    <option value="GOOGLE">Google</option>
    <option value="TAOBAO">Taobao</option>
    </select>
    <input type="submit" value="提交">
    </form>

<?php
/* form 的action属性为空，表示把表单获取的数据提交给自己。
    然后通过select的name属性获取下拉菜单的值

$_POST和$_GET的区别：
1.前者可以在网址的栏目上是看不到传送的内容的，而后者呢是是可以在网址的栏目是看到内容的
2.Get 方式需要使用 Request.QueryString 来取得变量的值,对发送的信息量也有限制（最多 2000 个字符）;
而 Post 方式通过 Request.Form 来访问提交的内容
3.前者传输的内容的大小比较大，安全性比较高，执行效率稍微低一些；后者的上传大小比较小，安全性低，执行的效率会计较高一点
4、 Get 方式提交数据，会带来安全问题，比如一个登陆页面，通过 Get 方式提交数据时，用户名和密码将出现在 URL 上，如果页面可以被缓存或者其他人可以访问客户这台机器，就可以从历史记录获得该用户的帐号和密码，所以表单提交建议使用 Post 方法；Post 方法提交的表单页面常见的问题是，该页面如果刷新的时候，会弹出一个对话框
5、默认情况下，POST 方法的发送信息的量最大值为 8 MB（可通过设置 php.ini 文件中的 post_max_size 进行更改）变量不显示在 URL 中，所以无法把页面加入书签
*/
}
?>