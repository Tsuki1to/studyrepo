# 开发时间：2/11/2022 下午4:46
import pandas as pd
from datetime import date,timedelta
# a1 = pd.Series([100,200,300],index = ['x','y','z'])
# print(a1)

'''excel中的填充操作'''
# s1 = pd.Series([1,2,3],index=[1,2,3],name = 'A')
# s2 = pd.Series([10,20,30],index=[1,2,3],name = 'B')
# s3 = pd.Series([100,200,300],index=[2,3,4],name = 'C')
# a1 = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
# print(a1)


'''向空的工作列表中填充信息'''
file_path = './books.xlsx'

# print(df)  #因为前面有空行和空列所以无法直接读取数据
df= pd.read_excel(file_path,skiprows=3,index_col=None
                  ,dtype= {'ID':str,'InStore':str,'Date':str})   #skiprows可以选择跳过前面的行数，usecoks可以选择使用的列的范围
start = date(2018,1,1)
for i in df.index:
    # df['ID'].at[i]= i+1 #.at函数使用方法结果是相同的
    df.at[i,'ID'] = i + 1
    df['InStore'].at[i] = 'Yes'if i%2==0 else 'No' #Yes和No隔行填充
    df['Date'].at[i] = start +timedelta(days=i)  #使用日期按照天数顺序填充
    # df['Date'].at[i] = date(start.year+i,start.month,start.day)  #使用日期按照年代顺序填充
    # df['Date'].at[i] = start +timedelta(days=i)  #使用日期按照顺序填充

df.to_excel('./books.xlsx')
print(df)
'这个是最新的版本' \
'2'