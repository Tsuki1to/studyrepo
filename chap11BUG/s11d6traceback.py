# 开发时间：14/9/2022 下午10:04



import traceback
try:
    print('---------------------')
    print(1/0)
except:
    traceback.print_exc()