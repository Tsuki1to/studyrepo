# 开发时间：21/10/2022 下午5:17
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
'''呈现出中国每个城市的门店数量'''

file_path = './directory.csv'
df = pd.read_csv(file_path)
df = df[df['Country']=='CN']
