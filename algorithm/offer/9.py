# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 00:20
# @Author  : TanXueFeng
# @Site    : 
# @File    : 9.py
# @Software: PyCharm
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)