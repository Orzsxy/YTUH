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

