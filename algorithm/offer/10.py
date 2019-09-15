# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 00:29
# @Author  : TanXueFeng
# @Site    : 
# @File    : 10.py
# @Software: PyCharm
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            s = [] * number
            s.append(1)
            s.append(1)
            for i in range(2, number + 1):
                s.append(s[i - 1] + s[i - 2])
            return s[number]


if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(2))
