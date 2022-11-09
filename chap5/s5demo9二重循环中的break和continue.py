# 开发时间：25/8/2022 下午5:02
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()