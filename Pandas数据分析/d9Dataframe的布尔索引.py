# 开发时间：14/10/2022 下午4:11
import pandas as pd
data = pd.read_csv('./dogNames2.csv')
print(data)
# 所有狗中名字出现频率大于800的名字
print(data[data['Count_AnimalName']>800])
# 所有狗中名字出现频率大于800并且小于1000的名字
print(data[(data['Count_AnimalName']>800) & (data['Count_AnimalName']<1000)] )
#当出现两个条件的时候，目标只有一个，不同的条件放在（）里
# &和  |或

#寻找狗名字中名字长度大于4并且使用频率大于700的名字
print(data[(data['Row_Labels'].str.len()>4) & (data['Count_AnimalName']>700)])