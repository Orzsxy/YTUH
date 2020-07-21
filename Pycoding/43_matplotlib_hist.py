#柱状图是用来观察数据y的值的，柱状图是用来观察分布的，不关心某个具体的值
import matplotlib.pyplot as plt
import numpy as np
#randn生成1000个高斯分布的数据
x1 = np.random.randn(1000) #高斯分布
x2= np.random.normal(0,0.8,1000) #生成100个期望是0方差是0.8的数据
kwargs = dict(bins=100,alpha=0.3)
plt.hist(x1,**kwargs) #bins:生成多少个柱
plt.hist(x2,**kwargs) # **把数据全都展开

plt.show()