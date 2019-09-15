# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 23:35
# @Author  : TanXueFeng
# @Site    : 
# @File    : 8.py
# @Software: PyCharm
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

# 斐波那契数列衍生
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            s = [] * number
            s.append(1)
            s.append(1)
            for i in range(2, number+1):
                s.append(s[i - 1] + s[i - 2])
            return s[number]

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(5))