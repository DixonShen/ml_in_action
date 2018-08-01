# coding: utf-8


# @Time    : 2018/7/26 下午4:43
# @Author  : yongxin.shen@ele.me
# @File    : test02.py


import re


file_path = '/Users/dixonshen/Downloads/Dtab12.txt'

lines = open(file_path, 'r').readlines()
blocks = []
code = ''
label = ''
note = ''
includes = ''
excludes = ''

block_count = 0

# flag indicates the type of specific line
# 0: code_label line
# 1: note line
# 2: includes line
# 3: excludes line
last_flag = 0
current_flag = 0

new_block_flag = False

for i in range(len(lines)):
    line = lines[i].strip()
    if re.compile('^[0-9]{3,}\.?\d{0,}\t|^[A-Z][0-9]{1,}\.?\d*\t').match(line):
        block_count += 1
        infos = line.split('\t', 2)
        print(infos)
        code = infos[0]
        label = infos[1]
        print(code + ',' + label)
print(block_count)


