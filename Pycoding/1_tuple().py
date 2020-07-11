#元组的创建
a = (1,2,3)
b = 1,2,3
c = (1,) #c为元组
c = (1)  #c为int

#tuple(可迭代的对象)
a = tuple((1,2,3))
b= tuple([1,2,3])
c= tuple(range(3))
#删除
del c

#元组的元素不能修改，列表可以
a = (20,10,5)
#a[0] = 1
#TypeError: 'tuple' object does not support item assignment

#通过索引和切片来访问元组对象
print (a[0:3:2])

#元组的排序：sorted(),排序生成新的对象，不对原有的对象更改
sorted(a)

'''
元组的处理速度比列表快；
不可变序列；
元组可以作为字典的键使用，列表不能
'''