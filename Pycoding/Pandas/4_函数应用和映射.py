#函数应用和映射
In [101]: frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
     ...:                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
In [102]: frame
Out[102]:
               b         d         e
Utah    0.235033 -1.051985 -0.192836
Ohio   -0.240199 -0.029016  1.090142
Texas  -0.443952 -0.954993  1.496374
Oregon -0.103782 -0.463400  1.387197
In [103]: np.fabs(frame)
Out[103]:
               b         d         e
Utah    0.235033  1.051985  0.192836
Ohio    0.240199  0.029016  1.090142
Texas   0.443952  0.954993  1.496374
Oregon  0.103782  0.463400  1.387197

In [108]: f = lambda x:x.max()-x.min()
In [109]: frame.apply(f)
Out[109]:
b    0.678985
d    1.022969
e    1.689210
dtype: float64

In [111]: frame.apply(f,axis = 1) 		# 或用 axis = columns
Out[111]:
Utah      1.287018
Ohio      1.330341
Texas     2.451367
Oregon    1.850597
dtype: float64

# 传递个 apply的参数可以是 由多个值组成的Series
In [112]: def f(x):
     ...:     return pd.Series([x.min(), x.max()], index=['min', 'max'])
     ...:
In [113]: frame.apply(f)
Out[113]:
            b         d         e
min -0.443952 -1.051985 -0.192836
max  0.235033 -0.029016  1.496374

# 元素级的函数也可以用在DataFrame
#	applymap
In [116]: format = lambda x:'%.2f' %x # # # # format = lambda x:('%.2f'%x)
In [117]: frame.applymap(format)
Out[117]:
            b      d      e
Utah     0.24  -1.05  -0.19
Ohio    -0.24  -0.03   1.09
Texas   -0.44  -0.95   1.50
Oregon  -0.10  -0.46   1.39
# 之所以叫 applymap 是因为Series有一个叫map的方法：
In [121]: frame['e'].map(format)
Out[121]:
Utah      -0.19
Ohio       1.09
Texas      1.50
Oregon     1.39
Name: e, dtype: object


# 排序：
# 排序Series
In [122]: obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
In [124]: obj.sort_index()
Out[124]:
a    1
b    2
c    3
d    0
dtype: int64
# 排序DataFrame
In [125]:   frame = pd.DataFrame(np.arange(8).reshape((2, 4)),^M
     ...:                      index=['three', 'one'],^M
     ...:                      columns=['d', 'a', 'b', 'c'])
In [126]: frame.sort_index()
Out[126]:
       d  a  b  c
one    4  5  6  7
three  0  1  2  3
In [127]: frame.sort_index(axis=1)
Out[127]:
       a  b  c  d
three  1  2  3  0
one    5  6  7  4
#   按照索引进行降序排列，两者类似
In [128]: frame.sort_index(axis=1,ascending=False)
Out[128]:
       d  c  b  a
three  0  3  2  1
one    4  7  6  5
# 按照值进行排序 sort_values(), Py3.6+以后就取消了order()方法，
In [131]: obj = Series([4,np.nan,7,np.nan,-3,-2])
In [134]: obj.sort_values()
Out[134]:
4   -3.0
5   -2.0
0    4.0
2    7.0
1    NaN
3    NaN

# DataFrame 中按照值进行排序： by=
In [135]: frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
In [136]: frame.sort_values(by='b')
Out[136]:
   b  a
2 -3  0
3  2  1
0  4  0
1  7  1

# 排名：
In [137]: obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
In [138]: obj.rank()	## #
Out[138]:
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64

In [139]: obj.rank(method='first')
Out[139]:
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64

In [140]: obj.rank(ascending=False, method='max')
Out[140]:
0    2.0
1    7.0
2    2.0
3    4.0
4    5.0
5    6.0
6    4.0
dtype: float64



In [141]: frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
     ...:                       'c': [-2, 5, 8, -2.5]})
In [142]: frame
Out[142]:
     b  a    c
0  4.3  0 -2.0
1  7.0  1  5.0
2 -3.0  0  8.0
3  2.0  1 -2.5
In [143]: frame.rank(axis='columns')
Out[143]:
     b    a    c
0  3.0  2.0  1.0
1  3.0  1.0  2.0
2  1.0  2.0  3.0
3  3.0  2.0  1.0
# average 				默认:在相等分组中，为各个值分配平均排名
# min					使用整个分组的最小排名
# max					使用整个分组的最大排名
# first					按值在原始数据中的出现顺序分配排名(我理解的是按照实数的大小 -10，-8.。。0，1，3，5.。。)



# 带有重复值的索引
n [144]: obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
In [145]: obj.index.is_unique
Out[145]: False
In [146]: obj['a']
     ...:
Out[146]:
a    0
a    1
dtype: int64

In [147]: df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
In [148]: df.loc['b']
Out[148]:
          0         1         2
b  0.940826  0.223722  1.175317
b  0.039920 -0.893853 -0.841165
