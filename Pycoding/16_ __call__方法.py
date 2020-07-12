'''
__call__()。
该方法的功能类似于在类中重载 () 运算符，
使得类实例对象可以像调用普通函数那样，
以“对象名()”的形式使用。
'''
class CL:
	def __call__(self,name):
		print(name)
	 
c = CL() 
c('张三')
c.__call__('张阿三')
 
#和下面这种函数类似：
def say():
	print("me too")
say()
say.__call__()

