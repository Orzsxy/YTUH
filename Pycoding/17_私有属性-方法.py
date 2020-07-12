'''
两个下划线开头的属性是私有的，
通过_类名__私有属性(方法)名访问私有的
'''
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, name,age):
		super(ClassName, self).__init__()
		self.name = name
		self.__age = age #私有属性
	def __work(self):
		print('私有方法')
c= ClassName('张三',19)
print(c.name)
print(c._ClassName__age)
c._ClassName__work()