# @property装饰器，把方法当成属性来调用
class Employee:
	def __init__(self,ct):
		self.__ct = ct

	@property
	def city(self):
		return self.__ct
	@city.setter
	def city(self,city):
		self.__ct = city

e = Employee('青岛')
e.city = '上海'
print(e._Employee__ct)
