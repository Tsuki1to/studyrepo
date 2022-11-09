# 开发时间：14/10/2022 下午2:46
import numpy as np
import pandas as pd
t1 = pd.DataFrame(np.arange(15).reshape(3,5),index=list('abc'),columns=list('vwxyz'))
print(t1)
# 4,a行，z列，输出数据类型为numpy,int
print(t1.loc['a','z'])
print('='*100)
#Dataframe中取行的索引，一下两个语句相同结果，输出结果为Series类型
print(t1.loc['a'])
print(t1.loc['a',:])
print('='*100)
#Dataframe中取列索引
print(t1.loc[:,'y'])
#Dataframe中选取两行
print(t1.loc[['a','c']])
#Dataframe中选取两列
print(t1.loc[:,['w','x']])
#Dataframe中选取固定行数和列数的数据
print(t1.loc['a':'c',['w','x']]) #loc方法中：步移法可以取到前后两个闭合
print('='*20,'loc是通过标签(表头)进行索引，而iloc是通过位置进行索引','='*20)
print(t1.iloc[:,[1,2]])
print(t1.iloc[[0,1],[0,2]])
print(t1.iloc[1:,:2])
t1.iloc[1:,:2] = 30  #可以通过具体位置索引进行赋值修改数据
print(t1)
t1.iloc[1,2] = np.nan
print(t1)
