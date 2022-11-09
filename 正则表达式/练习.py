# 开发时间：23/9/2022 上午11:17
#Email地址
 \w+([-+.]\w+)*@\w+([-.]\w+)*.\w+([-.]\w+)*

#URL地址
[a-zA-Z]+://[^s]*

#合法账号（字母开头，5-16个字节，允许字母数字下划线
^[a-zA-z][a-zA-Z0-9_]{4,15}$
#国内电话号码（4-8,3-8,3-8-3）
\d{3,4}-\d{7,8}|\d{3,4}-\d{7,8}-\d{3,4}
#匹配qq号
[1,9][0,9]{4,}
#中国邮政编码（6位数字
\d{6}
#匹配身份证（15位或者18位
\d{15}|\d{18}
#匹配ip地址
\d+.\d+.\d+.\d+
#形容carcar，barbar等重复三个字符的单词
(\w{3})(\1)

#以密码:开头的数字
(?<=密码.)\d+