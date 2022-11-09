# 开发时间26/9/2022 下午2:57
'''
宠物管理系统主界面
'''
from pet_tools import show_menu
from pet_tools import new_pet
from pet_tools import *    #import * 表示为导入包中所有的模块
def main():
    while True:
        show_menu()
        action = input('请输入你要想要使用的功能：')
        if action in ["1","2","3"]:
           if action == "1":
                new_pet()    #Ctrl键+左键点击函数名字跳转到函数定义处
           elif action == "2":
                show_all()
           elif action == "3":
                search()
        elif action == '0':
            print('欢迎再次使用【宠物管理系统】')
            input('按下任意键关闭窗口')
            break
        else:
            print('输入错误！请重新输入！')

    # 不断执行上述循环
if __name__ == '__main__':
    main()    #通过在main函数后添加需要调试的函数进行调试