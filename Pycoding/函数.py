def func(a,b):
	'''得到两个数种较大的一个'''
	if a>b:
		print(a,'比较大')
	else:
		print(b,'比较大')

func(10,2)
help(func.__doc__) #函数文档

#在函数内要改变、引用全局变量的值，要使用global说明。
#局部变量和全局变量同名，默认优先使用局部变量。
a = 100
def fun():
	global a
	print(a)
	a = 11
	print(locals()) #可以打印出全局变量和局部变量
	print(globals())
fun()
print(a)

import math
import time
#局部变量的效率较高
def fun0():
	start = time.time()
	for i in range(10000):
		math.sqrt(100)
	end = time.time()
	print('使用全局变量时间:{0}'.format(end-start))
def fun1():
	start = time.time()
	b = math.sqrt
	for i in range(10000):
		b(100) # b为局部变量了
	end = time.time()
	print("使用局部变量时间：{0}".format(end-start))
fun0()
fun1()

'''
参数传递在传递可变对象的更改是在原有可变对象上直接改动，不产生新的对象
		 传递不可变对象是会创建新的对象，在新的对象上进行改动，
'''

#带默认值的参数必须放普通参数的后面,实参会覆盖默认值
def fun2(a,b,c=1):
	print(a,b,c)
fun2(b=1,a=2,c=4) #命名参数
fun2(1,24) #位置参数

#参数的个数可变: *param 多出的参数被收到元组中，**param多出的参数被收到字典中
#在*或者**后面还有其他的参数，在传递实参时必须使用命名参数
def fun3(a,b,*c,**d):
	print(a,b,c,d)
fun3(1,2,3,4,name='张三',age=19)
def fun4(a,b,**c):
	print(a,b,c)
fun4(1,2,name='张三',age=19)

