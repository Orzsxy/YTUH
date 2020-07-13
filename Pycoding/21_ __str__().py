#print(类对象) 会打印出来对象的信息，其实是调用了 __str__()方法，
class Person():
	def __init__(self,name):
		self.name = name
p = Person('赵六')
print(p)

#重写 __str__()方法：
class Per():
	def __init__(self,name):
		self.name =name
	def __str__(self):
		return ('重写之后的信息..{0}'.format(self.name))
p = Per('荆轲')
print(p)
