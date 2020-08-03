#装饰类(比函数中嵌套装饰器整洁)
from functools import wraps
class logit(object):
	def __init__(self,logfile = 'out.log'):
		self.logfile = logfile
	def __call__(self,func):
		@wraps(func)
		def wrapped_function(*args,**agrgs):
			logstring = func.__name__+"was called"
			with open(self.logfile,'a') as f:
				f.write(logstring+"\n")
			self.notify() #发送一个通知
			return func(*agrs,**args)
		return wrapped_function
	def notify(self):
		pass
@logit()
def myfunc1():
	pass

#我们给logit创建⼦类
class	email_logit(logit):
	def	__init__(self,	email='admin@myproject.com',	*args,	**kwargs)：
		self.email	=	email
		super(logit,	self).__init__(*args,	**kwargs)
	def	notify(self):								
	#	发送⼀封email到self.email								
	#	这⾥就不做实现了								
	pass 	
#@email_logit将会和@logit产⽣同样的效果，但是在打⽇志的基础上，还 会多发送⼀封邮件给管理员。
