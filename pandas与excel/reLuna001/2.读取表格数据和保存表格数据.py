# 开发时间：2/11/2022 下午3:01
import pandas as pd
import numpy as np
file_path  = './工作簿1.xlsx'
df = pd.read_excel(file_path)  #直接读取表格信息pd会在表格第一列自动添加序号index
#如果表格信息自带index的话添加，index_col = "表格自带的表头（clomns）"
# df = pd.read_excel(file_path,header=1)   规定表头从哪一行开始
# df.columns = ['姓名','卡号','身份证号','本金','息费合计']   当没有表头的时候设置表头
print(df)
df.to_excel('./银行贷款信息.xlsx')
print('done!')
