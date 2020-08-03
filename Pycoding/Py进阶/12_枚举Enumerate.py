#枚举Enumerate
my_list	=	['apple',	'banana',	'grapes',	'pear'] 
for i,value in enumerate(my_list): #不用enumerate只能访问元素，没有相应的索引
	print(i,value)
for i,value in enumerate(my_list,2): #enumerate后面的参数支持从对应的索引进行访问
	print(i,value) 