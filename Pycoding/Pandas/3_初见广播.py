#初见广播
In [85]: arr = np.arange(12.).reshape((3, 4))
In [86]: arr
Out[86]:
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])
In [87]: arr[0]
Out[87]: array([0., 1., 2., 3.])
In [88]: arr-arr[0]
Out[88]:
array([[0., 0., 0., 0.],
       [4., 4., 4., 4.],
       [8., 8., 8., 8.]])

# DataFream与Series 之间的运算是把 Series的索引匹配到DataFream上(axis=1,这是默认的情况，在行上广播)，然后向下广播
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
    ...:                      columns=list('bde'),
    ...:                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0] 		# 相当于 .ix[0]
In [92]: frame - series		
Out[92]:
          b    d    e
Utah    0.0  0.0  0.0
Ohio    3.0  3.0  3.0
Texas   6.0  6.0  6.0
Oregon  9.0  9.0  9.0

# DataFrame 与 Series 运算时 （分别是列索引和行索引,找不到时，会重新索引形成并集)
series2 = pd.Series(range(3), index=['b', 'e', 'f'])

In [95]: frame + series2
Out[95]:
          b   d     e   f
Utah    0.0 NaN   3.0 NaN
Ohio    3.0 NaN   6.0 NaN
Texas   6.0 NaN   9.0 NaN
Oregon  9.0 NaN  12.0 NaN

# 若想在列上广播（axis=0):
In [97]: series3
Out[97]:
Utah       1.0
Ohio       4.0
Texas      7.0
Oregon    10.0
Name: d, dtype: float64
In [99]: frame
Out[99]:
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0
In [100]: frame.sub(series3,axis=0) # 在列上广播
Out[100]:
          b    d    e
Utah   -1.0  0.0  1.0
Ohio   -1.0  0.0  1.0
Texas  -1.0  0.0  1.0
Oregon -1.0  0.0  1.0