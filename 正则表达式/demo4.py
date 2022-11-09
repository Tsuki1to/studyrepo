# 开发时间：23/9/2022 上午10:43


#re.search     只返回一个结果
#re.match      只返回一个结果，从头开始匹配


# tex='aBc,Abc,ABC'
# import re
# q=re.search(r'^abc',tex,flags=re.I)  =  q=re.match(r'abc',tex,flags=re.I)


text='0371-65335967-2102,321-65585171,1010101282658'
import re
m=re.search(r'(\d{4})-(\d{8})',text)   #将正则表达式中的条件进行分组
print(m.group())   #在输出结果中添加Group语句，就可以返回指定的组，不写就是返回所有组
                   #使用groups语句就是返回一个所有组 一起组成的元组



text='aBc,Abc,aBC,AbC'
import re
s=re.finditer(r'abc',text,flags=re.I )  #re.finditer返回一个match的迭代器，flages的I语句为忽略结果的大小写
for i in s:
    print(i)



text='abC,110,AbC,aBc'
import re
m=re.sub(r'abc','***',text,flags=re.I)  #sub语句输出的是替换后的原文
print(m)

text='abC,110,AbC,aBc'
import re
m=re.subn(r'abc','***',text,flags=re.I)  #subn语句输出的是替换后的原文及替换的次数
print(m)


#分割
result=re.split(r'\s*[,:/]\s*','foo,bar  :  baz / qux')   #\s*[,:/]\s*表示为寻找分割的位置，前后各有0或者多个空格中间是特殊符号
print(result)    #结果返回列表