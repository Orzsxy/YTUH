#普通的对象赋值，就是对象内存地址的引用
a = ['a',['cs']]
print(id(a))
print(a)
print([id(value) for value in a])
b = a
print(id(b))
print(b)
print([id(value) for value in b])

a[0]='a_'
a[1].append(1)
print(a)
print([id(value) for value in a])
print(id(b))
print(b)

#浅拷贝
import copy
a = ['a',['cs']]
copy_a = copy.copy(a)
print('a_id:',id(a),'copy_a_id:',id(copy_a))
print('a:',a,'copy_a:',copy_a)
print('a_obj_id:',[id(value) for value in a],'copy_a_obj_id:',[id(value) for value in copy_a])
a[0] = 'a_'
copy_a[1].append('1')
print('a_id:',id(a),'copy_a_id:',id(copy_a))
print('a:',a,'copy_a:',copy_a)
print('a_obj_id:',[id(value) for value in a],'copy_a_obj_id:',[id(value) for value in copy_a])
'''
浅拷贝会创建一个新的对象，这个例子中”a is not copy_a”
但是，对于对象中的元素，浅拷贝就只会使用原始元素的引用（内存地址），也就是说”a[i] is copy_a[i]”

当对a进行修改的时候
由于list的第一个元素是不可变类型，所以a对应的list的第一个元素会使用一个新的对象地址
但是list的第二个元素是一个可变类型，修改操作不会产生新的对象，所以copy_a的修改结果与a的修改结果相同
'''
#产生浅拷贝的效果
'''
使用切片[:]
使用库函数(list/set/..)
使用copy
'''
#深拷贝
a = ['a',['cs']]
deepcp_a = copy.deepcopy(a)
print('a_id:',id(a),'deepcp_a_id:',id(copy_a))
print('a:',a,'deepcp_a:',deepcp_a)
print('a_obj_id:',[id(value) for value in a],'deepcp_a_obj_id:',[id(value) for value in copy_a])
a[0]='a_'
deepcp_a[1].append('1')
print('a_id:',id(a),'deepcp_a_id:',id(copy_a))
print('a:',a,'deepcp_a:',deepcp_a)
print('a_obj_id:',[id(value) for value in a],'deepcp_a_obj_id:',[id(value) for value in copy_a])
'''
跟浅拷贝类似，深拷贝也会创建一个新的对象，这个例子中”a is not deepcp_a”
但是，对于对象中的元素，深拷贝都会重新生成一份，而不是简单的使用原始元素的引用（内存地址）
对于可变对象也是生成新的对象，不在引用原有的对象地址
'''

'''
Python中对象的赋值都是进行对象引用（内存地址）传递
使用copy.copy()，可以进行对象的浅拷贝，它复制了对象，但对于对象中的元素，依然使用原始的引用.
如果需要复制一个容器对象，以及它里面的所有元素（包含元素的子元素），可以使用copy.deepcopy()进行深拷贝
对于非容器类型（如数字、字符串、和其他’原子’类型的对象）没有被拷贝一说
如果元组变量只包含原子类型对象，则不能深拷贝
'''
a = (10,20[5,6])
p