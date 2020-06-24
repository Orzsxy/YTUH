clc, clear
load mydata51
c=c'; c=sparse(c);  %生成Matlab工具箱需要的稀疏矩阵
[d,p]=graphshortestpath(c,11,95,'Directed',0)
plot(xy(ind1,1),xy(ind1,2),'Pk','MarkerSize',10), hold on
text(xy(ind1,1)+10,xy(ind1,2),{str{1,ind1}})
plot(xy(ind2,1),xy(ind2,2),'*k','MarkerSize',10)
text(xy(ind2,1)+10,xy(ind2,2),{str{1,ind2}})
plot(xy(ind3,1),xy(ind3,2),'.k')
text(xy(ind3,1)+10,xy(ind3,2),{str{1,ind3}})
for i=1:length(p)-1
    plot(xy([p(i),p(i+1)],1),xy([p(i),p(i+1)],2),'LineWidth',1.5,'Color','k')
end
