# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 12:09
# @Author  : TanXueFeng
# @Site    : 
# @File    : 13.py
# @Software: PyCharm
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

class Solution:
    def reOrderArray(self, array):

        even_list = []
        for i in range(len(array), 0, -1):
            if array[i - 1] % 2 == 0:
                even_list.insert(0, array.pop(i - 1))
        array.extend(even_list)
        return array


if __name__ == '__main__':
    s = Solution()
    list_p = [1, 2, 3, 4, 5]
    print(s.reOrderArray(list_p))
