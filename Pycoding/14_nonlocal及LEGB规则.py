# nonlocal用来声明外层的全局变量
# global用来声明全局变量

#使用nonlocal声明外层的局部变量
def outer():
	a = 10
	def inner():
		nonlocal a
		print(a)
		a = 20
	inner()
	print(a)
outer()

'''LEGB规则：py在查找名称时的顺序：LOCAL->Enclosed->Global->Build in
Local: 方法或者类的内部
Enclosed：指嵌套函数内部，
Global：全局变量
Build in:库函数中的关键字之类
'''
