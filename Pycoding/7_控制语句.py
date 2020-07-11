#三元运算符： 条件为真时 if 条件 条件为假时
num = 10
print(num if num<10 else 'num大于等于10')

#测试多分支结构：
score = 10 #input("请输入分数：")
score = int(score)
if score<60:
	grade = '不及格'
elif 60<=score<80:
	grade = '及格'
elif 80<= score<90:
	grade = '良好'
elif 90<= score<=100:
	grade = '优秀'


r1 = {'name':'张三','age':18,'city':'上海','money':'10k'}
for x in r1.keys():
	print(x)

#100内所有奇数的和：
sum =0 
for x in range(1,100,2):
	sum += x
print('100内奇数和为{0},'.format(sum))