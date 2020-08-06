#数学函数

# sum():
In [149]: df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
     ...:                    [np.nan, np.nan], [0.75, -1.3]],
     ...:                   index=['a', 'b', 'c', 'd'],
     ...:                   columns=['one', 'two'])
In [150]: df
Out[150]:
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3
In [151]: df.sum()
Out[151]:
one    9.25
two   -5.80
dtype: float64

In [152]: df.sum(axis=1)	# 支持维度参数
Out[152]:
a    1.40
b    2.60
c    0.00
d   -0.55
dtype: float64

# mean() 
In [153]: df.mean(axis=1,skipna=False)
Out[153]:
a      NaN
b    1.300
c      NaN
d   -0.275
dtype: float64

# 数学函数中的通用参数：
# skipna
# axis
# level		如果轴是层次化索引的，根据level分组约简

# idmax()、idmin() 已经取消了这两个方法

# cumsum()
In [159]: df.cumsum()
Out[159]:
    one  two
a  1.40  NaN
b  8.50 -4.5
c   NaN  NaN
d  9.25 -5.8

# 用来计算数学中常见的统计问题的方法 describle()
In [160]: df.describe()
Out[160]:
            one       two
count  3.000000  2.000000
mean   3.083333 -2.900000
std    3.493685  2.262742
min    0.750000 -4.500000
25%    1.075000 -3.700000
50%    1.400000 -2.900000
75%    4.250000 -2.100000
max    7.100000 -1.300000

In [161]: obj = Series(['a','b','c','d']*4)
In [164]: obj.describe()
Out[164]:
count     16
unique     4
top        d
freq       4
dtype: object

# 常见方法：
# count
# describe
# quantile
# sum
# mean
# median
# mad	根据平均值计算机绝对离差
# var		方差
# std		标准差

# skew		样本值的偏度(三阶矩)
# kurt		样本值的峰度(四阶矩)
# cummin summax	样本值的累计和
# sumprod	样本值的累计最大值和累计最小值
# cumprod	样本值的累计积
# diff		计算一阶差分(对时间序列很有用)
# pct_change	计算百分数变化


# 针对Series的 统计唯一值、统计个数、是否包含在一个数组中的方法：

In [167]: obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
In [169]: obj.unique()
Out[169]: array(['c', 'a', 'd', 'b'], dtype=object)

In [170]: obj.value_counts()
Out[170]:	# 默认是降序出现
a    3
c    3
b    2
d    1
dtype: int64

In [172]: obj.value_counts(sort=False) # 出现的顺序不变
Out[172]:
b    2
c    3
a    3
d    1
dtype: int64


In [176]: mask = obj.isin(['b','s'])
In [177]: obj[mask] # [b,c] 是否在obj中
Out[177]:
5    b
6    b
dtype: object


# 得到DataFrame 中多个相关列的一张柱状图（？）：
In [178]: data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
     ...:                      'Qu2': [2, 3, 1, 2, 3],
     ...:                      'Qu3': [1, 5, 2, 4, 4]})
In [179]: data
Out[179]:
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4
In [180]: data.apply(pd.value_counts).fillna(0)
Out[180]:
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0


# 清除 缺失项 NA

# 对于Series:
In [181]: from numpy import nan as NA
In [182]: data = Series([1,NA,3.5,NA,7])
In [183]: data.dropna()
Out[183]:
0    1.0
2    3.5
4    7.0
dtype: float64
In [185]: data[data.notnull()]
Out[185]:
0    1.0
2    3.5
4    7.0
dtype: float64

# 对于 DataFrame:
obj.dropna() # 丢弃含有NA的行
obj.dropna(how='all') # 只丢弃全为NA的行

obj.dropna(axis=1) #  在列上操作
obj.dropna(axis=1,how='all') # 

#另一种去除DF 行的方法
# 只留下一部分观测数据，用thresh方法：
# thrsh=n理解：这一行除去NA值，剩余数值的数量大于等于n，便显示这一行。
# n: 保留的数值大于等于 n 个
In [190]: df
Out[190]:
          0         1         2
0  0.626543       NaN       NaN
1 -1.356194       NaN       NaN
2  0.880020       NaN       NaN
3  0.040419       NaN  0.594405
4  0.339227       NaN  2.661595
5 -0.346132 -0.748202 -1.587561
6  0.273788  1.233893 -1.504088

In [191]: df.dropna(thresh=2)	#
Out[191]:
          0         1         2
3  0.040419       NaN  0.594405
4  0.339227       NaN  2.661595
5 -0.346132 -0.748202 -1.587561
6  0.273788  1.233893 -1.504088

In [193]: df.dropna(thresh=3)	#
Out[193]:
          0         1         2
5 -0.346132 -0.748202 -1.587561
6  0.273788  1.233893 -1.504088

In [194]: df.dropna(thresh=1)	#
Out[194]:
          0         1         2
0  0.626543       NaN       NaN
1 -1.356194       NaN       NaN
2  0.880020       NaN       NaN
3  0.040419       NaN  0.594405
4  0.339227       NaN  2.661595
5 -0.346132 -0.748202 -1.587561
6  0.273788  1.233893 -1.504088

# 填充缺失数据：
In [196]: df.fillna(0)
Out[196]:
          0         1         2
0  0.626543  0.000000  0.000000
1 -1.356194  0.000000  0.000000
2  0.880020  0.000000  0.000000
3  0.040419  0.000000  0.594405
4  0.339227  0.000000  2.661595
5 -0.346132 -0.748202 -1.587561
6  0.273788  1.233893 -1.504088
# 用字典填充缺失数据，键对应列、字典值对应索要填充的值
# 只填充 NA (fillna())
In [198]: df.fillna({1:'K',2:0})
Out[198]:
          0         1         2
0  0.626543         K  0.000000
1 -1.356194         K  0.000000
2  0.880020         K  0.000000
3  0.040419         K  0.594405
4  0.339227         K  2.661595
5 -0.346132 -0.748202 -1.587561
6  0.273788   1.23389 -1.504088

# fillna默认的是返回新对象,但是有可以就地修改:
In [199]: df.fillna(0,inplace=True)
In [200]: df
Out[200]:
          0         1         2
0  0.626543  0.000000  0.000000
1 -1.356194  0.000000  0.000000
2  0.880020  0.000000  0.000000
3  0.040419  0.000000  0.594405
4  0.339227  0.000000  2.661595
5 -0.346132 -0.748202 -1.587561
6  0.273788  1.233893 -1.504088

# 对 reindex 有效的插值方法也适用于fillna
In [211]: df
Out[211]:
          0         1         2
0  1.148114 -2.277815 -0.147938
1 -0.725451  0.157378 -0.390717
2  0.718833  0.475672       NaN
3  0.952390 -0.142251       NaN
4  0.662782 -0.652540       NaN
5  1.121762  0.440695 -0.199016
6 -1.537519 -1.459584  0.140664

In [212]: df.fillna(method='ffill',limit=2)
Out[212]:
          0         1         2
0  1.148114 -2.277815 -0.147938
1 -0.725451  0.157378 -0.390717
2  0.718833  0.475672 -0.390717
3  0.952390 -0.142251 -0.390717
4  0.662782 -0.652540       NaN
5  1.121762  0.440695 -0.199016
6 -1.537519 -1.459584  0.140664

In [213]: data = Series([1,NA,3.5,NA,7])
In [214]: data.fillna(data.mean())
Out[214]:
0    1.000000
1    3.833333
2    3.500000
3    3.833333
4    7.000000
dtype: float64

###fillna函数参数：
# value 	用于填充缺失值的标量、或字典对象
# method	使用reindex的插值方式，默认是fill
# axis
# inplace
# limit


