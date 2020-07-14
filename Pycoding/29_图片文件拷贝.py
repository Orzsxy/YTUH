with open('school.jpg','rb') as f:
	with open('cpschool.jpg','wb') as w:
		w.writelines(f.readlines())

with open('school.jpg','rb') as f:
	with open('cpschool.jpg','wb') as w:
		for li in f.readlines():
			w.write(li)  #write()参数是字符串

   

   