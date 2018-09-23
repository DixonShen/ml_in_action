# coding: utf-8


# @Time    : 2018/7/27 下午5:16
# @Author  : yongxin.shen@ele.me
# @File    : test03.py

import time
import re


p1 = '([\u4E00-\u9FA5\uF900-\uFA2D\w]+)[\(|（|《]*'
p2 = '\d*[-|弄]*\d+[栋|号楼|幢|号]+'
s1 = '红山花园555弄21-29号'
m1 = re.search(p2, s1)
print(m1)
print(m1.group(0))
