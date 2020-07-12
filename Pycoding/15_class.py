class Student:
	company = "bytedance"  #类属性，不同的实例属性可以共享
	count = 0
	def __init__(self,name,age): #self必须是第一个参数,对象属性初始化c
		self.name = name  #实例属性
		self.age  = age
		Student.count += 1
	def get_age(self): #实例方法
		print("{0}的年龄是:{1}".format(self.name,self.age))
s1 = Student('张三',18)
s1.get_age() #解释器自身调用的是 Student.get_age(s1),两者等价
Student.get_age(s1)
print('创建的人数:{0}'.format(Student.count))
#可以在类外面给对象新加属性，不过对应的对象删除之后就添加的属性就没有了
s1.city = '上海'
print(s1.city)


# obj.__dict__可以获得对象的所有属性
print(s1.__dict__)

#定义一个空类：
class A:
	pass


#类对象：
stu = Student #
s2 = stu('李四',20)
s2.get_age()

#类方法:操作类属性，必须有 cls
class People:
	company = "bytedance"
	@classmethod #类方法
	def printCompany(cls):
		print(cls.company)
People.printCompany()
#静态方法
class People1():

	@staticmethod #静态方法
	def printA(a,b):
		print(a+b)
People1.printA(1,2)
#类方法 和 静态方法都不能调用 实例方法
# 类方法中访问实例属性和实列方法会导致错误

#析构函数，解释器一般会自动调用析构方法释放资源,也可以手动 def __del__(self):
class People2():

	def __del__(self):
		print('执行到这儿，系统自动调用析构方法')
p = People2()
del p

#全都是对象
class People3():
	def fun(self):
		print('1')

def ff(s):#必须带一个参数，为了保证形参个数相同
	print('2')

def f(s):
	print('f')
p = People3()
People3.un2 = ff

p.fun()
p.un2()
People3.fun = f
p.fun()