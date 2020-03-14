import os
import re
import wc_function as wf
print('输入进行操作的路径')
path = input()

while 1:
    print('输入命令：')
    str1 = input()
    point = str1.find('.')
    # 文件拓展名
    file_extension = str1[point:]
    if str1[0:2] == '-s':
        # 文件名
        target = str1[6:]
        # 指令
        order = str1[3:5]
        model = '-s'


    else:
        # 文件名
        target = str1[3:]
        # 指令
        order = str1[0:2]
        model = 'normal'

    if order == '-c':
        wf.c(path, target, file_extension, model)
        break
    elif order == '-w':
        wf.w(path, target, file_extension, model)
        break
    elif order == '-l':
        wf.l(path, target, file_extension, model)
        break
    elif order == '-a':
        wf.a(path, target, file_extension, model)
    elif order == '-x':
        os.system("GUI.py")
    else:
        print('非法输入')
