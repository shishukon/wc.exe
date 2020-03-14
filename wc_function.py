import os
import re


# 获取目录下所有后缀为txt的文件和它的路径
def file_name(path, extension):
    l1 = []
    l2 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # 指定后缀的文件并将路径与文件名存入列表中
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
        # 查找文件
        if target == i:
            return os.path.join(root[count], filename[count])
            # 返回文件绝对路径


def c(path, target, file_extension, model):
    # s模式
    if model == '-s':
        # 获取目录下文件名以及其路径
        filename, root = file_name(path, file_extension)
        # 对列表中的每一个文件进行操作
        for i in range(len(filename)):
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, encoding="UTF-8")
            list2 = file.read()
            print(filename[i], ':Char number->', len(list2.replace('\n', '')))
    # 普通模式
    else:
        # 获取目录下文件名以及其路径
        file_path = find_target(path, target, file_extension)
        file = open(file_path, encoding="UTF-8")
        list1 = file.read()
        print('Char number->', len(list1.replace('\n', '')))


def w(path, target, file_extension, model):
    # s模式
    if model == '-s':
        # 获取目录下文件名以及其路径
        filename, root = file_name(path, file_extension)
        # 对列表中的每一个文件进行操作
        for i in range(len(filename)):
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, encoding="UTF-8")
            print(filename[i], ':word number->', len(re.split(r'[^a-zA-Z]+', file.read())))
    # 普通模式
    else:
        # 获取目录下文件名以及其路径
        file_path = find_target(path, target, file_extension)
        file = open(file_path, encoding="UTF-8")
        print('word number->', (len(re.split(r'[^a-zA-Z]+', file.read()))-1))


def l(path, target, file_extension, model):
    # s模式
    if model == '-s':
        filename, root = file_name(path, file_extension)
        for i in range(len(filename)):
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, encoding="UTF-8")
            print(filename[i], ':line number->', (len(file.readlines())))
    # 普通模式
    else:
        file_path = find_target(path, target, file_extension)
        file = open(file_path, encoding="UTF-8")
        print('line number->', len(file.readlines()))


def a(path, target, file_extension, model):
    code_line = 0
    blank_line = 0
    comment_line = 0
    if model == '-s':
        filename, root = file_name(path, file_extension)
        for i in range(len(filename)):
            # 计数清零，进行下一轮统计
            code_line = 0
            blank_line = 0
            comment_line = 0
            file_path = os.path.join(root[i], filename[i])
            file = open(file_path, encoding="UTF-8")
            for line in file.readlines():
                line = line.strip()
                # 空行统计
                if not len(line):
                    blank_line += 1
                # 注释统计
                elif line.startswith('#'):
                    comment_line += 1
                elif line.startswith('//'):
                    comment_line += 1
                # 代码行统计
                elif len(line) > 1:
                    code_line += 1
            print(filename[i], 'blank_line->', blank_line, ', comment_line->', comment_line
                  , ', code_line->', code_line)
    else:
        file_path = find_target(path, target, file_extension)
        file = open(file_path, encoding="UTF-8")
        for line in file.readlines():
            # 去除空格
            line = line.strip()
            # 空行统计
            if not len(line):
                blank_line += 1
            # 注释统计
            elif line.startswith('#'):
                comment_line += 1
            elif line.startswith('//'):
                comment_line += 1
                # 代码行统计
            elif len(line) > 1:
                code_line += 1
        print('blank_line->', blank_line, ', comment_line->', comment_line
              , ', code_line->', code_line)

