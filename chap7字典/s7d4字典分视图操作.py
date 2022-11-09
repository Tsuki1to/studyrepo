# 开发时间：26/8/2022 下午1:51
'''
1.key()====>获取字典中的所有key
2.values()======>获取字典中的所有values
3.items()======>获取字典中的所有key,values对
'''
scores={'张三':[100,101],'李四':54,'王五':44}
# k=scores.keys()
# print(k)
# print(type(k))
# print(list(k))    #将所有的key组成的视图转换成列表
#
# v=scores.values()
# print(v)
# print(type(v))
# print(list(v))
#
# i=scores.items()
# print(i)
# print(list(i))  #元组(), 转换之后的元素是由元组组成的

'''
字典元素的遍历
for item in scores()
'''
for i in scores:
    print(i,scores[i],scores.get(i))



