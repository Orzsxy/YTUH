#coding=utf-8
#文本文件只能是用记事本打开的。wor编辑的文档是二进制文件，还包括视频、图片

# open(,param),param有属性 r w a b(二进制文件) +(读和写两种模式) b和+都是可以和两外几种组合,+的用法是 a+ w+ r+ ...
#win操作系统默认是编码是 GBK；linux系统文件编码使用的是 utf-8
f =  open('t.txt','a',encoding='GBk')  #保存时使用的编码格式
f.write('测试')
f.close()

# with上下文管理器:不论什么原因跳出with块，都能确保文件关闭，执行完之后回到之前的现场
s = ["张三\n",'李四','王五\n'] #列表可以被写入,\n被自动转为换行
with open('E:\Pycoding\log.txt','a') as f:
    f.writelines(s) #write()不能 写list,但也是写入后换行

#按照字节读取文件
with open('E:\Pycoding\log.txt','r') as f:
    print(f.read(4)) #读取文件，按照字符个数，不写默认读取整个文件
#按照行读取文件，读取到文件末尾返回空串
with open('E:\Pycoding\log.txt','r') as f:
    while True:
        fragment = f.readline()
        if not fragment:
            break
        else:
            print(fragment,end=' ')
#按照行读取文件，每一行的内容作为一个字符串，放在列表中，最后返回一个列表
with open('E:\Pycoding\log.txt','r') as f:
    print(f.readlines())

#也可以这样按行读取:使用迭代器，每次返回一行
with open('E:\Pycoding\log.txt','r') as f:
    for st in f:
        print(st,end=' ')

#文件对象的一些属性：
with open('log.txt','rb') as f:
    print('文件名称是:{0}'.format(f.name)) #文件名：name
    print(f.tell()) # tell()返回文件指针的当前位置
    print(f.readline())
    print(f.tell())#读取一行后指针在文件中的位置,GBK中汉字占3个字节tell按照字节来的
    print(f.seek(-10,2)) #有时候这个会经常报错，因为没有用二进制格式打开的文件之只支持，从头的位置进行读取。
    #在模式中加上b的格式就可以了使用另外两种模式了
