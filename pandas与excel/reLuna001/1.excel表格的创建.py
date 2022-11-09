# 开发时间：2/11/2022 下午2:49
import pandas as pd
import numpy as np
import string
df = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Victor','Nick']})

df = df.set_index(['ID'])
print(df)
df.to_excel('./output.xlsx')
print('完成！')