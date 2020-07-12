def outer():
	print("outering")
	def inner():
		print('innering')
	inner()#被嵌套的内部函数只能在在里面调用，这样可以实现：数据隐藏、封装、

outer()
