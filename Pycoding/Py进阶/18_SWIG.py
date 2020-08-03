#SWIG
#SWIG http://www.swig.org/tutorial.html
#开发中不常用，当有⼀个C/C++代码库需要被多种语⾔调⽤时，考虑这种方法
#在shell中编译example.c :
unix % swig -python example.i
unix % gcc -c example.c example_wrap.c \
    -I/usr/local/include/python2.1
unix % ld -shared example.o example_wrap.o -o _example.so

#调用：
import example
example.fact(5)
example.my_mod(7,3)
example.get_time()
#'Sun Feb 11 23:01:07 1996'
