'''
os模块对操作系统操作，可以调用系统可执行文件、命令、目录等，在运维中是核心模块
'''
import os
os.system('notepad.exe')
'''
os.system('FilePath')
#os文件操作
os.remove() #
remove(path) 删除指定的文件
rename(src,dest) 重命名文件或目录
stat(path) 返回文件的所有属性
listdir(path) 返回 path目录下的文件和目录列表
#os目录操作
mkdir(path) 创建目录
makedirs(path1/path2/path3/...) 创建多级目录
rmdir(path) 删除目录
removedirs(path1/path2...) 删除多级目录
getcwd() 返回当前工作目录：current work dir
chdir(path) 把path设为当前工作目录
walk() 遍历目录树
sep 当前操作系统所使用的路径分隔符
'''

'''
os.path模块:
os.path.isabs(path) 判断 path是否绝对路径
isdir(path) 判断 path是否为目录
isfile(path) 判断 path是否为文件
exists(path) 判断指定路径的文件是否存在
getsize(filename) 返回文件的大小
abspath(path) 返回绝对路径
dirname(p) 返回目录的路径
getatime(filename) 返回文件的最后访问时间
getmtime(filename) 返回文件的最后修改时间
walk(top,func,arg) 递归方式遍历目录
join(path,*paths) 连接多个 path
split(path) 对路径进行分割，以列表形式返回
splitext(path) 从路径中分割文件的扩展名
'''