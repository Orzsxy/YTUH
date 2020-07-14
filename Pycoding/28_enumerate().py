'''
enumerate(sequence, [start=0])
将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
一般用在 for 循环当中。
start参数指下标起始的数字，默认是0
'''
a = ['张三','李四','王五']
print(tuple(enumerate(a)))
print(list(enumerate(a))) 
b = list(enumerate(a))
c = [str(index)+' '+str(value)+'\n' for index,value in b]

with open('E:\Pycoding\log.txt','a+',encoding='GBK') as f: #
	li = f.readlines()
	li = list(enumerate(li))
	li = [str(value)+' '+str(value)+'\n' for index,value in li]
	f.writelines(c)	