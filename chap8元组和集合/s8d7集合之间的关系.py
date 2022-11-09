# 开发时间：26/8/2022 下午4:49
s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)  #集合是无序的，元素相同就相等
print(s!=s2)

'''子集 、超集'''
s1={10,20,30,40,50,60,70}
s2={10,20,30}
s3={10,20,30,80}
print(s3.issubset(s1))#False
print(s2.issubset(s1))#True
'''超集'''
print(s1.issuperset(s3)) #False
print(s1.issuperset(s2))  #True

'''两个集合是否含有交集'''
print(s2.isdisjoint(s1))  #False  有交集为False
s4={100000,50000,600000}
print(s3.isdisjoint(s4))  #True   没有交集为True
