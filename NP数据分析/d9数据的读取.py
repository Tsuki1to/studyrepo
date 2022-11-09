# 开发时间：10/10/2022 下午4:40
#conding = utf-8
import numpy as np
# a = np.loadtxt(frame,dtype=（数据类型）,delimiter=(分隔字符串),skiprows=（跳过前面x行），usecols=（读取指定列，索引，
# unpack=False(True为数据转置，按照对角线进行翻转，默认为False))
data = np.genfromtxt('G:\OneDrive\PYcharmProject\DATA1.csv',delimiter=',',dtype='i',skip_header=1)
print(data)

#使用均值替换数组中的无意义的数值
def fill_num(data):
    for i in range(data.shape[1]):
        temp_col = data[..., i]
        wuxiaozhi = temp_col[temp_col<0]
        if wuxiaozhi <0:
            temp_nan_col = temp_col[temp_col>0]
            temp_col[temp_col<0] = temp_nan_col.mean()

    return data

if __name__ == '__main__':
    print(data)
    print('\n')
    data = fill_num(data)
    print(data)
