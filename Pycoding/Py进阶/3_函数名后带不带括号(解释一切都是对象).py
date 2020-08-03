def fun(name = 'bob'):
	return "fun:"+name;
print(fun())
g = fun;
print(g())
del fun
#print(fun())   #Error fun这个对象已经不存在了
print(g())
#函数的嵌套，但是嵌套在里面的函数只能在函数内部访问，不能再外面调用,是因为没有找到那个函数的地址。
def a():
	print('a');
	def b():
		return 'b'
	def c():
		return 'c'
	print(b())
	print(c())
a()
#b() Error找不到对应的地址
def	hi(name="yasoob"):				
	def	greet():								
		return	"now	you	are	in	the	greet()	function"				
	def	welcome():								
		return	"now	you	are	in	the	welcome()	function"				
	if	name	==	"yasoob":								
		return	greet				
	else:								
		return	welcome 
val	=	hi() #有()指这个函数将被执行，不然就是将其赋值为一个对象
print (val) #现在找到了内部函数的地址，所以能够访问了。
print(val())
# 把函数作为参数进行传递
def	hi():				
	return	"hi	yasoob!" 
def	doSomethingBeforeHi(func):				
	print("I	am	doing	some	boring	work	before	executing	hi():", end=' ')				
	print(func()) 
doSomethingBeforeHi(hi)




