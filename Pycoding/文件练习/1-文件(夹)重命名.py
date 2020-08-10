import os;
import re;
def rename():
	path = 'C:\\Users\\DELL\\Desktop\\wp_icon';
	filelist = os.listdir(path);
	i = 32
	for file in filelist:
		oldir = os.path.join(path,file);#join用来连接路径
		if os.path.isdir(oldir):
			continue;
		pre_name,end_name = os.path.splitext(file); #可以splitest返回的是一个二元组，获取到文件名的名称、文件扩展名
		newdir = os.path.join(path,"Picture"+str(i)+end_name);#"Picture".join(str(i))+end_name)
		i += 1
		os.rename(oldir,newdir)
rename()
'''join():(os.path中的)
os.path.join()函数：连接两个或更多的路径名组件

                         1.如果各组件名首字母不包含’/’，则函数会自动加上

　　　　　　　　　2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃

　　　　　　　　　3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾
'''
'''splitext():
path='D:/User/wgy/workplace/data/notMNIST_large.tar.gar'
os.path.splitext(path)会返回    (D:/User/wgy/workplace/data/notMNIST_large.tar,.gar)
'''
'''rename(src,drc) 分别是原来的路径(文件名)、换之后的路径(文件名)
如果drc未改之前已经存在了，会返回错误(不能出现两个重名的)
'''
