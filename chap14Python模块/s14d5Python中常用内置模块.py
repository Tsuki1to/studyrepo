# 开发时间：20/9/2022 下午3:41
import sys
import time

print(sys.getsizeof(24))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

import urllib.request
# print(urllib.request.urlopen('https://www.bilibili.com/video/BV1wD4y1o7AS?p=126&spm_id_from=pageDriver&vd_source=57fdd316522ba10240be584bf6da7c98').read())

'''
os 提供了访问操作系统服务功能的标准库
calender 提供与日期相关的各种函数的标准库
json   用于使用JSON序列化的反序列化对象
re   用于在字符串中执行正则表达式匹配和替换
decimal  用于进行精确控制运算精度、有效位数和四舍五入操作的十进制运算
logging 提供了领过的记录事件、错误、警告和调试信息等日志信息的功能
'''