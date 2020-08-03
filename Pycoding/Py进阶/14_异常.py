#异常
#处理异常的几种方式
try :
	file = with open(.)
except (IOError,EOFError) as e:
	print(e)

try:
	file = with open(.)
except (EOFError) as e:
	raise e
except (EOFError) as e:
	raise e
#	
try:
	file = with open(.)
except Exception as e:#异常的基类
	print(e)
finally:				#最终一定会执行的，不管有没有异常
	print("This	would	be	printed	whether	or	not	an	exception	occurred")
#
try:
	file = with open(.)
except Exception as e:#异常的基类
	print(e)
else:	#没有异常才执行else,但else中异常不会被捕获

finally:				#最终一定会执行的，不管有没有异常
	print("This	would	be	printed	whether	or	not	an	exception	occurred")