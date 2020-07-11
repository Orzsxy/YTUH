#集合，集合的底层就是字典的实现。相当于c++中set。不含重复对象
#创建集合对象:{}
a = {3,4,5}
#添加元素
a.add(9)
#使用set()将列表、元组转化为集合：
a = [1,2,3,4,5,1]
a = set(a)
print(a)
#删除指定元素
a.remove(1)
#集合清空
a.clear()
print(a)
#集合的运算
a = {1,2,'s','city'}
b = {'he','is','city'}
print(a|b,end=' ') #并
print(a.union(b))
print(a&b,end=' ') #交
print(a.intersection(b))
print(a-b,end=' ') #差
print(a.difference(b)) #