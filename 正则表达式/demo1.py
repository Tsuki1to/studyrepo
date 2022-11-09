# 开发时间：22/9/2022 下午12:09
#1.固定字符
# import re
# text='shengao:180,tizhong:150,xuehao:8888,mima:5260，8888'
# print(re.findall(r'8888',text))   #如果找到了该字符串，就返回包含目标的列表


#2.某一字符
# import re
# text='shengao:180,tizhong:150,xuehao:8888,mima:5260，8888'
# print(re.findall(r'\d',text))   #\d表示每个单个数字，\D表示为所有非数字对象，\w表示目标中除了标点符号外的所有单个字符
# #[]中添加关键字
# print(re.findall(r'[a-z]',text))  #找到目标中所有的小写字母


#3.重复的某一个字符
# import re
# text='shengao:180,tizhong:150,xuehao:8888,mima:5260，8888'
# print(re.findall(r'8+',text))   #'+'表示多次，找出目标中带有8的字符
# print(re.findall(r'\d?',text))   #'?'表示出现次数为0或者1，\d?就表示寻找的目标表位单个数字或者不是数字的字符
# print(re.findall(r'\d*',text))   #'?'表示出现次数为0或多个，\d*就表示寻找的目标表位多个数字或者不是数字的字符
# print(re.findall(r'\d{3}',text))  #\d{3}括号中数字表示为，寻找目标为3个字符的数字
# print(re.findall(r'\d{1,4}',text))  #\d{1,4}括号中数字表示为，寻找目标为1至4个字符的数字
# print(re.findall(r'\d{1,}',text))  #\d{1,}括号中数字表示为，寻找目标为1个以上字符的数字
# print(re.findall(r'\d{,8}',text))  #\d{,8}括号中数字表示为，寻找目标为8以下个字符的数字（包括0，所以包含没有数字的字符


#4.组合
#要求：找出座机的号码，（号码格式为4位数字-8位数字）
# text='我的手机号为：125837180030，我的座机号码为：0371-65335967-1524，我的学号为：1917301052。'
# import re
# print(re.findall(r'\d{3,4}-\d{7,8}',text))
# print(re.findall(r'\d{3,4}-\d{7,8}-\d{4}',text))


#5多种情况
#要求：找出手机号码或者座机号码
# text = '我的手机号为：15837180030，我的座机号码为：0371-65335967，我的学号为：1917301052。'
# import re
# print(re.findall(r'\d{3,4}-\d{7,8}|1\d{10}',text))  #使用|表示或者的意思，后面手机号为1加10个任意数字

#现在已经知道了是字符，重复多少次，组合，或
#6.限定位置
# text = '188123456789，我的手机号为：15837180030，我的座机号码为：0371-65335967，我的学号为：1917301052'
# import re
# print(re.findall(r'^1\d{10}|^\d{4}-\d{8}',text))   #'^'表示为以xxx为开头，
# print(re.findall(r'1\d{9}$|^\d{4}-\d{8}',text))   #在条件后加$表示为：必须以xxx为结尾


#7.添加内部的约束
text='barbar,carcar,herhel'
import re
print(re.findall(r'(\w{3})(\1)',text))  #(\1)表示为（\1）中内容要和前一个括号中的内容相同