#字典的创建: {}、 dict()
a = {'name':1,'2':2,'3':3}
b = dict(name = 1,age = 18,sex ='boy')
c = dict([('name',1),('age',18),('sex','boy')])
d = {}
e = dict()

#zip()创建字典
k = ['name','age','sex']
v = [1,18,'boy']
r = dict(zip(k,v))
print(r)

#dict.fromkeys()创建值为空的字典
p = dict.fromkeys(['name','age','sex'])
print(p)

#值的访问
print(r['sex'])
print(r.get('age'))

#获取所有的键值对
print(r.items())
#获取所有的键
print(r.keys())
#获取所有的值
print(r.values())
#键值对个数
print(len(r))
#判断一个键在不在字典中
print('kk' in r)
#字典的增删，update()将新字典中的所有键值对全都添加到旧字典对象上
w={'name':'kk','money':11}
r.update(w)
print(r)
#字典删除，del()方法，或者clear()删除所有的键值对,pop()删除指定的键值对，并返回对应的’值‘的对象。
del r['name']
x = r.pop('age')
print(x)
#popitem()随机的删除字典中一个键值对，并且返回对应的键值对
print(r.popitem())
#序列解包，序列解包用字典时，默认是对’键‘进行操作；若对键值进行操作用items(),对’值‘操作，要使用values();
r.update(w)
print(r)
#默认对键操作：
sex,name,money = r
#对键值操作items()
sex,name,money = r.items()
#对值进行操作values()
name,age,money = r.values()

