In [59]: data= pd.read_csv('examples\\ex5.csv')
In [60]: data
Out[60]:
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo

#  to_csv() 把数据写到文件：
In [61]: data.to_csv('out.csv')
# 以指定的分隔符写入到文件 (这儿sys.stdout指输出到屏幕)
In [69]: data.to_csv(sys.stdout,sep='|')
# 把 缺少的 数据项用 NULL 写入
In [70]: data.to_csv(sys.stdout,sep='|',na_rep='NULL')
# 不写入 行和例的标签：
In [70]: data.to_csv(sys.stdout,sep='|',na_rep='NULL',index=False,header=False)
# 只写如例的一部分cols已经被columns替换了：
In [71]: data.to_csv('out.txt',sep='|',na_rep='NULL',index=False,header=False,columnss=['a','b','c'])



# 上面都是DF的data,Series也有to_csv(): from_csv()

In [82]: date = pd.date_range('1/1/2000',periods=7) # date_range可以生成日期
In [83]: date
Out[83]:
DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
               '2000-01-05', '2000-01-06', '2000-01-07'],
              dtype='datetime64[ns]', freq='D')
In [86]: data = Series(range(7),index=date)
In [87]: data
Out[87]:
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
Freq: D, dtype: int64

#from_csv():
# In [94]: Series.from_csv('out.csv',parse_dates=True)
# 提示了没有这个方法，可以换成read_csv()



# IPython  中 to_csv() from_csv()相关文档