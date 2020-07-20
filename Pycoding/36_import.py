'''
import 模块名
import 模块1,模块2
import 模块名 as 模块别名
模块有四个类别：自己编写的.py文件、被共享的库或者DDL的C/C++扩展
包好一组模块的包
使用c编写并连接到Py解释器的内置模块
<class 'module'>
一个模块无论导入多少次都只有一个实列对象
'''
#导入模块的另一种内置函数:__import()__
m = __import__('math') #动态导入,py2 py3有差异
print(m.sin(0))
# 动态导入：
import importlib #无差异
a = importlib.import_module('math')
print(a.pi)

#import 自己写的py 
#上面弄的模块导入 会执行自己写的模块内容