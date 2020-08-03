#一行式


#从⽂件打印出json数据，那么你 可以这么做：				
#cat	file.json	|	python	-m	json.tool

#脚本性能分析	这可能在定位你的脚本中的性能瓶颈时，会⾮常奏效：				
#python	-m	cProfile	my_script.py 
#备注：cProfile是⼀个⽐profile更快的实现，因为它是⽤c写的 

#过通过⽹络快速共享⽂件？好消息，Python为你提供了这样的功能。进⼊到你要 共享⽂件的⽬录下并在命令⾏中运⾏下⾯的代码：				
#	Python	2				
#python	-m	SimpleHTTPServer				
#	Python	3				
#python	-m	http.server 


#列表辗平 
#⽤itertools包中的itertools.chain.from_iterable
import itertools
a_list=[[1,	2],	[3,	4],	[5,	6]]
print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))
