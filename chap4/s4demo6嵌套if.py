# 开发时间：19/8/2022 下午4:27
'''
会员 >=200 8折
    >=100 9折
    <100 不打折
非会员  >=200  9.5折
      <200  不打折
'''
answer=input('您是会员吗y/n:')
money=float(input('请输入您的购物金额：'))
#外层判断是否是会员
if answer=='y':
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)

else:
    if money>=200:
        print('打95折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)
