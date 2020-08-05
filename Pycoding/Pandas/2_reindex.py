# 重新索引：pd的reindex用来创建一个适应新索引的 新对象（Series、DataFream)

In [4]:  obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
In [5]: obj
Out[5]:
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64

In [7]: obj = obj.reindex(['d', 'b', 'a', 'c','e'])
In [8]: obj
Out[8]:
d    4.5
b    7.2
a   -5.3
c    3.6
e    NaN		#
dtype: float64

In [9]: obj = obj.reindex(['d', 'b', 'a', 'c','e'],fill_value=0)
In [10]: obj
Out[10]:
d    4.5
b    7.2
a   -5.3
c    3.6
e    NaN		# e 因该被填充为0 ，这儿还是Nan
dtype: float64

# reindex实现插值：
In [15]: obj = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
In [16]: obj
Out[16]:
0      blue
2    purple
4    yellow
dtype: object
In [17]: obj.reindex(range(6),method='ffill') # 向前插值
Out[17]:
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
# method 参数：
# ffill pad 		向前填充、向前搬运值
# bfill backfill	向后填充、搬运值

#DataFrame
In [22]: frame = DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns = ['Ohio','Texas','California'])
In [23]: frame   # 之前在创建DataFream的时候用的都是字典，这儿arange
Out[23]:
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8

#reindex可以修改行和列两个索引，但是之传入一个参数又不说明默认是对行索引
In [24]: frame = frame.reindex(columns=['Texas', 'Utah', 'California'])
In [25]: frame  # reindex是针对元对象的索引生成的新对象，所以解释了原先有的值现在没有的情况。和直接在DataFream对象上操作不一样
Out[25]:
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8

# 同时对行和列进行索引，插值只能按行进行
In [35]: frame
Out[35]:
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8
In [36]: frame.reindex(index=['a','b','c','d'],method='ffill',columns = ['Texas','Utah','California'])
Out[36]:
   Texas  Utah  California
a      1   NaN           2
b      1   NaN           2
c      4   NaN           5
d      7   NaN           8
#在执行下面这句话的时候出现 ValueError: index must be monotonic increasing or decreasing ,因为误把 columns值写成 O, 难道说时不能同时对行和列索引生成新对象？
frame.reindex(index=['a','b','c','d'],method='ffill',columns = ['Texas','O','California']) 

#################################
In [44]: frame
Out[44]:
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8
In [46]:frame.ix[['a','b','c','d'], ['Texas','Utah','California']]
# 出现：KeyError: "['b'] not in index" 。在官方文档中并没有给出这种方法，文档中给出的loc方法也不能这样生成新索引



# 删除指定轴上的项：
In [48]: obj = Series(np.arange(5),index=['a','b','c','d','e'])
In [50]: newobj = obj.drop('c')  # 会生成新的对象 
In [51]: newobj
Out[51]:
a    0
b    1
d    3
e    4
dtype: int32
In [52]: obj 
Out[52]:
a    0
b    1
c    2
d    3
e    4
dtype: int32


In [53]: data = pd.DataFrame(np.arange(16).reshape((4, 4)),
    ...:                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
    ...:                     columns=['one', 'two', 'three', 'four'])
In [54]: data
Out[54]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
In [55]: newdata = data.drop(['one','three'],axis=1)
In [56]: newdata
Out[56]:
          two  four
Ohio        1     3
Colorado    5     7
Utah        9    11
New York   13    15

# Series、DataFream 利用索引进型选取 
In [61]: data
Out[61]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
In [62]: data[:3]				# 数字进行切片，不包含末端
Out[62]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11

In [63]: obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

In [64]: obj
Out[64]:
a    0.0
b    1.0
c    2.0
d    3.0
dtype: float64

In [65]: obj[:2] 			# 数字进行切片，不包含末端，Series,DataFream都不包含
Out[65]:
a    0.0
b    1.0
dtype: float64

In [66]: obj['a':'c']		# 索引名称进行切片包含末端
Out[66]:
a    0.0
b    1.0
c    2.0	# 包含
dtype: float64

# 逻辑op：
In [67]: data[data>5] = 0
In [68]: data
Out[68]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      0     0
Utah        0    0      0     0
New York    0    0      0     0


In [69]: data.ix[:'Utah','three']
Out[69]:
Ohio        2
Colorado    0
Utah        0
Name: three, dtype: int32

#  ix来逻辑选取，
In [72]: data
Out[72]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
In [73]: data.ix[data.three>5,1:4]  # 分别是对行、列选择
Out[73]:
          two  three  four
Colorado    5      6     7
Utah        9     10    11
New York   13     14    15

#DataFream的函数操作： Series也类似
# obj[val]			选取DataFrame的单个列或一组列。在一些特殊情况下
#					比较便利:布尔型数组(过滤行)、切片(行切片)、
# obj.ix[val]		选取DataFrame的.单个行或一组行
# obj[:,val]		选取单个列或列子集
# obj[val1,val2]	同时选取行和列
# reindex   		实现插值：可以修改行和列两个索引，
# xs				根据标签选取单行或单列.并返回一个Series
# icol,irow			根据整数位置选取单列或单行，并返回一个
# get_value,set_value根据行标签和列标签选取、设置单个值。


# DataFream:算术运算,Series也是同样的方式
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
df2.loc[1, 'b'] = np.nan # 对某一个值进行操作
# 不匹配的地方会设置为 Nan
In [79]: df1+df2
Out[79]:
      a     b     c     d   e
0   0.0   2.0   4.0   6.0 NaN
1   9.0   NaN  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN
# add 方法时可以填充值，在有点地方不匹配会有：1+NAN = 1 
In [83]: df1.add(df2,fill_value=0)
Out[83]:
      a     b     c     d     e
0   0.0   2.0   4.0   6.0   4.0
1   9.0   5.0  13.0  15.0   9.0
2  18.0  20.0  22.0  24.0  14.0
3  15.0  16.0  17.0  18.0  19.0
# 再用reindex进行新索引的时候也可以进行填充
In [84]: df1.reindex(columns=df2.columns, fill_value=0)
Out[84]:
     a    b     c     d  e
0  0.0  1.0   2.0   3.0  0
1  4.0  5.0   6.0   7.0  0
2  8.0  9.0  10.0  11.0  0