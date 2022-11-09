# 开发时间：9/8/2022 下午2:08
import time
for i in range(20):

    print("\r" + "正"*i, sep="", end="  ")
    time.sleep(0.2)
print("\r下载完成")