# 开发时间：9/9/2022 下午4:01
s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))
#解码
#byte代表的是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK') #编码
print(byte.decode(encoding='GBK'))  #解码

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))