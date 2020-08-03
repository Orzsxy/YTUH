from functools import wraps
# 在函数中嵌套装饰器
def logit(logfile = 'out.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args,**kwargs):
			log_string = func.__name__ + "was called"
			print(log_string)
			with open(logfile,'a') as f:
				f.write(log_string+"\n")
			return func(*args,**kargs)
		return wrapped_function
	return logging_decorator
@logit()
def myfunc1():
	pass
@logit(logfile='func2.log')
def myfunc2():
	pass
