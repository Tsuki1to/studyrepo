# 开发时间：25/8/2022 下午8:47
'''
列表的删除操作
remove(元素).一次删除一个元素------重复元素只删除第一个-------元素不存在的话会报错
pop(索引).删除一个指定索引位置上的元素-------指定索引不存在会报错-----不指定索引会固定删除最后一个元素
切片lst[x:x:x]一次删除多个元素
clear()清空列表
del()删除列表
'''

lst=[10,20,30,40,50,60,70,80,30]
lst.remove(30)
print(lst)
# print(lst.remove(100))  ValueError: list.remove(x): x not in list
lst.pop(1)
print(lst)
lst.pop()
print(lst)
# print(lst.pop(7))  IndexError: pop index out of range

print('------切片操作，删除多个元素将产生一个新的元素------')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)
'''不产生新的对象，只删除原列表中的内容'''
lst[1:3]=[]
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''删除整个列表'''
del lst
# print(lst)  #NameError: name 'lst' is not defined. Did you mean: 'list'?