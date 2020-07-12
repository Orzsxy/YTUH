#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
#当后两个参数都为空时，等价于eval(expression)。
#当locals参数为空，globals参数不为空时，先查找globals参数中是否存在变量，并计算。
#当两个参数都不为空时，先查找locals参数，再查找globals参数。
#global必须是一个dict,locals不要求
a = 1
b = 2
d = dict(a=1,b=4)
f = eval('a+b',d)
print(f)