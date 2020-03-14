import os
import re


# 获取目录下所有后缀为txt的文件和它的路径(默认就是-s)
def file_name(path, extension):
    l1 = []
    l2 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == extension:
                l1.append(file)
                l2.append(root)
    return l1, l2


# 找到用户所选择的文件并返回它的路径
def find_target(path, target, extension, model=''):
    count = -1
    filename, root = file_name(path, extension)
    for i in filename:
        count = count + 1
        if target == i:
            return os.path.join(root[count], filename[count])
            # 返回文件绝对路径
            # print(os.path.join(root[count], filename[count]))
            # break


def c(path, target, file_extension, model):
    # s模式
    if model == '-s':
        filename, root = file_name(path, file_extension)
        for i in range(len(filename)):
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, 'r')
            list2 = file.read()
            print(filename[i], ':Char number->', len(list2.replace('\n', '')))
    # 普通模式
    else:
        file_path = find_target(path, target, file_extension)
        file = open(file_path, 'r')
        list1 = file.read()
        print('Char number->', len(list1.replace('\n', '')))


def w(path, target, file_extension, model):
    # s模式
    if model == '-s':
        filename, root = file_name(path, file_extension)
        for i in range(len(filename)):
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, 'r')
            print(filename[i], ':word number->', len(re.split(r'[^a-zA-Z]+', file.read())))
    # 普通模式
    else:
        file_path = find_target(path, target, file_extension)
        file = open(file_path, 'r')
        print('word number->', len(re.split(r'[^a-zA-Z]+', file.read())))


def l(path, target, file_extension, model):
    # s模式
    if model=='-s':
        filename, root = file_name(path, file_extension)
        for i in range(len(filename)):
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, 'r')
            print(filename[i], ':line number->', (len(file.readlines())))
    # 普通模式
    else:
        file_path = find_target(path, target, file_extension)
        file = open(file_path, 'r')
        print('line number->', len(file.readlines()))


def a(path, target, file_extension, model):
    code_line = 0
    blank_line = 0
    comment_line = 0
    file_path = find_target(path, target, file_extension)
    file = open(file_path, 'r')
    for line in file.readline():
        line = line.strip()
        if not len(line):
            blank_line += 1
        elif line.startswith('#'):
            comment_line += 1
        elif line.startswith('//'):
            comment_line += 1
        elif len(line)>1:
            code_line += 1
    print('blank_line->', blank_line, ', comment_line->', comment_line
          , ', code_line->', code_line)

