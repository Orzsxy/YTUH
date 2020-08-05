# Pandas是基于numpy构建的

In [2]: from pandas import Series,DataFrame
In [3]: import pandas as pd

# 由一组数据(Numpy类型的数据)以及一组与之相关的数据索引组成
# 只由一组数据可以构成最简单的Series
In [4]: obj = Series([4,7,5,-3])
In [5]: obj
Out[5]:
0    4
1    7
2    5
3   -3
dtype: int64

# 获取索引和值
In [6]: obj.values
Out[6]: array([ 4,  7,  5, -3], dtype=int64)
In [7]: obj.index
Out[7]: RangeIndex(start=0, stop=4, step=1)

#指定索引
In [8]: obj =Series([4,7,5,-3],index = ['a','b','c','d'])
In [9]: obj
Out[9]:
a    4
b    7
c    5
d   -3
dtype: int64
#通过索引获取值
In [10]: obj['a']
Out[10]: 4
In [11]: obj[['a','b','c']]
Out[11]:
a    4
b    7
c    5
dtype: int64

#Series对象也可以进行数组运算
In [12]: obj**2
Out[12]:
a    16
b    49
c    25
d     9
dtype: int64
In [13]: obj[obj>0]
Out[13]:
a    4
b    7
c    5
dtype: int64

# 可以将Series看成是字典，
In [15]: 'b' in obj
Out[15]: True
In [17]: 'e' in obj
Out[17]: False

In [18]: sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
In [20]: obj =Series(sdata)
In [21]: obj
Out[21]:
Ohio      35000
Texas     71000
Oregon    16000
Utah       5000
dtype: int64

#同时传入一个字典和索引
In [23]: states = ['California', 'Ohio', 'Oregon', 'Texas']
In [25]: obj = pd.Series(sdata,index = states)
In [26]: obj # 因为传入的索引值中没有Utah，所以最终Series没有改对象，index中有California，但字典中没有，所以相应的值为Nan
Out[26]:
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64

# Series出现了Nan，如何检测该值是否为Nan:
In [27]: obj.isnull()
Out[27]:
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
In [28]: obj.notnull()
Out[28]:
California    False
Ohio           True
Oregon         True
Texas          True
dtype: bool
In [29]: pd.isnull(obj)
Out[29]:
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool

# Series对象本身及索引都有一个name属性
In [31]: obj.name = 'population'
In [32]: obj.index.name = 'state'
In [33]: obj
Out[33]:
state
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64

