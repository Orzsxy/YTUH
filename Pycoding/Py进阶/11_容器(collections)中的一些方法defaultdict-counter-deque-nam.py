#容器(collections)中的一些方法defaultdict-counter-deque-namedtuple-enum.Enum

#defaultdict
#不同于dict，不用检查某一个key存不存在
#字典中对⼀个键进⾏嵌套赋值时，如果这个键不存 在，会触发keyError异常。	
#defaultdict允许我们⽤⼀个聪明的⽅式绕过这个问题
from collections	import	defaultdict 
colours	=	(				
	('Yasoob',	'Yellow'),				
	('Ali',	'Blue'),				
	('Arham',	'Green'),				
	('Ali',	'Black'),				
	('Yasoob',	'Red'),				
	('Ahmed',	'Silver'), )
cnt	=	defaultdict(list) 
for name,color in colours:
	cnt[name].append(color)
print(cnt)

import	collections 
tree	=	lambda:	collections.defaultdict(tree) 
some_dict = tree()
some_dict['colours']['favourite']	=	"yellow" 
#以⽤json.dumps打印出some_dict:
import json
print(json.dumps(some_dict)) 

# Counter 是一个计数器，
from collections	import	Counter 
favs	=	Counter(name	for	name,	colour	in	colours) 
print(favs) 

#deque提供了⼀个双端队列，
from collections import deque 
d = deque()
d.append('1')
d.append('2')
d.append('3')
print(len(d))
print(d[0])
print(d[-1])

d = deque(range(5))
print(d.popleft())
print(d.pop())
d = deque(maxlen = 10) #deque可以限制大小
d = deque([1,2,3,4,5])
d.extendleft([-1,0]) #而且是先存储 -1，在存储0
d.extend([6,7,8])
print(d)

#命名元组 (namedtuples)
#可以像字典(dict)⼀样访问namedtuple， 但namedtuples是不可变的
from collections import namedtuple
Animals = namedtuple('a','name,age,type') #namedtuple有两个关键字，第一个是要创建的命名元组的名称(通常和等号右面的值一样），第二个是命名元组的字段
perry = Animals(name = 'perry',age = 31,type = 'cat')
print(perry)
print(perry[0])#支持索引访问
print(perry._asdict()) #把明明元组转换为字典

#枚举，在py3.4中才有的,但不属于collectios
from enum import Enum
class	Species(Enum):				
	cat	=	1				
	dog	=	2				
	horse	=	3				
	aardvark	=	4				
	butterfly	=	5				
	owl	=	6				
	platypus	=	7				
	dragon	=	8				
	unicorn	=	9
	kitten	=	1		#	(译者注：幼⼩的猫咪)				
	puppy	=	2		
Animal	=	namedtuple('Animal',	'name	age	type') 
perry	=	Animal(name="Perry",	age=31,	type=Species.cat) 
drogon	=	Animal(name="Drogon",	age=4,	type=Species.dragon) 
tom	=	Animal(name="Tom",	age=75,	type=Species.cat) 
charlie	=	Animal(name="Charlie",	age=2,	type=Species.kitten) 
print(tom.type == charlie.type)
#可以有三种方式访问枚举的对象
print(Species.dog)
print(Species(1))#第一个出现的
print(Species['cat'])
