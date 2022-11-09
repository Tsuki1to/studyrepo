 # 开发时间：25/8/2022 下午1:24
'''
输出1到50之间5的倍数
5的倍数为与5取余数为0
不是5的倍数取余数不为0
'''
for i in range(1,51):
    if i%5==0:
        print(i)

print('-------使用continue语句进行实现-------')
for i in range(1,51):
    if i%5: #(i%5!=0)
        continue
    print(i)