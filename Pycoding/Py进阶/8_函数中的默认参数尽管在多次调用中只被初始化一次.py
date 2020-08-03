#函数中的默认参数尽管在多次调用中只被调用一次
def	add_to(num,	target=[]):
	target.append(num)				
	return	target 
print(add_to(1)) #	Output:	[1] 
print(add_to(2)) #	Output:	[1,	2] 
print(add_to(3)) #	Output:	[1,	2,	3]
#函数内使得每次来都创建一次
def	add_to(element,	target=None):
	if	target	is	None:						
		target	=	[]				
	target.append(element)				
	return	target 
print(add_to(1)) #	Output:	[1] 
print(add_to(2)) #	Output:	[2] 
print(add_to(3)) #	Output:	[3]