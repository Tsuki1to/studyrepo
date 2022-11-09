# 开发时间：11/10/2022 上午11:38
import numpy as np
t1 = np.arange(15).reshape(3,5).astype('float')
t1[1,2:] = np.nan
print(t1)
print('\n')
print('\n')
print('\n')
#遍历t1的所有列
def fill_ndarray(t1):
    for i in range(t1.shape[1]):   #shape[1]表示为数组中的所有列
        temp_col = t1[...,i]   #提取当前的一列   (数组的切片操作)
        nan_num = np.count_nonzero(temp_col!=temp_col)   #（布尔值索引
        if nan_num != 0:   #如果不为0，则这一列中有nan
            temp_not_nan_col = temp_col[temp_col ==temp_col]  #就把这一列中不为nan的数组赋值给一个新的数组，因为nan和nan不相等所以没法提取出来
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()  #选中带有nan那一列中的nan，赋值为nan列中不为nan数组的平均值

    return t1

if __name__ == '__main__':
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)