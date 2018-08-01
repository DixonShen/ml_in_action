# coding: utf-8


# @Time    : 2018/7/28 上午11:52
# @Author  : yongxin.shen@ele.me
# @File    : numpy_test.py

from numpy import *

r = random.rand(4, 4)
r_mat = mat(r)
inv_mat = r_mat.I
print(r_mat * inv_mat)
