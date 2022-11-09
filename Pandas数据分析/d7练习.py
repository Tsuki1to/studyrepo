# 开发时间：13/10/2022 下午4:50
import pandas as pd
data = pd.read_csv('./dogNames2.csv')
# print(data.head())
# print(data.info())
#data.sort_values后跟by,表示哪个列进行排序
d1 = data.sort_values(by='Count_AnimalName',ascending=False) #ascending=False降序
#显示排序前五行
print(d1.head(5))
print('='*100)
#显示Dataframe中前20个数据
print(d1[:20])
print(d1[4:5])  #表示索引Dataframe中的第五条数据
print('='*100)
#显示Dataframe按照指定列和指定步移取值
#[]中是数字就是行索引
#[]中是字符串的话就是列索引
print(d1[:20]['Row_Labels'])