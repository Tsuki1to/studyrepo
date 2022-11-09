# 开发时间：23/9/2022 上午11:41
import os.path
filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择数字进入系统：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('确定退出系统吗y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice==1:
                insert()  #学生录入信息
            elif choice==2:
                search()  #学生查找信息
            elif choice==3:
                delete()   #学生删除信息
            elif choice==4:
                modify()   #学生修改信息
            elif choice==5:
                sort()    #学生信息排序
            elif choice==6:
                total()   #统计学生信息
            elif choice==7:
                 show()   #显示所有学生信息
def menu():
    print('===================学生管理系统==========================')
    print('---------------------功能菜单--------------------------')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出系统')
    print('--------------------------------------------------------')
def insert():
    student_list=[]
    while True:
        try:
            id = int(input('请输入id(如1000)：'))
        except:
            print('不是整数')
        name = input('请输入姓名：')
        if not name:
            break  # 如果为空，返回False，则break
        try:  # 成绩有可能录入错误，执行Try except处理异常错误
            eng_list = int(input('请输入英语成绩：'))
            python_list = int(input('请输入Python成绩：'))
            java_list = int(input('请输入java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue  # 返回至while True并重新输入
            # 将录入的学生信息保存在字典中
        student = {'id': id, 'name': name, '英语成绩': eng_list, 'Python成绩': python_list, 'java成绩': java_list}
            # 再将一个录入的学生信息加入到列表中
        student_list.append(student)  # 添加后并结束一轮录入
        answer = input('请问是否继续录入学生信息？y/n\n')
        if answer == 'y' or answer == "Y":
            continue
        else:
            break
            # 结束录入后要调用save（）函数进行保存学生信息
    save(student_list)
    print('学生信息了录入完毕！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='UTF-8')  #使用编码保存防止中文乱码
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]   #声明一个空列表
    while True:
        id=''
        name=''
        if os.path.exists(filename):   #判断文件是否存在
            mode=input('按照ID查找请输入1，按照名字查找请输入2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=input('请输入学生的姓名：')
            else:
                print('输入错误，请重新输入！')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()   #获取全部的内容并存入列表中
                for item in student:     #遍历列表存入字典中
                    d=dict(eval(item))
                    if id != '':   #因为有两种查询方式，所以判断两次
                        if d['id']==id:
                            student_query.append(d)   #如果查询到ID在字典中，则将内容添加进新的列表
                    elif name != '':
                        if d['name']==name:
                            student_query.append(d)   #如果查询到name在字典中，则将内容添加进新的列表
            #显示查询的结果
            show_student(student_query)  #展示新的列表需要格式化输出
            student_query.clear()  #清空
            answer=input('是否要继续查询y/n\n')
            if answer =='y':
                continue
            else:
                break
        else:
            print('学生信息暂未存储')
            return
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示')
        return
    #定义标题的显示格式
    format_titl='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_titl.format('ID','姓名','英语成绩','Python成绩','java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('英语成绩'),
                                 item.get('Python成绩'),
                                 item.get('java成绩'),
                                 int(item.get('英语成绩'))+int(item.get('Python成绩'))+int(item.get('java成绩'))))
def delete():
    show()
    while True:
        student_id=int(input('请输入要删除的学生的ID:'))
        if student_id!='':#输入的id不为空
            if os.path.exists(filename):#判断文件是否存在
                with open(filename,'r',encoding='utf-8') as file:#打开文件
                    student_old=file.readlines()#读取所有数据，放到列表当中
            else:
                student_old=[]
            flag=False   #标记是否删除
            if student_old:#如果列表不空，用只写的方式打开，将原有类容进行覆盖
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:#遍历列表，读出的是一个字符串
                        d=dict(eval(item))#将字符串转成字典
                        if d['id']!=student_id:#如果不相等就把其写入
                            wfile.write(str(d)+'\n')
                        else:#相等就删除
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息以被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show() #删除之后要重新显示所有学生信息
            answer=input('是否继续删除?y/n')
            if answer=='y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(filename):  # 判断这个文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()  # 以只读的形式赋给列表
    else:
        return
    student_id = input('请输入要修改的学生id:')
    with open(filename, 'w', encoding='utf_8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['englist'] = input('请输入英语成绩:')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入java成绩：')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否修改其他学生信息？y/n\n')
        if answer == 'y':
            modify()
def sort():
    show()
    if os.path.exists(filename):   #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:     #使用只读模式打开
            stu=rfile.readlines()    #按照行数读取数据
            stuent_new=[]     #建立一个空白列表
        for item in stu:    #遍历stu数据
            d=dict(eval(item))    #转换stu数据为字典
            stuent_new.append(d)   #转换后的字典添加进新的空列表中
    else:
        print('没有学生信息')
        return
    asc_or_desc=input('请选择：（0.升序，1.降序）')
    if asc_or_desc=="0":
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('输入错误，请重新输入：')
        sort()       #重新调用sort（）方法
    mode=input('请选择排序方式（1.用英语成绩排序 2.用Python成绩排序 3.用java成绩排序 0.用总成绩排序）')
    if mode=='1':
        stuent_new.sort(key=lambda x:int(x ['英语成绩']),reverse=asc_or_desc_bool)
    elif mode=='2':
        stuent_new.sort(key=lambda x:int(x ['Python成绩']),reverse=asc_or_desc_bool)
    elif mode=='3':
        stuent_new.sort(key=lambda x: int(x['java成绩']),reverse=asc_or_desc_bool)
    elif mode=='0':
        stuent_new.sort(key=lambda x:int(x ['java成绩'])+int(x ['Python成绩'])+int(x ['英语成绩']),reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入')
        sort()
    show_student(stuent_new)
def total():   #判断列表的长度
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('未录入学生信息')
    else:
        print('暂未保存数据')
def show():
    student_lst=[]   #建立空列表
    if os.path.exists(filename):   #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:    #按照只读的方式打开文件
            students=rfile.readlines()    #按行读取文件
            for item in students:      #遍历文件
                student_lst.append(eval(item))    #将遍历出的目标转换成字典保存在列表中
            if student_lst:           #判断列表是否为空
                show_student(student_lst)     #调用show_student函数
    else:
        print('暂时没有学生信息')
if __name__ == '__main__':
    main()



