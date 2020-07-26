import os
# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# 输入文件夹路径、空文件列表[]
# 返回 文件列表Filelist,包含文件名（完整路径）
p = "C:\\Users\\DELL\\Desktop\\Python_pdf"
def get_filelist(dir, Filelist):
	newDir = dir
	if os.path.isdir(dir):
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			get_filelist(newDir, Filelist)
	elif os.path.isfile(dir):
			Filelist.append(dir)
			#要是只需返回在路径下找到的文件名称:Filelist.append(os.path.basename(dir)) 在dir的文件目录没有文件的的候，就返回空值
	return Filelist
if __name__ =='__main__' :
	files = os.listdir(p) #listdir不会递归显示内容
	for f in files:
		print(f)
	list = get_filelist(p, []) #递归
	print(len(list))
	for e in list:
		print(e)
def get_filelist_walk(path):
	Filelist = []
	for home, dirs, files in os.walk(path):#walk能够实现递归
		for filename in files:# 文件名列表，包含完整路径
			Filelist.append(os.path.join(home, filename))
			# # 文件名列表，只包含文件名
			# Filelist.append( filename
	return Filelist
if __name__ =="__main__":
	Filelist = get_filelist_walk(p)
	print("walk")
	print(len( Filelist))
	for file in Filelist:
		print(file)