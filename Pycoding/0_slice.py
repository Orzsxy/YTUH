#slice(stop)
#class slice(start, stop[, step]) 起始位置，终止位置，步长。好像没有用[:]简便
array = []
array =list( range(10) ) #想得到数必须list,返回的range返回的是一个迭代器

myslice = slice(5)  # 切片对象
print(array[myslice])
print(myslice)

myslice = slice(2,5,2)
print(array[myslice])
print(myslice)

# split(sep),用来分割
s = 'i love i'
s = s.split(' ')
print(s)