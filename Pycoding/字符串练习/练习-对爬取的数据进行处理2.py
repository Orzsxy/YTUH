 # -*- coding: UTF-8 -*-
import re
import os

def Indexs(strp,ch):
    '''在strp找出ch的所有索引'''
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

with open('writeress.txt','r',encoding='UTF-8') as f:
	string = f.readlines()

with open('writeress.txt','w',encoding='UTF-8') as f:
	cnt = 1 
	#第一次处理：
	# for stri in string:		
	# 	if "title=\"\"" not in stri:
	# 		f.writelines(stri)
	#第二次处理：
	# for stri in string:
	# 	tdids = Indexs(stri,'<td>')
	# 	td1ids = Indexs(stri,'</td>')
	# 	stri = stri.replace(stri[tdids[4]:td1ids[4]+5],'')
	# 	stri = stri.replace(stri[tdids[2]:tdids[3]],'')
	# 	f.writelines(stri)
	# #第三次处理：
	# reps = ['<tr>','<td>','</td>','<a href=\"','target=\"_blank\">','</a>','</tr>','\"']
	# for stri in string:
	# 	for rep in reps:
	# 		stri=stri.replace(rep,'                                        ')
	# 	# print(stri)
	# 	f.writelines(stri)	
	# #第四次处理：
	# for stri in string:
	# 	stri = stri.replace(stri[0:75],'')
	# 	f.writelines(stri)	
	# #第五次处理：
	# for stri in string:
	# 	httpids = Indexs(stri,'http')
	# 	if len(httpids)==2 :
	# 		stri=stri.replace(stri[httpids[1]:httpids[1]+70],'  ') #stri = re.sub(stri[l:r],'   ',stri)#
	# 	elif len(httpids)>2:
	# 		pass
	# 	f.writelines(stri)
	# #第6次处理：
	# for stri in string:
	# 	stri = re.sub('               ','',stri)
	# 	f.writelines(stri)	 
	# #第7次处理：
	# for stri in string:
	# 	stri = re.sub('复制这段内容后打开百度网盘手机App，操作更方便哦','',stri)
	# 	f.writelines(stri)	 




