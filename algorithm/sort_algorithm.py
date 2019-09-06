# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 21:15
# @Author  : TanXueFeng
# @Site    : 
# @File    : sort_algorithm.py
# @Software: PyCharm

# 排序算法：直接插入排序, 折半插入排序, 起泡排序, 直接选择排序, 希尔排序, 快速排序, 堆排序, 2路归并排序, 基数排序
import copy


def insert_sort(p_l):
    """
    直接插入排序
    :param p_l:list
    :return: list
    O(n^2)
    稳定排序
    """
    l: list = copy.copy(p_l)
    length = len(l)
    for i in range(1, length):
        if l[i] < l[i - 1]:
            item = l[i]
            j = i - 1
            while j >= 0 and item < l[j]:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = item
    return l


def half_insert_sort(p_l):
    """
    折半插入排序
    :param p_l:list
    :return: list
    O(n^2)
    稳定排序
    """
    l: list = copy.copy(p_l)
    length = len(l)
    for i in range(1, length):
        low, high = 0, i - 1
        item = l[i]
        while low <= high:
            mid = (low + high) // 2
            if item < l[mid]:
                high = mid - 1
            else:
                low = mid + 1
        j = i - 1
        while j >= high + 1:
            l[j + 1] = l[j]
            j -= 1
        l[high + 1] = item
    return l


if __name__ == '__main__':
    l_p = [49, 38, 65, 97, 76, 13, 27, 49]
    formatted_l = insert_sort(l_p)
    print(formatted_l)
    formatted_l = half_insert_sort(l_p)
    print(formatted_l)
