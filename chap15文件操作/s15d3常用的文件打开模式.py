# 开发时间：20/9/2022 下午7:58
# 'w'只写模式，没有文件就重新创建一个文件，如果有就覆盖原来的文件内容
# file=open('b.txt','w')
# file.write('hello world')
# file.close()

#'a'追加模式，在文件的末尾追加内容，执行一次追加一次
# file=open('b.txt','a')
# file.write('/nhello world')
# file.close()

#‘b’为二进制模式，不能单独使用，rb为在二进制下读取，wb为在二进制下写入
src_file=open('1663676706566.png','rb')
target_file=open('copy.png','wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()