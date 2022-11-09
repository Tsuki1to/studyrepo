# 开发时间：20/9/2022 下午9:36
#with语句可以自动管理上下文资源，不论什么原因跳出，with语句都能确保文件的正确关闭，以此来达到释放资源的目的‘
'''with open('1000.txt','r') as file:   #就相当于file=open()_
    #上下文管理器
    print(file.read())'''

with open('copy.png','rb') as file:
    with open('copy2.png','wb') as target_file:
        target_file.write(file.read())