# 开发时间：20/9/2022 上午10:57
#在本模块中导入calc模块
import calc   #使用方法要首先导入模块
print(calc.add(1,2))    #使用格式为：模块.方法（参数）
print(calc.jian(10,5))


print('---------------------------------------')
from calc import add
print(calc.add(9,87))



import calc2

print(calc2.add(10,20))