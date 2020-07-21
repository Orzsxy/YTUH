#---encoding=utf-8---
import matplotlib.pyplot as plt
import numpy as np

#bar柱状图的宽度不是由width决定的，bar函数会根据二维坐标系的尺寸自动确定柱状图宽度，width指定的是这个标准宽度的倍数
#参数可以是浮点数
np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5,5,5)
print(x,y)
plt.subplot(1,2,1)
vbar = plt.bar(x,y) #返回每一个‘柱’
for bar,height in zip(vbar,y): #对每个y值小于0的颜色值设置为绿色
    if height<0:
        bar.set(color='green')
plt.axhline(0,color='blue',linewidth=2) #画布第一行中画一条水平蓝线
plt.subplot(1,2,2)
#barh将y和 x轴对换，
hbar = plt.barh(x,y,color='red')
plt.axvline(0,color='red',linewidth=2) #画布第一列中画一条垂直红线
plt.show()

#例二：
real_name=['千与千寻','将夜','熊出没']
real_num1 = [1000,2310,4301]
real_num2 = [2312,3454,6754]
real_num3 = [3232,2432,5432]

x= np.arange(len(real_name))
width=0.3 #分成三份
p1=plt.bar(x,real_num1,alpha=0.5,width=width)
p2=plt.bar([i+width for i in x],real_num2,alpha=0.5,width=width)
p3=plt.bar([i+2*width for i in x],real_num3,alpha=0.5,width=width)
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文乱码
x_label = ['第{0}天'.format(i+1) for i in x ]
plt.xticks([i+width for i in x],x_label)
plt.ylabel('score')
plt.title('这是个title')
plt.legend(handles=[p1,p2,p3],labels=real_name,loc='best')  #添加图例
plt.show()
'''
plt.legend( )中有handles、labels和loc三个参数，其中：
handles需要传入你所画线条的实例对象
labels是图例的名称（能够覆盖在plt.plot( )中label参数值）
loc代表了图例在整个坐标轴平面中的位置（一般选取'best'这个参数值）
'''


