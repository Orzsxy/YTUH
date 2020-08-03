#协程
#Python中的协程和⽣成器很相似但又稍有不同。
# ⽣成器是数据的⽣产者 协程则是数据的消费者 
def	grep(pattern):								
	print("Searching	for",	pattern)								
	while	True:												
		line	=	(yield)												
		if	pattern	in	line:																
			print(line) 
#！yield返回了什么？ 我们已经把它变成了⼀个协程。它将不再返回任何初始值，相反要从外部传值给它。
#我们可以通过send()⽅法向它传值
search	=	grep('coroutine')				
next(search)				
#output:	Searching	for	coroutine				
search.send("I	love	you")				
search.send("Don't	you	love	me?")				
search.send("I	love	coroutine	instead!")				
#output:	I	love	coroutine	instead! 因为coroutine in line
#发送的值会被yield接收。
#我们为什么要运⾏next()⽅法呢？这样做正是为了启动⼀个 协程。
#就像协程中包含的⽣成器并不是⽴刻执⾏，⽽是通过next()⽅法来响应send()⽅法。
#因此，你必须通过next()⽅法来执⾏yield表达式。 

#过调⽤close()⽅法来关闭⼀个协程:
search.close()

