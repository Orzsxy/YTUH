# -*- coding: UTF-8 -*-
import re
import os
'''
fileList = []

# Function can get *.xls/*.xlsx file from the directory
"""
dirpath: str, the path of the directory
"""
def _getfiles(dirPath):
    # open directory 
    files = os.listdir(dirPath)
    # re match *.xls/xlsx，you can change 'xlsx' to 'doc' or other file types.
    ptn = re.compile('.*\.fa')
    for f in files:
        # isdir, call self
        if (os.path.isdir(dirPath + '\\' + f)):
            getfiles(dirPath + '\\' + f)
        # isfile, judge
        elif (os.path.isfile(dirPath + '\\' + f)):
            res = ptn.match(f)
            if (res != None):
                fileList.append(dirPath + '\\' + res.group())
        else:
            fileList.append(dirPath + '\\无效文件')


# Function called outside
"""
dirpath: str, the path of the directory
"""
def getfiles(dirPath):
    _getfiles(dirPath)
    return fileList

if __name__ == "__main__":
     path = 'E:\\Pycoding\\编码'
     files = getfiles(path)
     print('.fa文件提取结果：')
     for f in fles:
         print(f)
'''
path = 'E:\Pycoding\str'
cpath = 'E:\Pycoding\删除后的'
pathn = 'E:\Pycoding\Addn'
files = os.listdir(path)
#print(len(files))
print(files)
def Indexs(strp,ch):
    '''找出>的所有索引'''
    ids = list() #全局变量
    st = strp
    i = -1
    length = len(st) 
    try:
        while st.index(ch,i+1,length) != -1: #find()
            i = st.index(ch,i+1,length)
            ids.append(i)
    except BaseException as e:
        #print(e)
        pass
    return ids

encodes = ['ATG','aTG','AtG','ATg','atG','Atg','aTg','atg','TGG','tGG','TgG','TGg','tgG','Tgg','tGg','tgg']
for file in files:
    with open(path+"/"+file,'r') as f:
        rna = f.readlines()
    with open(pathn+"/"+file,'w') as f:#写入添加换行的
        for string in rna:
            ids = Indexs(string,'>')
            l = len(ids)
           # print(l,ids)
            cnt=0
            if l == 0 :
                f.write(string)
            else:
                for i in ids:
                    if i!=0:
                        string = string[:i+cnt]+'\n'+string[i+cnt:]
                        cnt+=1
                f.write(string)
    with open(pathn+"/"+file,'r') as f:
        rna = f.readlines()
    with open(cpath+"/"+file,'w') as f:
        flag = 0
        for string in rna:
            if flag&1:
                for encode in encodes:
                    string  = string.replace(str(encode),'___')#string = re.sub(encode,'',string)
                string  = string.replace('___','')
                f.write(string)
            else:
                f.write(string)
            flag +=1

#修改字符除了用切片和能用连接:
chs = 'Asdcsdsdc'
chs=list(chs)
chs[5] = 'Q'
chs=''.join(chs)
print(chs)