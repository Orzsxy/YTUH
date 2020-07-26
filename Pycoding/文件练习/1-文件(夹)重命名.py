import os;
import re;
def rename():
	path = 'C:\\Users\\DELL\\Desktop\\wp_icon\\P';
	filelist = os.listdir(path);
	i = 1
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
def rename1():
	path = 'C:\\Users\\DELL\\Desktop';
	mark = addinfo
	filelist = os.listdir(path); #不会递归调用，只显示path根目录下的内容
	for file in filelist:
		if file.endswith('.txt'):	#看是不是以txt结尾的文件。 	#if file != sys.argv[0]:可以用来判断此时读取的文件是不是当前的程序
			os.rename(file,mark+file)
fileList = []
def getfile_listdir(dirPath):
	# Function can get *.jpg 
    files = os.listdir(dirPath)
    # re match *.xls/xlsx，you can change 'xlsx' to 'doc' or other file types.
    ptn = re.compile('.*\.jpg')
    for f in files:
        # isdir, call self
        if (os.path.isdir(dirPath + '\\' + f)):
            getfile_listdir(dirPath + '\\' + f)
        # isfile, judge
        elif (os.path.isfile(dirPath + '\\' + f)):
            res = ptn.match(f)
            if (res != None):
                fileList.append(dirPath + '\\' + res.group())
        else:
            fileList.append(dirPath + '\\无效文件')
if __name__ == '__main__':
	pa = 'C:\\Users\\DELL\\Desktop\\wp_icon'
	getfile_listdir(pa)
	print("提取结果：")
	for f in fileList:
		print(f)


'''
def getfiles_walk(dirPath):
	#home,dirs,
	files = os.listdir(dirPath)
    ptn=re.compile('.*\.jpg')
    for f in files:
        res = ptn.match(f)
        if (res != None):
            fileList.append(dirPath + '\\' + res.group())
        else:
            fileList.append(dirPath + '\\无效文件')
if __name__ == '__main__':
	pa = 'C:\\Users\\DELL\\Desktop\\wp_icon'
	getfiles_walk(pa)
	print("提取结果：")
	for f in fileList:
		print(f)
#help(re.compile)
'''