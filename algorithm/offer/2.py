# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 21:53
# @Author  : TanXueFeng
# @Site    : 
# @File    : 2.py
# @Software: PyCharm
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = s.replace(" ", "%20")
        return new_s