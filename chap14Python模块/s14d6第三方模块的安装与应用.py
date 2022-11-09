# 开发时间：20/9/2022 下午4:11
# 在线安装第三方模块
# 在cmd面板中键入 pip Install+模块名

import schedule
import time
def job():
    print('哈哈---')

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)