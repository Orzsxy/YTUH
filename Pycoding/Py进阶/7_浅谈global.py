def	add(value1,	value2):
	global	result				
	result	=	value1	+	value2 
add(2,	4)
print(result)
#最好不要使用global
#最常用的一种方法，返回多个值或者元组、列表
def	profile():				
	name	=	"Danny"				
	age	=	30				
	return	name,	age 
def	profile():
	name	=	"Danny"				
	age	=	30				
	return	(name,	age) 
profile_data	=	profile() 
print(profile_data[0]) #	Output:	Danny print(profile_data[1]) 