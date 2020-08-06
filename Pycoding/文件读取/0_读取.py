# Linux下查看文件可用： ! cat ch06/ex1.csv
# Win 下查看			： ! type ch06\\ex1.csv		用两个是为了防止转义
#  !type ch06\\ex1.csv	也可


# 逗号隔开的文件格式读取到DF:pd.read_csv()
In [11]: df = pd.read_csv('examples\\ex1.csv')
In [12]: df
Out[12]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
# read_table可以以读取csv文件，需要sep设置分隔符
In [14]: df = pd.read_table('examples\\ex1.csv',sep=',')


# 并不是所有的文件第一行都有标题，
# 可以用pandas为其分配默认的列名,也可以自己定义列名：
# header=None 使用默认列名
In [24]: !type examples\\ex2.csv
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
In [25]: pd.read_csv('examples\\ex2.csv',header=None)#分配默认的列名
Out[25]:
   0   1   2   3      4
0  1   2   3   4  hello
1  5   6   7   8  world
2  9  10  11  12    foo

In [26]: pd.read_csv('examples\\ex2.csv',names=['a','b','c','d','message'])#分配默认的列名
Out[26]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

# 如果希望可以谋一列数据作为索引，或者某两列数据作为层次化的索引可以这样用：
In [27]: pd.read_csv('examples\\ex2.csv',names=['a','b','c','d','message'],index_col='message')# 用的索引名
Out[27]:
         a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12

In [28]: !type examples\\csv_mindex.csv
key1,key2,value1,value2
one,a,1,2
one,b,3,4
one,c,5,6
one,d,7,8
two,a,9,10
two,b,11,12
two,c,13,14
two,d,15,16
In [29]: pd.read_csv('examples\\csv_mindex.csv',index_col=['key1','key2']) # 按照顺序执行内外层索引结构
Out[29]:
           value1  value2
key1 key2
one  a          1       2
     b          3       4
     c          5       6
     d          7       8
two  a          9      10
     b         11      12
     c         13      14
     d         15      16

# 使用正则表达式自己编写固定的分隔符：
In [30]: list(open('examples\\ex3.txt')) 
Out[30]: # 原数据中的换行符被显示输出：
['            A         B         C\n',
 'aaa -0.264438 -1.026059 -0.619500\n',
 'bbb  0.927272  0.302904 -0.032399\n',
 'ccc -0.264273 -0.386314 -0.217601\n',
 'ddd -0.871858 -0.348382  1.100491\n']

In [31]: pd.read_table('examples\\ex3.txt',sep='\s+') # \s 是空格
Out[31]: # 因为列名比数据的行所在的列少，所以第一列被认为是DF索引
            A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491

# skiprows 忽略某一行的读取
In [32]: !type examples\\ex4.csv
# hey!
a,b,c,d,message
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
In [33]: pd.read_csv('examples\\ex4.csv',skiprows=[0,2,3])
Out[33]:
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

# 判断数据缺失项：NA -1 #IND NULL
In [40]: !type examples\\ex5.csv
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo

In [41]: result = pd.read_csv('examples\\ex5.csv')

In [42]: pd.isnull(result)
Out[42]:
   something      a      b      c      d  message
0      False  False  False  False  False     True
1      False  False  False   True  False    False
2      False  False  False  False  False    False

# 数据缺失的对应项，用Nan表示na_values可以接受值：

In [48]: result = pd.read_csv('examples\\ex5.csv',na_values=['NULL'])

In [49]: result
Out[49]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo

# 指定一些值赋值为NaN:

In [44]: s = {'message':['NA','foo'],'something':'two'}

In [45]: result = pd.read_csv('examples\\ex5.csv',na_values=s)

In [46]: result
Out[46]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       NaN  5   6   NaN   8   world
2     three  9  10  11.0  12     NaN

# 逐块读取文件（读取部分）

In [51]: result = pd.read_csv('examples\\ex6.csv')
In [52]: result
Out[52]:
           one       two     three      four key
0     0.467976 -0.038649 -0.295344 -1.824726   L
1    -0.358893  1.404453  0.704965 -0.200638   B
2    -0.501840  0.659254 -0.421691 -0.057688   G
3     0.204886  1.074134  1.388361 -0.982404   R
4     0.354628 -0.133116  0.283763 -0.837063   Q
...        ...       ...       ...       ...  ..
9995  2.311896 -0.417070 -1.409599 -0.515821   L
9996 -0.479893 -0.650419  0.745152 -0.646038   E
9997  0.523331  0.787112  0.486066  1.093156   K
9998 -0.362559  0.598894 -1.843201  0.887292   G
9999 -0.096376 -1.012999 -0.657431 -0.573315   0
[10000 rows x 5 columns]

In [54]: result = pd.read_csv('examples\\ex6.csv',nrows=5)
In [55]: result
Out[55]:
        one       two     three      four key
0  0.467976 -0.038649 -0.295344 -1.824726   L
1 -0.358893  1.404453  0.704965 -0.200638   B
2 -0.501840  0.659254 -0.421691 -0.057688   G
3  0.204886  1.074134  1.388361 -0.982404   R
4  0.354628 -0.133116  0.283763 -0.837063   Q


In [56]: result = pd.read_csv('examples\\ex6.csv',chunksize=1000)
In [57]: result
Out[57]: <pandas.io.parsers.TextFileReader at 0x26574335a48>
# 对读取的块逐行迭代
tot = Series([])   
for piece in result:
	tot = tot.add(piece['key'].value_counts(),fill_values=0)
tot = tot.order(ascending=False)
In [] : tot[:5]
Out[]:
E 368
X 364
L 346
Q 340
M 338
