'''
项目中存在很多模块时，将功能类似的模块组织在一起，就形成了包，实现模块的导入
包本质上是一个有__init__()模块的文件夹！
包下面可以包含模块、子包，就像文件夹下面的子文件夹一样，子文件夹下面也必须有__init__()模块
'''
#包的使用
#import 包名.子包名1.子包名2.模块名   使用：这样导入在使用模块时必须有完整的名称，这种只能导入模块或者包，不能是变量、函数、类等对象
	# import a.aa.module 使用:a.aa.module.对象名()
#from 包名.子包名1.子包名2 import 模块名1，模块名2  使用:模块名.对象() 
	# from a.aa import module1,module2  使用：module1.对象名()
#from 包名.子包名1.子包名2.模块 import 对象名 使用： 对象名()
#不提倡 import *
#允许使用路径：
#from . import module 当前目录
#from .. import module 上级目录

#查看模块的搜索路径：
import sys
print(sys.path)

'''
顺序：
1. 内置模块 
2. 当前目录 
3. 程序的主目录 
4. pythonpath目录（如果已经设置了 pythonpath环境变量） 
5. 标准链接库目录 
6. 第三方库目录（site-packages 目录） 
7. .pth文件的内容（如果存在的话） 
8. sys.path.append()临时添加的目录
'''
