import matplotlib.pyplot as plt
#导入3D包：
from mpl_toolkits.mplot3d import Axes3D
#创建坐标
X = [1,1,2,2]
Y = [3,4,4,3]
Z = [1,100,1,1]
#创建Axes3D
figure = plt.figure()
ax = Axes3D(figure)

ax.plot_trisurf(X,Y,Z)
plt.show()