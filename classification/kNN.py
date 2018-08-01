# coding: utf-8


# @Time    : 2018/7/28 下午12:11
# @Author  : yongxin.shen@ele.me
# @File    : kNN.py

import numpy as np
from numpy import *
import operator
import os
from os import path
import matplotlib
import matplotlib.pyplot as plt


def create_dataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# knn分类器
def knn_classifier0(data, data_set, labels, k):
    data_size = data_set.shape[0]
    diff_mat = tile(data, (data_size, 1)) - data_set
    distances = ((diff_mat ** 2).sum(axis=1)) ** 0.5
    distances = distances.argsort()
    class_count = {}
    for i in range(k):
        label_index = labels[distances[i]]
        class_count[label_index] = class_count.get(label_index, 0) + 1
    sorted_class_count = sorted(class_count.items(),
                                key=operator.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]


# knn数据集转化为numpy数组
def file2matrix(file_path):
    fhandler = open(file_path, 'r')
    lines = fhandler.readlines()
    data_count = len(lines)
    data_matrix = zeros((data_count, 3))
    label_vec = []
    index = 0

    for line in lines:
        line = line.strip()
        infos = line.split("\t")
        data_matrix[index, :] = infos[0:3]
        label_vec.append(infos[3])
        index += 1

    return data_matrix, label_vec


# 将特征值归一化
def auto_norm(data_set):
    min_value = data_set.min(0)
    max_value = data_set.max(0)
    ranges = max_value - min_value
    norm_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    norm_data_set = data_set - tile(min_value, (m, 1))
    norm_data_set = norm_data_set/tile(ranges, (m, 1))
    return norm_data_set


def dating_classification_test():
    test_ratio = 0.1
    current_path = path.dirname(path.abspath(__file__))
    dating_file = path.join(current_path, "data/datingTestSet.txt")
    dating_data_matrix, dating_labels = file2matrix(dating_file)
    dating_data_matrix = auto_norm(dating_data_matrix)
    m = dating_data_matrix.shape[0]
    test_number = int(m*test_ratio)
    error_count = 0
    for i in range(test_number):
        res = knn_classifier0(dating_data_matrix[i, :], dating_data_matrix[test_number:m, :],
                              dating_labels[test_number:m], 3)
        print("the classifier came back with: %s, the real answer is: %s"
              % (res, dating_labels[i]))
        if res != dating_labels[i]:
            error_count += 1
    print(error_count)
    print(test_number)
    print("the total error rate is: %f" % (error_count/test_number))


def img2vector(file_path):
    fhandler = open(file_path, 'r')
    digit_vec = zeros((1, 1024))
    for i in range(32):
        line = fhandler.readline()
        for j in range(32):
            digit_vec[0, 32*i+j] = int(line[j])
    return digit_vec


def handwriting_digits_test():
    current_path = path.dirname(path.abspath(__file__))
    digits_dir = path.join(current_path, "data/digits/trainingDigits")
    file_list = os.listdir(digits_dir)
    labels = []
    m = len(file_list)
    training_matrix = zeros((m, 1024))

    for i in range(m):
        file_name = file_list[i]
        label = file_name.split("_")[0]
        labels.append(label)
        training_matrix[i, :] = img2vector("data/digits/trainingDigits/" + file_name)

    test_file_list = os.listdir(digits_dir)
    error_count = 0
    m_test = len(test_file_list)
    for i in range(m_test):
        test_file = test_file_list[i]
        label = test_file.split("_")[0]
        test_vec = img2vector("data/digits/trainingDigits/" + test_file)
        res = knn_classifier0(test_vec, training_matrix, labels, 1)
        print("the classifier came back with: %s, the real answer is: %s"
          % (res, label))
        if res != label:
            error_count += 1

    print("\nthe total number of errors is: %d" % error_count)
    print("\nthe total error rate is: %f" % (error_count/m_test))


# dating_classification_test()
handwriting_digits_test()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(dating_data_matrix[:, 1], dating_data_matrix[:, 2],
#            15.0*array(dating_labels), 15.0*array(dating_labels))
# plt.show()
