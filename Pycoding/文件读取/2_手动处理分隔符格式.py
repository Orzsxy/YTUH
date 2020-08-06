# 手动处理分隔符格式
In [104]: ! type examples\\ex7.csv
"a","b","c"
"1","2","3"
"1","2","3"

In [105]: import csv
In [107]: f = open('examples\\ex7.csv')
In [108]: reader = csv.reader(f)			# 一次性读，第二次需要重新读
In [109]: reader
Out[109]: <_csv.reader at 0x2657469ef98>
In [110]: list(reader)
Out[110]: [['a', 'b', 'c'], ['1', '2', '3'], ['1', '2', '3']]


In [129]: f = open('examples\\ex7.csv')
In [130]: reader = list(csv.reader(f))
In [131]: header,values = reader[0],reader[1:]
In [132]: data_dict = {h:v for h,v in zip(header,zip(*values))}   # values：[['1', '2', '3'], ['1', '2', '3']] header: ['a', 'b', 'c']  每个列表的第一个压缩在一块
In [133]: data_dict 
Out[133]: {'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}


# 只要定义出csv.Dialect 的子类就可以定义出新的分割格式。
# https://stackoverflow.com/questions/45840330/python-typeerror-quoting-must-be-an-integer

In [143]: class my_dialect(csv.Dialect):
     ...:     lineterminator = '\n'
     ...:     delimiter = ';'
     ...:     quotechar ='"'
     ...:     quoting = csv.QUOTE_MINIMAL
     ...:
     ...:
In [144]: reader = csv.reader(f,dialect=my_dialect)
In [145]: reader
Out[145]: <_csv.reader at 0x2657469e898>
# reader中的参数也可以不写成子类形式，直接传参
In [146]: reader = csv.reader(f,delimiter='|')

# 写入文件：
with open('.csv','w') as f:
	writer = csv.writer(f,dialect = my_dialect)
	writer.writerow(('o','n','w'))
	writer.writerow(('1','2','3'))
	