'''
os模块对操作系统操作，可以调用系统可执行文件、命令、目录等，在运维中是核心模块
'''
import os
#os.system('notepad.exe') #打开可执行命令
#os.system('ping baidu.com')
#os.system('cmd')
print(os.name)#win操作系统名字是nt，linux是posix
print(os.sep) #os的目录分隔符win是\ Linux是/
print(repr(os.linesep))#换行分隔符win是\r\n,linux是\n\
print(os.stat('32_os模块.py'))#获取文件的信息
print(os.getcwd())#当前的工作目录

from os import path
print(path.isabs('E:\Pycoding')) #是否是绝对路径
print(path.isdir('E:\Pycoding')) #是否是目录(有可能是文件)
print(path.isfile('E:\Pycoding')) #是否是文件
print(path.exists('E:\Pycoding')) #目录或文件是否存在
print(path.getsize('E:\Pycoding'))#获得文件大小
print(path.abspath('E:\Pycoding'))#获得文件绝对路径
print(path.dirname('E:\Pycoding'))#获得文件所在目录
#对文件或者目录的创建时间访问时间或者修改时间
print(path.getctime('E:\Pycoding'))
print(path.getatime('E:\Pycoding'))
print(path.getmtime('E:\Pycoding'))

# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分割num次
# 在path中的split() 分割成路径名或、文件(目录)名

ph = path.abspath('E:\Pycoding')
print(path.split(ph))
print(path.splitext(ph)) #用在含有文件名的目录中，把文件名也隔开
print(path.join('a','b','c'))#用目录连接符把字符连接起来

#找出目录中所有类型的文件
ph = os.getcwd()
files = [file for file in os.listdir(ph) if  file.endswith('py') ]
print(files)
#walk()
list_files = os.walk(ph) #返回 指定目录的路径、目录下的所有文件夹、目录下的所有文件
for dirpath,dirname,filenames in list_files: #打印所有子目录子文件
	for dir in dirname:
		print(path.join(dirpath,dir))
	for file in filenames:
		print(path.join(dirpath,file))
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