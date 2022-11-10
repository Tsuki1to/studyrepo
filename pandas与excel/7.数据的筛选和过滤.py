# 开发时间：10/11/2022 下午3:27
import pandas as pd
file = './Score.xlsx'
Scores = pd.read_excel(file,index_col='ID')
Scores = Scores.loc[Scores.Age.apply(lambda x:18<=x<30)] \
         .loc[Scores.Score.apply(lambda x:85<=x<100)]
'''筛选年龄在18至30之间的，成绩在85至100之间的'''
print(Scores)