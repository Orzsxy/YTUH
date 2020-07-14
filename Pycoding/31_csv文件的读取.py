'''
逗号分隔符文本格式，用在数据交换，数据库文件导入导出：
csv文件比excel的不同：
值没有类型，都是字符串
不能指定字体颜色样式
不能指定单元格样式，不能合并单元格
没有多个工作表
不能嵌入图像图表
'''
import csv
with open('dd.csv','r') as f:
	a = csv.reader(f)
	print(a)
	for value in a:
		print(value)
	print(list(a)) #生成器只能引用一次

#写入
with open('wcsv.csv','w') as f: #运行时不能打开文件
	wcsv = csv.writer(f) #得到文件的一个写入器
	wcsv.writerow(['ID','姓名','年龄'])

	al = [['1','张三','19'],[2,'李四',10]]
	wcsv.writerows(al)