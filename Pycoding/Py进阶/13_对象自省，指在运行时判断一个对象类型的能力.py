#对象自省，指在运行时判断一个对象类型的能力
my_list = [4,1,2,3]
#dir返回一个列表，表示对应的对象所含含有的所有 属性 和 方法
print(dir(my_list))
print(sorted(my_list))
#还有 id type

#还有 inspect模块
import inspect
print(inspect.getmembers(str)) #查看对象的成员


#列表、元组、集合三种推导式很简单但是很重要放在下面:
#反转字典的键和值：{v:	k	for	k,	v	in	some_dict.items()}

