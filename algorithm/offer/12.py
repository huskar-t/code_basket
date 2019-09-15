# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 11:11
# @Author  : TanXueFeng
# @Site    : 
# @File    : 12.py
# @Software: PyCharm
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#
# 保证base和exponent不同时为0

# 降幂
import math


class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        odd = False
        temp = base
        negative_times = False
        if exponent < 0:
            negative_times = True
            exponent = -exponent
        times = exponent
        if exponent % 2 == 1:
            # 奇数减一
            times = exponent - 1
            odd = True
        while times > 1:
            temp *= temp
            times = int(times/2)
        if odd:
            temp *= base
        return temp if not negative_times else 1/temp

if __name__ == '__main__':
    s = Solution()
    print(s.Power(2,0))
    print(math.pow(2,-4))