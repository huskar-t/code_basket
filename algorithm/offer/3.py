# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 21:56
# @Author  : TanXueFeng
# @Site    : 
# @File    : 3.py
# @Software: PyCharm
# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.result_list = []
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode:
            self.result_list.append(listNode.val)
            if listNode.next:
                self.printListFromTailToHead(listNode.next)
            else:
                self.result_list.reverse()
        return self.result_list

if __name__ == '__main__':
    l1 = ListNode(67)
    l2 = ListNode(0)
    l3 = ListNode(24)
    l4 = ListNode(58)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    s = Solution()
    print(s.printListFromTailToHead(l1))
