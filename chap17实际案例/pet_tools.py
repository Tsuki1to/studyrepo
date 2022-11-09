# 开发时间26/9/2022 下午3:56

Header = ['名字','年龄','性别','体重']
# pet_info = [{'nickname': '牛牛',
# 'age': '13',
# 'gender': '雌性',
# 'weight': '20'},{'nickname': '落落',
# 'age': '12',
# 'gender': '雌性',
# 'weight': '32'}]
pet_info=[]
#测试数据
def show_menu():
    '''
    显示系统菜单
    :return:  print
    '''
    print('')
    print('宠物管理系统'.center(32,'*'))
    print('1.新增宠物信息')
    print('2.显示全部宠物信息')
    print('3.搜索宠物信息')
    print('0.退出系统')
    print('*'*36)
def new_pet():

    print('新增宠物信息'.center(32,'='))
    nickname = input('请输入宠物姓名：')
    age = input('请输入宠物年龄：')
    gender = input('请输入宠物性别（雄性/雌性）：')
    weight = input('请输入宠物体重（kg）：')
    print(f'添加{nickname}成功！')
    pet = {'nickname':nickname,
           'age':age,
           'gender':gender,
           'weight':weight}
    # {'nickname': '牛牛', 'age': '13', 'gender': '雌性', 'weight': '20'}
    pet_info.append(pet)
    print(pet_info)
def show_all():
    print('显示全部宠物信息'.center(32,'='))
    if len(pet_info) == 0:
        print('宠物信息为空，请重新输入！')
        return

        # 打印表头print('名字\t\t年龄\t\t性别\t\t体重')
    for title in Header:
        print(title,end='\t\t')
    print()
    print('-'*28)
    #逐行打印列表中的每个宠物的信息
    for pet in pet_info:   #遍历列表中的键值对，输出为字典
        # print(f"{pet['nickname']}\t\t{pet['age']}\t\t"
        #       f"{pet['gender']}\t\t{pet['weight']}")
        for value in pet.values():     #遍历字典中的值
            print(f'{value}',end='\t\t')
        print()#格式化打印出字典中所有值
def search():
    print('搜索宠物信息'.center(32,'='))
    #1.引导用户输入要搜索的信息
    find_name=input('请输入想要查询的宠物信息：')
    #2.在宠物信息列表中查找对应昵称的宠物信息
    for pet in pet_info:
        if pet['nickname']== find_name:
            #打印表头
            for title in Header:
                print(title,end='\t\t')
            print()
            print('-'*36)
            #逐行打印每个宠物信息
            for value in pet.values():
                print(f'{value}',end='\t\t')
            print()
            #处理查找到的宠物的信息
            deal_pet(pet)
            break
    else:
        print(f'对不起，没有找到{find_name}')

    #3.如果找到了就打印输出
    #4.如果没找到就打印输出提示信息
def deal_pet(find_pet):
    '''
    处理查找到的宠物信息
    :param find_pet: 查找到的宠物信息
    :return:
    '''
    action = input('请选择要执行的操作:【1】修改【2】删除【0】返回上级菜单')
    if action == '1':
       find_pet['nickname'] = input_pet_info(find_pet['nickname'],'请输入新的昵称：（回车就不进行修改）')
       find_pet['age'] = input_pet_info(find_pet['age'],'请输入年龄：（回车就不进行修改）')
       find_pet['gender'] = input_pet_info(find_pet['gender'],'请输入性别：（回车就不进行修改）')
       find_pet['weight'] = input_pet_info(find_pet['weight'],'请输入体重：（回车就不进行修改）')
       print('【宠物信息已经修改成功！】')


    elif action == '2':
        pet_info.remove(find_pet)
        print('【宠物信息已经成功删除！】')
def input_pet_info(pet_value,tip):
    '''
    检测用户输入内容是否为空
    为空时返回原来列表中的值
    不为空时返回用户输入的值
    :param pet_value: 用户输入的值
    :param tip: 键
    :return: 判断是否为空返回原值或者用户输入的值
    '''
    result=input(tip)
    if len(result) > 0:
        return result
    else:
        return pet_value


if __name__ == '__main__':
    # show_all()
    # new_pet()
    search()
