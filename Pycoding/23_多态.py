#多态：同一个方法因为对象不同可能会产生不同的行为，
#多态是方法的多态，没有属性的多态
#多太存的两个必要条件：继承和重写
class Man():
	def eat(self):
		print('人吃饭')
class Chinese(Man):
	def eat(self):
		print('中国人吃饭')
class English(Man):
	def eat(self):
		print('外国人吃饭')

def judge(m):
	if isinstance(m,Man):
		m.eat()  #会根据对象的不同来调用对应方法
	else:
		print('非人类')
judge(Chinese())
judge('123')

'''
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
'''