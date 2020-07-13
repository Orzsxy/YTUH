'''
__add__   +
__sub__
__lt__   小于
__le__
__eq__
__gt__   大于
__ge__
__ne__
'''
class Person():
	def __init__(self,name):
		self.name = name
	def __add__(self,P):
		if isinstance(P,Person):
			return '{0}{1}'.format(self.name,P.name)
	def __mul__(self,num):
		return self.name*num
		
print(Person('张三')+Person('李四'))
print(Person('王五')*3)