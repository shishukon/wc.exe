import os
import re
print('输入进行操作的路径')
path = input()


def file_name(path):
    l1 = []
    l2 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                l1.append(file)
                l2.append(root)
    return l1, l2


def find_target(target):
    count = -1
    filename, root = file_name(path)
    for i in filename:
        count = count + 1
        if target == i:
            return os.path.join(root[count], filename[count])
            # 返回文件绝对路径
            # print(os.path.join(root[count], filename[count]))
            # break


def c(file_path):
    file = open(file_path, 'r')
    print(len(file.read()))


def w(file_path):
    f = open(file_path, "r")
    print(len(re.split(r'[^a-zA-Z]+', f.read())))


def l(file_path):
    file = open(file_path, 'r')
    print(len(file.readlines()))


while 1:
    print('输入命令：')
    str = input()
    target = str[10:]
    order = str[0:9]
    file_path = find_target(target)
    if order == 'wc.exe -c':
        c(file_path)
        break
    elif order == 'wc.exe -w':
        w(file_path)
        break
    elif order == 'wc.exe -l':
        l(file_path)
        break
    else:
        print('非法输入')
