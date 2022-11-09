# 开发时间：9/11/2022 上午11:27
import glob
import pandas as pd
path = './书'
'合并多个文件'
all_file = glob.glob(path+'/*.xlsx')
all_data=[]
for filename in all_file:
    df = pd.read_excel(filename,index_col=None,header=0)
    all_data.append(df)
data2 = pd.concat(all_data,ignore_index= True)   #ignore_index意思是不同添加新的索引
print(data2)
# data2.to_excel('./书/output1.xlsx')
print('搞定')