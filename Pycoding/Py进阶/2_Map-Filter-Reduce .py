#Map，Filter	和	Reduce 
#Map会把一个函数影射到一个输入列表的所有元素上,
#map(function_to_apply,	list_of_inputs
# lambda 参数:操作(参数) 
#不使用Map:
items	=	[1,	2,	3,	4,	5] 
squared	=	[]
for i	in	items:				
 	squared.append(i**2) 
#使用Map:
items	= [1,	2,	3,	4,	5] 
squared	= list(map(lambda x: x**2, items))#匿名函数lambdas来配合
#列表函数使用Map
def multiply(x):
	return x
def add(x):
	return x+x
func = [multiply,add]
for i in range(5):
	value = map(lambda x  :x(i), func)
	print(list(value)) #Py2中会自动转化为list，py3中取消了这个
#filter过滤列表中的元素
ll = range(-5,5)
file = filter(lambda x: x<0, ll )
print(list(file))
#推导式的可读性更比map、filter好
#reduce
#https://www.cnblogs.com/lonkiss/p/understanding-python-reduce-function.html
from functools import reduce
scientists =({'name':'Alan Turing', 'age':105},
             {'name':'Dennis Ritchie', 'age':76},
             {'name':'John von Neumann', 'age':114},
             {'name':'Guido van Rossum', 'age':61})
def reducer(accumulator , value):
    sum = accumulator + value['age']
    return sum
total_age = reduce(reducer, scientists,0)
print(total_age)
#set
Ls = ['a','b','c','b','d','m','n','n']
l = set([x for x in Ls if Ls.count(x) > 1])
print(l)
#两个集合的交集:intersection
valid=set(['yellow',	'red',	'blue',	'green',	'black']) 
input_set=set(['red',	'brown']) 
print(input_set.intersection(valid)) 
#差集：difference()
valid=set(['yellow',	'red',	'blue',	'green',	'black']) 
input_set=set(['red',	'brown']) 
print(input_set.difference(valid)) 