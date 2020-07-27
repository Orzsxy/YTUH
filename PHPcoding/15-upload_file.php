<?php
if ($_FILES["file"]["error"] !=0){ #全局数组 $_FILES，可以从客户计算机向远程服务器上传文件。
    echo "错误：".$_FILES["file"]["error"]."<br>";
}
else{
    echo "上传文件名: ".$_FILES["file"]["name"]."<br>";
    echo "文件类型: ".$_FILES["file"]["type"]."<br>";
    echo "文件大小: ".($_FILES["file"]["size"] / 1024)." kB<br>";
    echo "文件临时存储的位置: ".$_FILES["file"]["tmp_name"];
}
/*
第一个参数是表单的 input name，第二个下标可以是 "name"、"type"、"size"、"tmp_name" 或 "error"
$_FILES["file"]["name"] - 上传文件的名称
$_FILES["file"]["type"] - 上传文件的类型
$_FILES["file"]["size"] - 上传文件的大小，以字节计
$_FILES["file"]["tmp_name"] - 存储在服务器的文件的临时副本的名称
$_FILES["file"]["error"] - 由文件上传导致的错误代码
*/
?>

<?php
// 允许上传的图片后缀
$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["file"]["name"]);
//echo $temp;//."<br>";
$extension = end($temp);        // 获取文件后缀名
if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 204800)    // 小于 200 kb
&& in_array($extension, $allowedExts))  //判断是不是在数组中
{ 
    if ($_FILES["file"]["error"] > 0)
    {
        echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    }
    else
    {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"]; 
        //文件被上传后在服务端储存的临时文件名，一般是系统默认。可以在 php.ini 的 upload_tmp_dir更改，但putenv() 函数设置是不起作用的。
        /*文件被上传结束后，默认地被存储在了临时目录中，这时您必须将它从临时目录中删除或移动到其它地方，如果没有，则会被删除。也就是不管是否上传成功，脚本执行完后临时目录里的文件肯定会被删除。所以在删除之前要用PHP的 copy() 函数将它复制到其它位置，此时，才算完成了上传文件过程。
        */
    }
}
else
{
    echo "非法的文件格式";
}
/*
_FILES['myFile']['error']:
UPLOAD_ERR_OK - 值：0; 没有错误发生，文件上传成功。 
UPLOAD_ERR_INI_SIZE - 值：1; 上传的文件超过了 php.ini 中 upload_max_filesize 选项限制的值。 
UPLOAD_ERR_FORM_SIZE - 值：2; 上传文件的大小超过了 HTML 表单中 MAX_FILE_SIZE 选项指定的值。 
UPLOAD_ERR_PARTIAL - 值：3; 文件只有部分被上传。 
UPLOAD_ERR_NO_FILE - 值：4; 没有文件被上传。 
UPLOAD_ERR_NO_TMP_DIR -其值为 6，找不到临时文件夹。PHP 4.3.10 和 PHP 5.0.3 引进。
UPLOAD_ERR_CANT_WRITE - 其值为 7，文件写入失败。PHP 5.1.0 引进。
*/
?>
<?php
// 允许上传的图片后缀
$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["file"]["name"]);
echo $_FILES["file"]["size"];
$extension = end($temp);     // 获取文件后缀名
if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 204800)   // 小于 200 kb
&& in_array($extension, $allowedExts))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    }
    else
    {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"] . "<br>";
        
        // 判断当前目录下的 upload 目录是否存在该文件
        // 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
        if (file_exists("upload/" . $_FILES["file"]["name"]))
        {
            echo $_FILES["file"]["name"] . " 文件已经存在。 ";
        }
        else
        {
            // 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
            move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);
            echo "文件存储在: " . "upload/" . $_FILES["file"]["name"];
        }
    }
}
else
{
    echo "非法的文件格式";
}
?>