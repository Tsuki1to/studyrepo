# 开发时间：25/8/2022 下午8:31
'''
向列表的末尾添加一个元素lst.append()
向列表的末尾一次性添加多个元素lst.extend()
在列表的任意指定位置x添加一个元素y-----insert(x,y)

'''
lst=[10,20,30]
print('添加元素前',lst,id(lst))
lst.append(100)
print('添加元素后',lst,id(lst))




lst2=['hello','world']
# lst.append(lst2)  #将lst2作为一个元素添加进了列表的末尾
# print(lst)

lst.extend(lst2)
print(lst)



lst.insert(1,22)
print(lst)

#切片：可以在列表任意位置添加N个元素
lst3=['hello',True,False]
lst[1:]=lst3
print(lst)
lst[1:4:]=lst3
print(lst)
