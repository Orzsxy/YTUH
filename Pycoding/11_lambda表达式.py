# lambda表达式:匿名函数
#lambbda arg1,arg2,arg3:<表达式>
#只允许包含一个表达式，不能包含复杂的语句，表达式的结果就是lambda的返回值
f = lambda a,b,c:a+b+c
print(f)
print(f(1,2,3))

r = [lambda a:a**2,lambda b:b**2,lambda c:c**2] 
print(r[0](1),r[1](2),r[2](3)) # r[i] 是lambda表达式

def fun1(a,b):
	return a*b
def fun2(a,b):
	return a*b
r = [fun1,fun2]
print(r[0](2,2),r[1](3,3))