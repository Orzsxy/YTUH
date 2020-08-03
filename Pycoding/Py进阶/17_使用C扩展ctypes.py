#使用C扩展
#c的速度可说是py的0.5
#有三种方式使用c扩展
#ctypes，SWIG，Python/C	API
from ctypes import *


# win    生成dll文件

#在win下生成dll的文件我知道的目前只有两种 利用vs自带的cl、link,以及MinGW中gcc编译
#vs中: cl /c Test.c
#      link /dll Test.obj

#MinGW（gcc）:
# gcc -shared -o Test.dll Test.c
adder = CDLL('./add.dll') 
result_int = adder.add_int(4,5)
print(result_int)
#OSError: [WinError 193] %1 不是有效的 Win32 应用程序。若出现这个错误正常，因为win下的dll一般都是32位的，而py是64位的。
# 想解决的方案 https://blog.csdn.net/vample/article/details/88877745

#在Linux中生成 .so文件
gcc	-shared	-Wl,-soname,adder	-o	adder.so	-fPIC	add.c 
# Mac：生成 .so文件
gcc	-shared	-Wl,-install_name,adder.so	-o	adder.so	-fPIC	add.c 
adder	=	CDLL('./adder.so')
在传入浮点、布尔型要使用ctype才可以
a	=	c_float(5.5) 
b	=	c_float(4.1) 
add_float	=	adder.add_float 
print(add_float(a, b))
