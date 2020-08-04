#用于数组的文件读取
#np.save() np.load()

# 以二进制形式
In [4]: arr = np.arange(10)
In [5]: np.save('save_arr',arr) # 默认下是以未压缩的二进制格式保存在扩展名.npy文件中，自动添加npy

In [7]: np.load('save_arr.npy') #加载
Out[7]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#保存多个数组：
In [10]: np.savez('save_arr',a=arr,b=arr)
In [12]: np.load('save_arr.npz')
Out[12]: <numpy.lib.npyio.NpzFile at 0x28e1d60b488>
In [13]: ans = np.load('save_arr.npz')
In [15]: ans['b']
Out[15]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [16]: ans['a']
Out[16]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#以本本形式读取：
arr =np.loadtxt('arrtext.txt',delimiter=',')
np.savetxt('arrtext.txt',delimiter=',') #写入到以，隔开的文本中
