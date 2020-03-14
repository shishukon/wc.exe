file = open('D:/123.txt', 'r')
code_line = 0
blank_line = 0
comment_line = 0
#line = file.read()
#print(line)
for line in file.read():
    line = line.strip()
    if not len(line):
        blank_line += 1
    elif line.startswith('#'):
        comment_line += 1
    elif line.startswith('//'):
        comment_line += 1
    elif len(line) > 1:
        code_line += 1
print('blank_line->', blank_line, ', comment_line->', comment_line, ', code_line->', code_line)