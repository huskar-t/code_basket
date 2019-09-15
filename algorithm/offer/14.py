# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 12:30
# @Author  : TanXueFeng
# @Site    : 
# @File    : 14.py
# @Software: PyCharm

# 输入一个链表，输出该链表中倒数第k个结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.stack = []

    def FindKthToTail(self, head, k):
        # write code here
        self.stack_in(head)
        if k > len(self.stack) or k < 1:
            self.stack = []
            return None
        s = self.stack[-k]
        self.stack = []
        return s

    def stack_in(self, head):
        if head:
            self.stack.append(head)
            self.stack_in(head.next)
