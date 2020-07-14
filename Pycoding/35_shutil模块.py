'''
shutil模块是做文件及文件夹拷贝、压缩、删除，还可以做文件夹的压缩、解压。
算是对os模块的一个补充
'''
import shutil
shutil.copyfile('E:\Pycoding\log.txt','cplog.txt') #拷贝文件
#shutil.copytree(path1,path2) #目录及其中的内容拷贝，当path2目录存在时不能拷贝，避免一样

#压缩、解压
shutil.make_archive("E:\Pycoding",'zip','E:\Pycoding') #压缩后存放的目录，压缩的格式，压缩的内容
# 结果存放在了上一级目录
# 
import zipfile

z = zipfile.ZipFile('E:/Pycoding/newzip.zip',"w")
z.write('log.txt')
z.write('cplog.txt')
z.close()

uz = zipfile.ZipFile('E:/Pycoding/newzip.zip',"r")
uz.extractall('E:/') #存放的目录
uz.close()