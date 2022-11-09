# 开发时间：12/10/2022 下午4:49
import pandas as pd

df = pd.read_csv('./Global Hunger Index.csv')
print(df)
# for i in df:
#     print(i)

# print(df.index)
# print(df.shape)
# print(df.columns)
# print(df.values)
# print(type(df.values))  #<class 'numpy.ndarray'>
# print(df.dtypes)
# print(df.ndim)
# print(df.head())   #显示行信息，默认显示头5行
# print('*'*110)
# print(df.tail())   #显示后几行，默认显示后5行
# print(df.info())
 #   Column                      Non-Null Count  Dtype
# ---  ------                      --------------  -----
#  0   Entity                      471 non-null    object
#  1   Code                        471 non-null    object
#  2   Year                        471 non-null    int64
#  3   Global Hunger Index (2021)  471 non-null    float64
#  4   411773-annotations          12 non-null     object
# dtypes: float64(1), int64(1), object(3)
# memory usage: 18.5+ KB
# None

print(df.describe())  #数据为int或者float列的基本数据统计描述