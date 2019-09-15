# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 12:42
# @Author  : TanXueFeng
# @Site    : 
# @File    : 15.py
# @Software: PyCharm
# 输入一个链表，反转链表后，输出新链表的表头。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def __init__(self):
        self.stack = []

    def ReverseList(self, pHead):
        # write code here
        new_head = None
        self.stack_in(pHead)
        stack_length = len(self.stack)
        for i in range(stack_length):
            node = self.stack.pop()
            if i == 0:
                new_head = node
            if i == stack_length - 1:
                node.next = None
            else:
                node.next = self.stack[-1]
        return new_head

    def stack_in(self, node):
        if node:
            self.stack.append(node)
            if node.next:
                self.stack_in(node.next)
