# 开发时间：26/8/2022 下午2:18
items=['Fruits','Books','Others']
prices=[96,78,85]
d={i.upper():p for i,p in zip(items,prices)}  #upper()大写函数
print(d)
print(type(d))
