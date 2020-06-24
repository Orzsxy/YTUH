%���Ƶ���


load('topo.mat','topo','topomap1')%���ص���߳�����,topo.mat,topo�Դ�������


contour(0:359,-89:90,topo,[0 0],'b')%���ƺ���Ϊ0�ĵȸ���
axis equal%���õȱ���������
box on%��ʾ�������
set(gca,'XLim',[0 360],'YLim',[-90 90], 'XTick',[0 60 120 180 240 300 360], 'Ytick',[-90 -60 -30 0 30 60 90]);%��������̶�

hold on%����ͼ�β�������
image([0 360],[-90 90],topo,'CDataMapping', 'scaled');%�ø߳����ݻ���ͼ��
colormap(topomap1);%�޸���ɫӳ���

[x,y,z] = sphere(50);%����һ����

cla reset%��ͼ����λ
axis square off%�رվ�������ϵ

%����Ϊ���û��Ƶ���Ĺ�������
props.AmbientStrength = 0.1;
props.DiffuseStrength = 1;
props.SpecularColorReflectance = .5; 
props.SpecularExponent = 20;
props.SpecularStrength = 1;
props.FaceColor= 'texture';
props.EdgeColor = 'none';
props.FaceLighting = 'phong';
props.Cdata = topo;
surface(x,y,z,props);%���Ƶ������
light('position',[-1 0 1]);%���ù���
light('position',[-1.5 0.5 -0.5], 'color', [.6 .2 .2]);%���ù���
view(3)%������ά�ӽ�
