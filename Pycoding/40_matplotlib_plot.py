import matplotlib.pyplot as plt
import numpy as np
 #plot绘制的图
#plt.plot([0,2],[0,4]) #(0,0)、（2，4）
x = [0,2,3,4,5]
y= [0,4,9,16,25]
#plt.plot(x,y,linewidth=1)#设置线条宽度
plt.title('function',fontsize=24) #标题及标题大小
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
#plt.savefig('新保存的图片.jpg')默认png
#绘制余弦正弦
x = np.linspace(0,10)
siny = np.sin(x)
cosy = np.cos(x)
plt.subplot(2,2,1) #给画布分区，先设置在画
plt.plot(x,siny)
plt.xlim(-1,1) #给图片坐标区间设置区域
plt.subplot(2,2,4)
plt.plot(x,cosy,'--g',label='--g') #线颜色默认顺序：蓝色、橘色
plt.legend(loc='upper left',fancybox=True,framealpha=1,shadow=False,borderpad=1) #默认在右上角添加label,loc='lower right','upper left
#fancybox:边框,framealpha：透明度,shadow：阴影,borderpad：边框宽度
plt.subplot(2,2,3)
np.random.seed(0) #随机数种子，每次产生的随机数都相同
x = np.random.rand(100) #生成100个点
y = np.random.rand(100)
size = np.random.rand(10)*1000 #生成10种大小，点的个数大于大小的个数，哪些点会循环绘制不同的大小
color = np.random.rand(100) #生成100种颜色，颜色的个数必须和点个数相同
plt.scatter(x,y,s=size,c=color,alpha=0.7) #alpha是透明度 #scatter绘制散点图，但是plot的效率要高一些
plt.show()
