#coding=utf-8
import traceback
try:
	print(2)
	a = 3/0
	print(1) #发生错误之后就不再执行了
except BaseException as e:
	print(0)
	print(e)
	print(type(e))

while True:
	try:
		x = int(input('请输入一个数字：'))
		print('输入的数字：{0}'.format(x))
		if x==0:
			break;
	except BaseException as e:
		print(e)

try:
	while True:
		x = int(input('请输入一个数字：'))
		print('输入的数字：{0}'.format(x))
		if x == 0:
			break;
except BaseException as e:
	print(e)
except ValueError: #try 出多个 exception,但是ValueError类型没有子类
	print(e)

##把异常输出到文件,这时候异常后面的程序仍然可以执行
try:
	print(1)
	a = 1/0
except :
	with open('E:\Pycoding\log.txt','a') as f:
		traceback.print_exc(file = f)

##try...except..else结构
try:
	print(1)
	a = 1/1
except BaseException as e:
	print(2)
else:
	print('没有错误执行这儿')
##try...except...finally结构,不管是否发生异常,finally结构都执行,通常用来释放try中申请的资源
try:
	f = open('E:\Pycoding\lg.txt','r')
	conest = f.readline()
	print(conest)
except:
	print('文件没有找到')
finally:
	print('释放资源')
	try:
		f.close()
	except BaseException as e:
		print(e)
##with 结构，with常用在文件管理、网络通讯时的开发，不是用来取代try..except..finally结构的，
with open('E:\Pycoding\log.txt','r') as f:
	print(f.readline())

## traceback打印错误信息
try:
	print(1)
	a = 1/0
except:
	#traceback.print_exc() #Traceback 错误日志就是这个方法调用的
	with open('E:\Pycoding\log.txt','a') as f:  #open中第二个参数： r读 w覆盖写 a追加写
		traceback.print_exc(file = f)

#自定义异常类，raise抛出异常
class AgeError(Exception):#继承异常类
	def __init__(self,msg):
		Exception.__init__(self)
		self.errormsg = msg
	def __str__(self):
		return str(self.errormsg)
if __name__ == "__main__": ## ??
	age = int(input('输入年龄：'))
	if age<1 or age>100:
		raise AgeError(age)
	else:
		print('年龄：',age)
'''
SyntaxError 语法错误
NameError   访问没有声明的对象
ZeroDivisionError 除0错误
ValueError  数值错误
TypeError   类型错误
AttributeError 属性错误
IndexError  索引错误
KeyError	字典的关键字不存在
ImportError 导入对象/模块错误
GeneratorError 生成器发生异常
'''