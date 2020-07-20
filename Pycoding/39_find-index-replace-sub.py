import re
chs = "ABCDEFGHIJKLMNOPQCDRSTUVWXYCDZ"
print ('A' in chs)
#find()
chs.find('CD',0,len(chs)) #找不到返回-1
#rfind(),返回最后一次出现的位置
print(chs.rfind('CD',0,len(chs)))
#index(),没有找到会抛出异常
chs.index('CD', 0, len(chs))
#rindex()最后的位置
chs.rindex('CD',0,len(chs))
#在一个元素中没有找到所有对应字符索引的方法
#index:
i=-1
ids=list()
try:
	while chs.index('CD',i+1,len(chs)): 
		i = chs.index('CD',i+1,len(chs))
		ids.append(i)
except BaseException as e:
    print(e)
print(ids)
#多个元素中找出元素为1的索引
X=[1,2,3,1,4]
id1 = [i for i,x in enumerate(X) if x==1]

#replace(str, replaceText, max)  str:被替换字符, replaceText:替换字符, max:最大次数,不填入为全部
s = '/n123/n456/n789'
print(s.replace('/n','',2))
print(s.replace('/n',''))
#re.sub((str, replaceText, string) str:被替换多个字符, replaceText:替换字符, string:替换操作的字符串
print(re.sub('/n','',s))
#strip()、去除字符串的 首尾 字符，直到没有匹配的字符
chs = 'saaaay yes no yaaaass'
print(chs.strip('sya'))#去除首尾中所有's' 'y' 'a' 的，直到不能匹配,是按照单个字符处理的
#同理，lstrip用于去除左边的字符，rstrip用于去除右边的字符。
