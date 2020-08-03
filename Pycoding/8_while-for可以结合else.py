'''
for 和while可以结合else，在循环体正常结束时会执行else,若循环体被break结束 不会执行else，
'''
salary=[]
for i in range(4):
	x = intput('一共输入四名员工工资，输入Q、q退出')
	if x.upper()=='Q':
		print('录入完成，退出')
		break
	if float(x)<0:
		continue
	salary.append(x)
else:
	print('四名员工工资全部录入',salary)

# for else的应用场景，
#for循环结束的时机：循环中遇到break、for循环到结束
#现在有for循环结束了，想知道最终是因为break，还是循环到结束，需要进一步分析，使用for else，就可以直接看出是在哪儿结束
for n in range(2,10):
	for x in range(2,n):
		if(n%x==0):
			break;
	else:
		print(n,"is a prime number")




