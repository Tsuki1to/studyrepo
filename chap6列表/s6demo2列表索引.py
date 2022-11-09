# 开发时间：25/8/2022 下午5:51
print('---------获取列表中的索引（页码-----------')
#使用index函数对list进行查找
lst=['hello','world',98,'hello']
print(lst.index('hello'))  #如果列表中有相同的元素只返回列表中相同元素的第一个元素的索引
# print(lst.index('python')) ValueError: 'python' is not in list
# print(lst.index('hello',1,3))  ValueError: 'hello' is not in list
#按照列表中顺序查找，后面带数字
print(lst.index('hello',1,4)) #3


print('------------获取列表中的单个元素------------------')
'''
1.正向索引从0到N-1
2.逆向索引从-N到-1
3.指定索引不存，抛出indexError
'''
lst=['hello','world0',98,'world',51,32]
print(lst[2])  #获取索引为2的元素
print(lst[-3])  #获取索引为-3的元素
# print(lst[10]) #IndexError: list index out of range