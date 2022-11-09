# 开发时间：21/10/2022 下午5:03
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)



file_path = './directory.csv'
df = pd.read_csv(file_path)
'''找到中国城市门店数量的排行'''
data1 = df[df['Country']=='CN'].groupby(by=['City']).count()['Brand'].sort_values(ascending=False)[:10]
print(data1)