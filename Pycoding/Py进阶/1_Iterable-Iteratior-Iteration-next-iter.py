#先理解迭代器(iterators) ：可以遍历⼀个容器（特别是列表）的对象。迭代器在遍历并读取⼀个容器的数据元素时有三个部分： 
#可迭代对象(Iterable) 迭代器(Iterator) 迭代(Iteration) 


#可迭代对象(Iterable):一个对象，有支持索引的方法，这个对象就是可迭代对象。
#迭代器(Iterator) ：一个对象，定义了next(Python2)	或者__next__⽅法，它就是⼀个迭代器。
#迭代(Iteration) ： 使⽤⼀个循环来遍历某个东西时，这个过程本⾝就叫迭代。

#⽣成器(generators)也是⼀种迭代器，但是你只能对其迭代⼀次。为它们并没有把所有的值存在 内存中，⽽是在运⾏时⽣成值。
#yield(暂且译作“⽣出”)⼀个值
def generator_function(): # 一个生成器函数
	for i in range(10):
		yield i
for i in generator_function():
	print(i);
def finbon(n):
	a =b = 1
	for i in range(n):
		yield a	#每迭代一次就返回一个值
		a,b = b,a+b
print("SS")
for val in finbon(3):
	print(val);
#内置函数next()返回可迭代对象的下一个元素，
def	generator_function():				
	for	i	in	range(3):								
		yield	i 
gen	= generator_function() 
print(next(gen)) #out1
print(next(gen)) #out2
print(next(gen)) #out3 
#print(next(gen)) #out StopIteration
#在yield所有的值之后，next()触发了StopIteration，在for循环中没有看到这种异常是因为for会自动捕捉这个异常，停止调用

# iter生成一个可迭代对象
my_string	=	"Yasoob";
my_iter	=iter(my_string) 
print(next(my_iter)) 
