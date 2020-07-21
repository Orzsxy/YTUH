import matplotlib.pyplot as plt
import numpy as np
#绘制pyplot等高线图
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y) #计算 x,y相交的点，也就是相同的值。
Z = np.sqrt(X**2+Y**2) #绘制等高线就是xy相交的点在计算出z值
plt.contour(X,Y,Z) #绘制等高线图
plt.contourf(X,Y,Z) #会对空间部分进行填充
plt.show()


