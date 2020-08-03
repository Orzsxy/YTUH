#函数缓存
#函数缓存允许我们将⼀个函数对于给定参数的返回值缓存起来。 
#Py3.2+以后的版本 ⽤lru_cache
from	functools	import	lru_cache 
@lru_cache(maxsize=3) 
def	fib(n):
	if	n	<	2:								
		return	n				
	return	fib(n-1)	+	fib(n-2) 
print([fib(n)	for	n	in	range(10)]) 
#	Output:	[0,	1,	1,	2,	3,	5,	8,	13,	21,	34] 
#那个maxsize参数是告诉lru_cache，最多缓存最近多少个返回值。 
#我们也可以轻松地对返回值清空缓存，通过这样： fib.cache_clear()

#Py2+的就是装饰器就是缓存机制