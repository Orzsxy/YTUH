'''
生成器推导式生成对像
生成器推导式与列表推导式类似，只是生成器推导式使用小括号，列表推导式生成列表对象，
生成器推导式生成的既不是列表也不是元组，而是一个迭代器对象，可以手动转换
'''
s = (x**2 for x in range(5))
print(type(s))
print(list(s))
print(tuple(s)) #error,只能访问一次，再次访问，需要在生成一次
s = (x**2 for x in range(5))
print(tuple(s))

S = (x*2 for x in range(5))
print(S.__next__()) # __next__()、next(S)访问迭代器的对象,py2使用.next()访问

list(S)
k = iter(S) #可以将一个可以迭代的对象转化为迭代器对象
print(k.__next__())
'''
没有修复这个bug:
Traceback (most recent call last):
  print(k.__next__())
'''