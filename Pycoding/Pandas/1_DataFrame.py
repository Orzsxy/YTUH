#DataFrame
# 是一个表格型的数据结构，含有一组有序的例，每列可以是不同的数据类型，
# 既有行索引，又有列索引，
# DataFrame中的数据是一个或者多个 二维块存放的。

# 创建DataFrame,(还可以用字典的嵌套创建)
In [34]: data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    ...:         'year': [2000, 2001, 2002, 2001, 2002, 2003],
    ...:         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
In [35]: frame = pd.DataFrame(data)
In [36]: frame
Out[36]:
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2

#按照指定的列序列排序：
In [42]: DataFrame(data,columns = ['year','state','pop'],index=['one','two','there','four','five','six'])
Out[42]:
       year   state  pop
one    2000    Ohio  1.5
two    2001    Ohio  1.7
there  2002    Ohio  3.6
four   2001  Nevada  2.4
five   2002  Nevada  2.9
six    2003  Nevada  3.2
# 传入的例找不到会产生Nan:
In [37]: DataFrame(data,columns = ['years','state','pop'])
Out[37]:
  years   state  pop
0   NaN    Ohio  1.5
1   NaN    Ohio  1.7
2   NaN    Ohio  3.6
3   NaN  Nevada  2.4
4   NaN  Nevada  2.9
5   NaN  Nevada  3.2

#获取列索引：
In [39]: frame.columns
Out[39]: Index(['state', 'year', 'pop'], dtype='object')
In [40]: frame['year'] # 返回某一列，等价于Series格式：
Out[40]:
0    2000
1    2001
2    2002
3    2001
4    2002
5    2003
Name: year, dtype: int64

# ix获取某一行
In [48]: frame.ix[3]
Out[48]:
state    Nevada
year       2001
pop         2.4
Name: 3, dtype: object

# 增加一新的列：（frame['debt']会提示keyError)
In [51]: frame['debt'] = 16.5
In [52]: frame
Out[52]:
    state  year  pop  debt
0    Ohio  2000  1.5  16.5
1    Ohio  2001  1.7  16.5
2    Ohio  2002  3.6  16.5
3  Nevada  2001  2.4  16.5
4  Nevada  2002  2.9  16.5
5  Nevada  2003  3.2  16.5

In [59]: frame['debt'] = np.arange(6)
In [60]: frame
Out[60]:
    state  year  pop  debt
0    Ohio  2000  1.5     0
1    Ohio  2001  1.7     1
2    Ohio  2002  3.6     2
3  Nevada  2001  2.4     3
4  Nevada  2002  2.9     4
5  Nevada  2003  3.2     5

#也可以针对某一个Series（DataFrame都共用一个索引)进行赋值(也可以某一行)：
In [61]: var = Series([-1.3,5.5,7.7],index = [0,3,5])
In [62]: frame['debt']=var # 若对返回的Series进行修改会修改到DataFrame上
In [63]: frame
Out[63]:
    state  year  pop  debt
0    Ohio  2000  1.5  -1.3
1    Ohio  2001  1.7   NaN
2    Ohio  2002  3.6   NaN
3  Nevada  2001  2.4   5.5
4  Nevada  2002  2.9   NaN
5  Nevada  2003  3.2   7.7

# del 删除某一列：
In [64]: del frame['debt']
In [65]: frame
Out[65]:
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2


# 字典的嵌套创建DataFrame:
# 外层字典的键作为列索引，内层字典的键作为行索引
In [66]: pop = {'Nevada': {2001: 2.4, 2002: 2.9},
    ...:        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
In [67]: frame = DataFrame(pop)
In [68]: frame
Out[68]:
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2000     NaN   1.5

#实现转换：
In [69]: frame.T
Out[69]:
        2001  2002  2000
Nevada   2.4   2.9   NaN
Ohio     1.7   3.6   1.5

# 通过Series进行创建DataFrame
In [72]: pdata = {'Ohio':frame['Ohio'][:-1],
    ...: 'Nevada':frame['Nevada'][:2]}
In [73]: pd.DataFrame(pdata)
Out[73]:
      Ohio  Nevada
2001   1.7     2.4
2002   3.6     2.9

# 给行和列设置名称：
In [75]: frame.index.name = 'year';frame.columns.name = 'state'
In [76]: frame
Out[76]:
state  Nevada  Ohio
year
2001      2.4   1.7
2002      2.9   3.6
2000      NaN   1.5

# 索引 的 对象
# 被赋值的对象不能被修改
In [78]: index = frame.index
In [80]: index[::-1]
Out[80]: Int64Index([2000, 2002, 2001], dtype='int64', name='year')
In [84]: index[-1] = 1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
TypeError: Index does not support mutable operations

# Index的其他用法：
In [85]: i = pd.Index(np.arange(3))
In [86]: i
Out[86]: Int64Index([0, 1, 2], dtype='int64')
In [87]: ii = pd.Index(np.arange(6))
In [88]: ii
Out[88]: Int64Index([0, 1, 2, 3, 4, 5], dtype='int64')
In [89]: i.append(ii)
Out[89]: Int64Index([0, 1, 2, 0, 1, 2, 3, 4, 5], dtype='int64')
In [90]: i.diff(ii)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-90-62a408219e2a> in <module>
----> 1 i.diff(ii)  #计算差集
AttributeError: 'Int64Index' object has no attribute 'diff'

In [92]: pd.Index(i,ii)
Out[92]: Int64Index([0, 1, 2], dtype='int64')
In [93]: i.intersection(ii) # 计算交集  
Out[93]: Int64Index([0, 1, 2], dtype='int64')



