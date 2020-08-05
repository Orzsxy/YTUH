import matplotlib.pyplot as plt
import numpy as np

# 或者通过subplot返回的AxesSubplot对象，直接用对象调用对应的方法就可以直接在相应的subplot上绘图：
fig = plt.figure()  # 创建一个面板，所有的绘图都是在这上面进行的,此实出现一个空的面板
#不能通过figure绘图，必须用add_subplot 创建一个或者多个subplot在这上面进行

#后来又出现了plt.subplots()简便的方法，可以创建一个figure,并且返回一个含有已经创建的subplot对象的数组
# 可以通过对应的一维或二维数组索引对subplot进行绘制
fig,axes = plt.subplots(2,3)

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

plt.plot(np.random.randn(50).cumsum(),'k--') # 此实的的绘图就在最后一次用过的subplot上面进行绘图(ax3)

# 默认会在subplot外围留下一定的边距，subplot之间也会有间距，间距和图像的宽度、高度有关，在调整了图像的大小后间距也会自动调整大小。
# 利用顶级函数：subplots_adjust(left=None,bottom=None,right=None,top = None,wspace=None,hspace=None) 调整间距的大小
# wspace hspace 控制高度和宽度的百分比，可以用作subplot之间的宽度。
fig,axes =plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True,figsize=(8,6))
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
plt.subplots_adjust(wspace=0,hspace=0) # subplot之间的间距变为0

#plot接受一组X和Y坐标，还可以接受表示颜色和线性的字符串缩写：
ax.plot(x,y,'g--')
#或者是：
ax.plot(x,y,linestyle='--',color='g')
#常用的颜色有缩写词，使用其他常用的颜色可以用RGB值:#CECEE

#在绘制连续的线型图时不太容易看到关键点的位置，可以在格式符串中加上带有标记的类型：
#标记的类型和线型一定要放在颜色后面:
plt.plot(np.random.randn(30).cumsum(),'ko--')
#或者是：
plt.plot(np.random.randn(30),color='k',linestyle='dashed',marker='0')

#在线型图中，非实际的点默认时按照线性方式插入的，可以通过drawstyle选项修改：
data = np.random.randn(30)
plt.plot(data,'k--',label='Default')
plt.plot(data,'k-',drawstyle='steps-post',label='step-post')
plt.legend(loc='best') # Figure_1.png

plt.xlim([0,10]) #会将x轴的范围设置为0-10
plt.xlim() #根据数据的返回设置x轴

#设置轴标签、标题、刻度、刻度标签
xa = fig.add_subplot(1,1,1)
xa.plot(np.random.randn(1000).cumsum()) # Figure_2.png
xa.set_xticks([0,250,500,750,1000])
labels = xa.set_xticklabels(['one','two','three','four','five'],rotation =30,fontsize='small' )
xa.set_title('My first matplotlib plot')
xa.set_xlabel('Stages') # Figure_3.png   设置y轴上的只把上面的x改成y就可以

# 创建图例：
fig = plt.figure()  # Figure_4.png
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(),'k',label='one')
ax.plot(np.random.randn(1000).cumsum(),'k--',label='two')
ax.plot(np.random.randn(1000).cumsum(),'k.',label='three')
ax.legend(loc = 'best')  #loc说明图列最好的放置位置， 从图例中去除一个霍多尔元素时，不使用label或者传入 label='_nolegend_'

# 注解
# 通过 text、arrow、annotate、 添加
# text可以将文本绘制在图标上的指定坐标(x,y)



# 图形的绘制：
fig = plt.figure(figsize=(12, 6)); ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3) # b蓝色
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],  # 都是以从图形最下面一个以逆时针方向进行的
                   color='g', alpha=0.5) # g 绿色
ax.add_patch(rect) #创建的图形对象都是要放在块中， 完整块集合在matplotlib.patches 中
ax.add_patch(circ)
ax.add_patch(pgon) # Figure.png


# 将图表保存在文件中
# 保存到格式只要指定对应的扩展名就可以
plt.savefig('figpath.png',dpi = 400, bbox_inches = 'tight') # dpi是像素的分辨率， bbox_inches 指代保留的图表周围的空白部分，tight(最小白边）

# 没必要保存在磁盘，保存在缓冲区，用于在web上显示
from io import StringIO
buffer = StringIO()
plt.savefig(buffer)
plot_data = buffer.getvalue() #

#savefig() 参数：
# fname                 可以是含有路径的文件名
# dpi
# facecolor、 edgecolor 图象的背景色
# format                显示设置图象的文件格式
# bbox_inches


# matplotlib 自带一些设置， 通过这组全局参数自定义，管理图象大小，subplot,配色，字体大小，等
# rc方法：
plt.rc('figure',;figsize=(10,10))
figure_option={
    'family': 'monospace',
    'weight': 'bold',
    'size':'small'
}
plt.rc('font',**font_options)
