a	=	[(1,	2),	(4,	1),	(9,	10),	(13,	-3)]			
a.sort(key=lambda	x:	x[1])	#sort(key=None, reverse=False)
print(a)


list1=[1,2,3,4]
list2 =[9,7,6,4] 
data=zip(list1,list2)
sorted(data)	#data.sort() zip后再用sort() py3会有错，

