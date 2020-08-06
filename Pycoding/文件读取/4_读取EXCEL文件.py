In [160]: xls_file = pd.ExcelFile('examples\\ex1.xlsx')
In [161]: table = xls_file.parse('Sheet1')  # 通过parse把微软的文件读取到DF中
In [162]: table
Out[162]:
   Unnamed: 0  a   b   c   d message
0           0  1   2   3   4   hello
1           1  5   6   7   8   world
2           2  9  10  11  12     foo
