# 开发时间：26/8/2022 下午1:45
# in  not in 返回 True 或者False
'''key的判断'''
scores={'张三':100,'李四':54,'王五':44}
print('张三' in scores)
print("张三" not in scores)


'''删除 del()'''
del scores['张三'] #删除指定的key-value对
# scores.clear()  清空字典元素
print(scores)

'''字典元素的新增操作'''

scores['陈留']=98
print(scores)  #字典新增键值对
scores['陈留']=100
print(scores)  #字典修改指定键的值
