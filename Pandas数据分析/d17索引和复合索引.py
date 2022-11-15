# 开发时间：21/10/2022 下午4:13
import pandas as pd
import numpy as np

a = pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':list('hjklmno')})
print(a)  #设置一个数组4行分别有不同的值


#将c,d设置为数组a的索引并赋值给b(有两列索引，称为复合索引)
b = a.set_index(['c','d'])
print(b)

#c为带有两列复合索引的Series类型
c = b['a']
print(c)
print(type(c))  #<class 'pandas.core.series.Series'>
print(c['one']['j'])  #二级索引
print(c['one'])   #一级索引

#与b不同的是d将两个复合索引的位置换了一下
d = a.set_index(['d','c'])['a']
print(d)
#如果二级索引的值都相同，一级索引不相同只取相同的二级索引就会很麻烦
#这时候就需要swamplevel进行复合索引转换
#将较少的二级索引和一级索引调换
d = d.swaplevel()
print(d)
print(d['one']) #这样就可以简单的取到one的值


#在数组为Dataframe的时候只能使用loc下标进行索引
print(b)
print(b.loc['one'].loc['h'])

print(b.swaplevel().loc['h'])
'''不管是Series还是Dataframe，想输出内层索引的值，就要进行swaplevel，把索引进行交换'''
