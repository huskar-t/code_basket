# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 00:57
# @Author  : TanXueFeng
# @Site    : 
# @File    : 11.py
# @Software: PyCharm
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-100))
