# 开发时间：10/11/2022 下午3:57
import pandas as pd
file = './multSheet.xlsx'
students = pd.read_excel(file,sheet_name='Sheet1',index_col="ID")
Scores = pd.read_excel(file,sheet_name='Sheet2',index_col="ID")
table = students.join(Scores,how='left').fillna(0)  #how= 意思为不论如何保留左边的表格
#fillna（）表示将nan中填充0
table.Score = table.Score.astype(int)
print(table)
