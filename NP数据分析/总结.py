# 开发时间11/10/2022 下午2:51
import numpy as np

'''切片与索引操作'''
t = np.arange(15).reshape(3,5)
#选择行切片
t1= t[2]
print(t1)
t1=t[3:,:]

# #选择列切片
t1=t[:,4:]

# #选择行列：连续的行列
t1=t[2:,:3]
#
# #选择行列，不连续的行列
# t1=t[[1,3][2,4]]   #选择位置为第二行第三个，第四行第五个。
#
#
# #索引
t1=t[2,3]
#
'''赋值'''
t[2,2]=3    #或者赋值nan（np.nan）)

'''布尔索引赋值（例如：把数组中大于10的数赋值10'''
t[t>10] = 10
print(t)

'''三元运算符'''
t3=np.where(t>9,20,0)  #把数组中大于9的元素替换为20，其余的替换为0
print(t3)

'''裁剪'''
t4 = np.clip(t,10,20)
print('\n')
print(t4)
#把数组中小于10的替换为10，大于20的替换为20

'''转置'''
t5 = t.T
t6 = t.transpose()
t7 = t.swapaxes(1,0)
print('\n')

'''文件的读取'''
#np.loadtxt(file_path,delimiter=,dtype=)

'''nan和inf'''
#nan不是数字
np.nan!=np.nan #效果相同 np.isnan()
np.count_nonzero(np.nan!=np.nan)  #可以筛选出数组中不为nan数值

#inf表示无穷

'''常用统计函数'''
t.sum(axis=0)
t.max(axis=0)
t.mean(axis=0)
np.meadian(t,axis=0)
np.average(t,axis=0)
np.std(t,axis=0)   #标准差，表示离散程度
np.ptp(t)   #计算极差（最大值-最小值）
