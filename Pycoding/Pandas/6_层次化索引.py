

# 层次化索引：
# pandas的功能，使在一个轴上有两个以上的索引，能以低纬度形式处理高纬度数据

In [6]: data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
In [7]: data
Out[7]:
a  1    0.414230
   2    1.786898
   3   -1.580723
b  1    0.152616
   2   -0.516761
   3    1.089415
c  1   -0.157162
   2    1.128579
d  2    0.180912
   3   -1.128723
dtype: float64
# 
In [8]: data.index
Out[8]:
MultiIndex([('a', 1),
            ('a', 2),
            ('a', 3),
            ('b', 1),
            ('b', 2),
            ('b', 3),
            ('c', 1),
            ('c', 2),
            ('d', 2),
            ('d', 3)],
           )
# 对内层索引进行选取，[:,:] ,前是是对外层索引、	,后是内层索引
In [9]: data[:,2]
Out[9]:
a    1.786898
b   -0.516761
c    1.128579
d    0.180912
dtype: float64

# Series的层次化索引可以通过unstack,被转化成DataFrame:


# 通过unstack转化为DataFrame stack转化为Series
In [10]: data.unstack()
Out[10]:
          1         2         3
a  0.414230  1.786898 -1.580723
b  0.152616 -0.516761  1.089415
c -0.157162  1.128579       NaN
d       NaN  0.180912 -1.128723

# DataFrame 中每个轴都可以有层次索引，每个索引也都可以有自己的名字
In [11]: frame = DataFrame(np.random.randn(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
In [13]: frame.index.names=['key1','key2']
In [14]: frame.columns.names=['state','color']
In [15]: frame
Out[15]:
state          Ohio            Colorado
color         Green       Red     Green
key1 key2
a    1    -0.753210  1.544642 -0.704277
     2    -2.462603 -0.222514  1.672321
b    1     1.386842  1.120400 -0.919724
     2    -1.711599  0.038431  1.107696
# 交换层次索引的层次
In [16]: frame.swaplevel('key1','key2') # 或者是 swaplevel(0,1)
Out[16]:
state          Ohio            Colorado
color         Green       Red     Green
key2 key1
1    a    -0.753210  1.544642 -0.704277
2    a    -2.462603 -0.222514  1.672321
1    b     1.386842  1.120400 -0.919724
2    b    -1.711599  0.038431  1.107696
# In [18]: frame.swaplevel(0,1).sortlevel(0)  取消了sortlevel()方法
# 有 sort_index() sort_values()

#
# 根据层次求和：
In [31]: frame.sum(level='key2')
Out[31]:
state      Ohio            Colorado
color     Green       Red     Green
key2
1      0.633633  2.665041 -1.624000
2     -4.174202 -0.184084  2.780017

In [40]: frame.sum(level='color',axis=1) # color虽然是列上的名字，一般操作的都是行上的关系，所以也要用axis=1说明
Out[40]:
color         Green       Red
key1 key2
a    1    -1.457486  1.544642
     2    -0.790281 -0.222514
b    1     0.467119  1.120400
     2    -0.603903  0.038431

#把DataFrame的一些列索引转化为行索引，使变成层次化的结构：
In [41]: frame = DataFrame({'a':np.random.randn(7),
    ...: 'b':range(7,0,-1),
    ...: 'c':['one','one','one','two','two','two','two'],
    ...: 'd':[0,1,2,0,1,2,3]})
In [42]: frame
Out[42]:
          a  b    c  d
0 -0.661234  7  one  0
1  1.161592  6  one  1
2  0.697384  5  one  2
3 -0.937146  4  two  0
4  0.624776  3  two  1
5 -0.569641  2  two  2
6 -2.379362  1  two  3
In [43]: frame.set_index(['c','d']) # 对应的索引默认去除
Out[43]:
              a  b
c   d
one 0 -0.661234  7
    1  1.161592  6
    2  0.697384  5
two 0 -0.937146  4
    1  0.624776  3
    2 -0.569641  2
    3 -2.379362  1
In [44]: frame.set_index(['c','d'],drop=False) # 对应的列索引也不会去除
Out[44]:
              a  b    c  d
c   d
one 0 -0.661234  7  one  0
    1  1.161592  6  one  1
    2  0.697384  5  one  2
two 0 -0.937146  4  two  0
    1  0.624776  3  two  1
    2 -0.569641  2  two  2
    3 -2.379362  1  two  3
# 使用 reset_index()可回复原来的形式


# 比 ix切片索引更稳定、可靠，而且是基于位置的索引方式：
# Series : iget_values()   pandas新版本已经取消了这个
# DataFrame: irow、 icol		DataFrame也取消了这个

# In [51]: s = Series(range(3),index=[-5,1,3])
# In [54]: s.iget_value(2)
