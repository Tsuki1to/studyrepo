# 开发时间：14/9/2022 下午7:30
lst=[{'rating':[9.7],'title':'肖申克的救赎','actors':['蒂姆罗宾斯','摩根弗里曼']},
     {'rating':[9.6],'title':'霸王别姬','actors':['张国荣','张丰毅','葛优','巩俐']},
     {'rating':[9.5],'title':'阿甘正传','actors':['汤姆汉克斯','罗宾怀特']}]

#思路不清晰BUG
# name=input('请输入你要查询的演员：')
# for item in lst:
#     for movie in item:
#         actors=movie['actors']
#         if name in actors:
#             print(name+'出演了:'+movie)

#正确
name=input('请输入你要查询的演员：')
for i in lst:    #遍历列表=====》i得到的是一个又一个的字典
    if name in i['actors']:
        print(name+'出演了：'+i['title'])