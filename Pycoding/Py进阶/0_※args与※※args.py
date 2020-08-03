#*args与**kargs
#多余的参数都存在args中，只有一个*时
def	test_var_args(f_arg,*argv):				
	print("first	normal	arg:",	f_arg)				
	for	arg	in	argv:								
		print("another	arg	through	*argv:", arg) 
test_var_args('yasoob',	'python',	'eggs',	'test') ;
#	**kargs可以传递字典，
def	greet_me(**kwargs):				
	for	key,value in kwargs.items():
			print("{0}	=	{1}".format(key,value))
greet_me(name = "body");
karg = {'arg1' :1,'arg2': 2,'arg3' : 3 };
greet_me(**karg);
#################如果在参数中使用这三种不同的类型,他们的定义顺序：
def fun(agr,*args,**kargs)
