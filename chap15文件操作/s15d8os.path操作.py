# 开发时间：21/9/2022 下午9:55


import os.path
print(os.path.abspath('s15d1文件操作中的编码格式.py'))    #获取文件的绝对路径
print(os.path.exists('s15d1文件操作中的编码格式.py'),os.path.exists('111.py'))   #判断文件是否在包中存在
print(os.path.join('G:\\onedrive\\PYcharmProject\\chap15文件操作\\s15d1文件操作中的编码格式.py'))   #将目录与目录或者文件名拼接起来
print(os.path.split('G:\\onedrive\\PYcharmProject\\chap15文件操作\\s15d1文件操作中的编码格式.py'))   #分离文件名和扩展名
print(os.path.splitext('demo13.py'))    #分离文件名与后缀名
print(os.path.basename('G:\\onedrive\\PYcharmProject\\chap15文件操作\\s15d1文件操作中的编码格式.py'))   #将路径中的文件名提取出来
print(os.path.dirname('G:\\onedrive\\PYcharmProject\\chap15文件操作\\s15d1文件操作中的编码格式.py'))   #将路径中的目录名提取出来
print(os.path.isdir('G:\\onedrive\\PYcharmProject\\chap15文件操作\\s15d1文件操作中的编码格式.py'))   #判断是否为路径
