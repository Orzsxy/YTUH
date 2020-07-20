#numpy底层是c写的，支持向量计算
import numpy as np
a = np.arange(10)
print(a)
print(type(a))

#对ndarray对象进行向量计算
print(np.sqrt(a))

#使用array创建高维数组：
print(np.array([[1,2,3],(4,5,6)])) #list还是tuple都转化为ndarray
print(np.array([[[1,1,1],[2,2,2],[3,3,3]]],dtype=float,ndmin=1))
print(np.array([1,1,1],dtype=float,ndmin=3))#ndim维度

'''
也是数组：
np.arange(start,end,step,dtype) 
start 起始值，默认为0
end	  终值，不包含
step  步长,默认为0c
dtype 若不给出，按照输入的数据类型
'''
print(np.arange(10))
'''
np.random.random(size)
返回[0,1.0）之间的随机数,可以高维
'''
a = np.random.random(5)
print(a)
a = np.random.random(size=(4,5)) #二维
print(a)
a =np.random.random(size=(5,3,4))#三维，5个3行4列
print(a)
'''
np.random.randint(start,end,size,dtype) 
随机整数：数的起始范围，维度，类型
'''
d = np.random.randint(0,6,size=(3,2),dtype=np.int64)
print('默认的类型',d.dtype) #不设置默认的是32位
'''
随机的标准正态分布数
np.random.randn(d0,d1,...dn) 
dn表格的每个维度
'''
a = np.random.randn(2,3) #二维的2行3列
'''
指定期望和方差的分布
np.random.normal(loc=0.0,scale=1.0,size)
loc:期望
scale:方差
size:维度
'''
a = np.random.normal(loc=1,scale=4,size=(2,3))
print(a)

'''
这些ndarray对象具有的属性：
ndim:维度大小
shape:具体的维度大小
dtype
itemsize:每个元素占用字节
'''
'''
zeros(shape,dtype=float,oredr='C')：0填充数组
ones(shape,dtype='None,order='C'):
empty(shape,dtype=float,order='C')：没有赋值的数组，初始的值是原先内存中的值
order有两个属性值，C、F行优先，列优先在内存中的元素存储顺序
'''
a = np.zeros((5,)) #其实就是 zeros(5),都是一维的
a = np.ones((2,3),dtype=int)
a = np.empty((10,)) #
print(a)
'''
linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None):由等差数列构成的一维数组
logspace(start,stop,num=50,endpoint=True,base=10.0,dtype,zxis=0):由等比数列构成的一维数组
start、stop 序列的起始、终止值，如果endpoint=True那么stop这个值包含在数组中
num 数的个数，默认是50
base：比值,默认是10
'''
a = np.linspace(1,10,10)
a = np.logspace(1,10,2,base=10)
print(a)

#ndarray一维切片操作和list操作一样
#二维数组的切片:[行切片,列切片]，里面都作为一维的操作
a = np.arange(1,13)
print(a)
a=a.reshape(3,4)
print(a)
print(a[-1:0:-1,3:1:-1])  
print(a[:,1]) #所有行第一列
print(a[2][1])
print(a[2,1]) 	#用坐标获取第三行，第二列的元组
print(a[(2,1),(1,2)]) #获取第三行第二列，第二行第散列的元素，前一部分代表所有的行，后面代表所有列
'''
数组的拷贝，直接对象名赋值和先前一样是地址
使用深拷贝就不改变原先对象，numpy中深拷贝是copy
'''
cpa = np.copy(a[:2:1,:])
print(cpa)

#修改数组的维度也可以：np.reshape(obj,(dim1,dim2...ndim))
#将多维的转化为一维的：obj.reshape(-1)、obj.ravel()、obj.flatten()
print(a.reshape(-1))
print(a.ravel())
print(a.flatten())

'''数组的拼接：hstack()、vstack()
水平拼接，对应的接到每行后面
垂直拼接直接放在下面
np.concatenate((a1,a2,...),axis):沿着指定轴连接相同形状的两个或者多个数组
axis:默认是0,垂直方向沿着它连接数组的轴。垂直方向时要求列数相同，水平方向行数相同，1是水平
对于二维数组有两个轴：axis：0,1
对于三维数组有三个轴：axis:0,1,2
...
'''
print(a)
print(cpa)
#b = np.hstack([a,cpa]) #要求两个数组的行数相同，列数不要求，会填充
#print(b)
b = np.vstack([a,cpa]) #要求两个数组列相同，行数不要求
print(b)
b = np.concatenate((a,cpa))
print(b)