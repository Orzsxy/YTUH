import matplotlib.pyplot as plt
import numpy as np
boy = 100
girl = 200
boyp = boy/(boy+girl)
girlp = 1-boyp
labels=['boy','girl']
colors = ['blue','red']
plt.rcParams['font.sans-serif']=['SimHei']
#返回三个参数：
paches,texts,autotexts=plt.pie([boyp,girlp],labels=labels,colors=colors,explode=(0,0.05),autopct='%.1f %%')
#explode是中间进行隔开,autopct是精确度

#设置饼状图中的字体颜色
for text in autotexts:
    text.set_color('white')
#设置标签字体大小
for text in texts:
    text.set_fontsize(15)
#设置标签字体大小+饼状图中的字体大小
for text in texts+autotexts:
    text.set_fontsize(20)
plt.show()