import pickle
#对数据进行序列化和反序列化
with open('log.dat','wb') as f:
	pickle.dump('张三',f);pickle.dump('李四',f)
	pickle.dump('王五',f)
with open('log.dat','rb') as f:
	a = pickle.load(f)
	b = pickle.load(f)
	print(id(a),a)
	print(id(b),b)


