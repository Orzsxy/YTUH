#为类的属性减小内存消耗

#一般的不用slots()定义类的属性
class	MyClass(object):		
	def	__init__(self,	name,	identifier):						
		self.name	=	name						
		self.identifier	=	identifier						
		self.set_up()	
#使⽤	__slots__: 
class	MyClass(object):		
	__slots__	=	['name',	'identifier']		
	def	__init__(self,	name,	identifier):						
		self.name	=	name						
		self.identifier	=	identifier						
		self.set_up()	
#第⼆段代码会为内存减轻负担。有些⼈已经看到内存占⽤率⼏乎有40%~50%的减少。 

#⽤IPython来可以来显示内存的精确消耗
#在py中需要进一步安装使用,支持py3.8+ https://github.com/ianozsvald/ipython_memory_usage
#import	ipython_memory_usage.ipython_memory_usage	as	imu 
#imu.start_watching_memory() 