# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 23:19
# @Author  : TanXueFeng
# @Site    : 
# @File    : 7.py
# @Software: PyCharm
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
import math


class Solution:
    def Fibonacci(self, n):
        return int((1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n))

class Solution2:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            s = []*n
            s.append(1)
            s.append(1)
            for i in range(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(1000))
    s2 = Solution()
    print(s2.Fibonacci(1000))