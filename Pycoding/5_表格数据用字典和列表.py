r1 = {'name':'张三','age':18,'city':'上海','money':'10k'}
r2 = {'name':'李四','age':20,'city':'北京','money':'15k'}
r3 = {'name':'王五','age':19,'city':'青岛','money':'16k'}
tb = [r1,r2,r3]
#找到第二行人的薪资
print(tb[1].get('money'))
#打印表中所有人薪资
for i in range(len(tb)):
	print(tb[i].get('money'))
#打印表中所有数据：
for i in range(len(tb)):
	print(tb[i].get('name'), tb[i].get('age'),tb[i].get('city'),tb[i].get('money'))
