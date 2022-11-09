# 开发时间：14/9/2022 上午11:27
def phe(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return phe(n-2)+phe(n-1)
#斐波那契数列
print(phe(6))



for i in range(1,7):
    print(phe(i))

'''
总结
递归函数就是函数调用韩函数本身
递归函数的组成：if(终止条件)   +   else(调用条件)
'''