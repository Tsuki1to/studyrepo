# 开发时间：25/8/2022 下午6:18
#列表切片：用于获取多个元素。语法格式：列表名称[start:stop:step]
lst=[10,20,30,40,50,60,70,80,90]
#start=1,stop=6,step=1
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切片出的片段：',id(lst2))
print(lst[1:6]) #默认步长为1
print(lst[1:6:])  #默认步长为1
print(lst[1:6:2]) #步长为2
print(lst[:6:2])  #start默认为0
print(lst[1::2])  #stop默认为末尾
print('-------step为负数的情况下------------')
print('原列表',lst[::1])
print('step为负数情况下切片',lst[::-1])
print(lst[7:0:-2])
print(lst[6::-1])