# 开发时间：20/9/2022 下午3:24
#包与目录之间的区别
#包 包含__init__.py文件
#目录里通常不包含__init__.py文件
'''
导入时使用规范
import 包名.模块名
'''
#在s14d4文件中导入package1中的模块A

import package1.modelA
print(package1.modelA.a)

#or
import package1.modelA as wa  #wa为前面地址的别名
print(wa.a)

'''
使用import导入的时候只能跟包名或者模块名
import package1
import calc
'''



'''
使用from  xxx  import xxx 时可以from包名Import模块名或者，from包名.模块名import函数/变量名
from package import modelA
from package1.modelA import a

'''