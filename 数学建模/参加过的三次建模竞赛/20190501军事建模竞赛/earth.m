%绘制地球


load('topo.mat','topo','topomap1')%加载地球高程数据,topo.mat,topo自带的数组


contour(0:359,-89:90,topo,[0 0],'b')%绘制海拔为0的等高线
axis equal%设置等比例坐标轴
box on%显示坐标框线
set(gca,'XLim',[0 360],'YLim',[-90 90], 'XTick',[0 60 120 180 240 300 360], 'Ytick',[-90 -60 -30 0 30 60 90]);%设置坐标刻度

hold on%保持图形不被覆盖
image([0 360],[-90 90],topo,'CDataMapping', 'scaled');%用高程数据绘制图像
colormap(topomap1);%修改颜色映射表

[x,y,z] = sphere(50);%生成一个球

cla reset%绘图区复位
axis square off%关闭矩形坐标系

%以下为设置绘制地球的光照属性
props.AmbientStrength = 0.1;
props.DiffuseStrength = 1;
props.SpecularColorReflectance = .5; 
props.SpecularExponent = 20;
props.SpecularStrength = 1;
props.FaceColor= 'texture';
props.EdgeColor = 'none';
props.FaceLighting = 'phong';
props.Cdata = topo;
surface(x,y,z,props);%绘制地球表面
light('position',[-1 0 1]);%设置光照
light('position',[-1.5 0.5 -0.5], 'color', [.6 .2 .2]);%设置光照
view(3)%设置三维视角
