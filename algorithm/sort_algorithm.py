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


def bubble_sort(p_l):
    """
    起泡排序
    :param p_l:list
    :return:list
    O(n^2)
    稳定排序
    """
    l: list = copy.copy(p_l)
    index = len(l)
    last = 1
    while index > last:
        changed = False
        for j in range(index - 1):
            if l[j] > l[j + 1]:
                changed = True
                last = j
                l[j + 1], l[j] = l[j], l[j + 1]
        index -= 1
        if not changed:
            break
    return l


def select_sort(p_l):
    """
    简单选择排序
    :param p_l: list
    :return: list
    O(n^2)
    不稳定排序
    """
    l: list = copy.copy(p_l)
    list_length = len(l)
    for i in range(list_length):
        index = i
        for j in range(i + 1, list_length):
            if l[j] < l[index]:
                index = j
        if index != i:
            l[index], l[i] = l[i], l[index]
    return l


def shell_sort(p_l):
    """
    希尔排序
    :param p_l:list
    :return:list
    O(n^1.5)
    不稳定
    """
    l: list = copy.copy(p_l)
    list_length = len(l)
    step = int(list_length / 2)
    while step > 0:
        for i in range(step, list_length):
            left_item_index = i - step
            if left_item_index >= 0 and l[left_item_index] > l[i]:
                l[left_item_index], l[i] = l[i], l[left_item_index]
        step = int(step / 2)
    return l


def fast_sort(p_l):
    """
    快速排序递归实现
    :param p_l:
    :return:
    O(nlog(2,n))
    """
    if len(p_l) <= 1:
        return p_l
    l: list = copy.copy(p_l)
    compare_item = l[0]
    bigger_list = []
    smaller_list = []
    for i in range(1, len(l)):
        if l[i] > compare_item:
            bigger_list.append(l[i])
        else:
            smaller_list.append(l[i])
    result_list = fast_sort(smaller_list)
    result_list.append(compare_item)
    result_list.extend(fast_sort(bigger_list))
    return result_list


if __name__ == '__main__':
    l_p = [49, 38, 65, 97, 76, 13, 27, 49]
    formatted_l = insert_sort(l_p)
    print(formatted_l)
    formatted_l = half_insert_sort(l_p)
    print(formatted_l)
    formatted_l = bubble_sort(l_p)
    print(formatted_l)
    formatted_l = select_sort(l_p)
    print(formatted_l)
    formatted_l = shell_sort(l_p)
    print(formatted_l)
    formatted_l = fast_sort(l_p)
    print(formatted_l)
