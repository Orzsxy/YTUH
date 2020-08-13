# -*- coding: UTF-8 -*-
import re
import os

def Indexs(strp,ch):
    '''找出ch的所有索引'''
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

with open('res.html','r',encoding='UTF-8') as f:
	string = f.read()
	# string = list(string)

with open('CPwriteress.html','w',encoding='UTF-8') as f:
	lids = Indexs(string,'<tr') # 有的是<tr action='..'>,所以不能用<tr>
	rids = Indexs(string,'</tr>')
	length = len(lids)
	rength = len(rids)
	print(length)

	for lid,rid in zip(lids,rids):
		if(string[lid:(lid+10)] in "<tr class=\"active\">") or (string[lid:(lid+5)] in "<tr>\";"):
			pass
		else:
			f.write(string[lid:(rid+5)]+"\n")
