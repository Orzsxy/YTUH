# Python中支持多继承,尽量不要使用多继承，容易混乱
#class 子类类名(父类类名1,父类类名2):
class Person():
	def __init__(self,name,age):
		self.name = name
		self.__age = age
	def say_age(self):
		print('姓名：{0}'.format(self.name))

class Student(Person):
	def __init__(self,name,age,score):
		
		Person.__init__(self,name,age)
		self.score = score 


s = Student('张三',18,92)
s.say_age()
#print(s.age)
print(dir(s))
#子类虽然继承了父类的所有属性，但是父类的私有属性不能直接方法，要按照访问自己类中私有成员的方法进行访问
print(s._Person__age)
print(s.name)

#多继承中使用mro()查看调用的顺序：其实是多继承中同名方法的调用是按照继承的顺序决定的
class A():
	def say(slef):
		print('A')
class B():
	def say(self):
		print('B')
class C(A,B):
	def say(self):
		print('C')
k =C()
print(C.mro()) #在项目中可以打印出调用的层次结构
k.say() #