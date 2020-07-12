name = ('张三','李四','王五')
age = (12,18,20)
city = ('北京','上海','杭州')
tb = zip(name,age,city)
for name,age,city in tb:
	print("{0}年龄为{1}，居住在{2}".format(name,age,city))

#推导式生成列表、字典、元组、集合

#列表推导式： [表达式 for item in 可迭代对象]      [表达式 for item in 可迭代对象 if 条件判断]
k = [x for x in range(10) if x%2==0]
print(k)

cells = [[row,col]for row in range(10) for col in range(5)]
print(cells)

cells = [(row,col)for row in range(10) for col in range(5)]
print(cells)
print(cells[0][0])

#字典推导式：
#{key:value for 表达式 in 可迭代对象 } 可以加判断语句和双重循环

#统计文本中字符出现的次数
stri = 'i love you, you love me'
c = dict({c:stri.count(c) for c in stri})
c = {c:stri.count(c) for c in stri}
print(c)

#集合推导式
x = { k for k in range(20) if k%2==0}
print(x)

#没有元组推导式，生成的是一个迭代器,可迭代的对象
k = (x for x in range(1,10))
print(k) #result:generator object <genexpr> at 0x00000293EBAD0890>
print(tuple(k))
print(tuple(k)) #这种生成的可迭代的对象一般都只能用一次