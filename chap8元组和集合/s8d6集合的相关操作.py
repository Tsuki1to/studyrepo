# 开发时间：26/8/2022 下午4:30
s={2,3,4,5,5,7,7}
#集合元素的判断
#in not in

#集合元素的新增操作
'''添加一个元素'''
s.add(80)  #添加一个元素
print(s)
'''添加多个元素'''
s.update({200,300,400})  #添加集合
print(s)
s.update([100,90,8])    #添加列表
print(s)
s.update((78,68,54))  #添加元组
print(s)

#集合删除操作

s.remove(100)
print(s)
# # s.remove(6542) #KeyError: 6542
# print(s)
s.discard(90) #有这个元素就删除
s.discard(98754)  #没有这个元素也不报错
print(s)

# pop()
s.pop() #删除集合中任意元素
print(s)
# s.pop(3)  pop()无法指定参数，报错
s.clear()
print(s)
