# 开发时间：25/8/2022 下午9:19
'''
列表的排序操作
1.调用sort()方法，默认从小到大排序（升序），也可以指定reverse=True进行降序排列(------在原列表中进行排序
2.调用内置函数sorted()进行升序排列，可以指定reverse=True，进行降序排列，原列表不发生改变（-----产生一个新的列表
'''
lst=[10,50,80,55,1110,66]
print('排序前的列表',lst)
lst.sort()
print('排序后的列表',lst)

#降序
lst.sort(reverse=True)
print(lst)


print('-------将产生一个新的列表对象--------')
lst=[55,232,66,77,99,88]
print('原列表',lst)
new_list=sorted(lst)
print(lst)
print(new_list)
#降序
desc_list=sorted(lst,reverse=True)
print(desc_list)
