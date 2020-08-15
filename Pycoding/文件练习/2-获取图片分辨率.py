import os;
from PIL import Image


# filename = r'E:\data\yangben\0.jpg'
# img = Image.open(filename)
# imgSize = img.size #图片的长和宽
# print (imgSize)
# maxSize = max(imgSize) #图片的长边
#
# minSize = min(imgSize) #图片的短边
# print(maxSize, minSize)


def rename():
    path = 'E:\\wordpress\\wp_icon\\PP';
    filelist = os.listdir(path);
    i = 1031
    for file in filelist:
        oldir = os.path.join(path, file);  # join用来连接路径
        # imgfile = Image.open(oldir)  #不关闭下次会提示有进程仍然在访问
        with Image.open(oldir) as imgfile:
            imgSize = imgfile.size
        print(i,imgSize)
        if os.path.isdir(oldir):
            continue;
        pre_name,end_name = os.path.splitext(file); #可以splitest返回的是一个二元组，获取到文件名的名称、文件扩展名
        newdir = os.path.join(path,"Picture"+str(i)+'-'+str(max(imgSize))+'x'+str(min(imgSize))+end_name);#"Picture".join(str(i))+end_name)
        i += 1
        print(newdir)
        os.rename(oldir,newdir)


rename()