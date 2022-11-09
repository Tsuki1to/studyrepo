# 开发时间：26/8/2022 下午1:27
'''
字典中元素的获取方法
1.[]=====>scores['张三']
2.get()======>scores.get('张三')
'''
scores={'张三':100,'李四':54,'王五':44}
#1.
print(scores['张三'])
# print(scores['陈留']) #KeyError: '陈留'
#2.
print(scores.get('张三'))
print(scores.get('陈留')) #None
print(scores.get('骂起',99)) #99  是在查找'骂起'所对应对额Value不存在时所对一个的一个默认值
