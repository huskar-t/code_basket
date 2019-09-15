# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 12:53
# @Author  : TanXueFeng
# @Site    : 
# @File    : 16.py
# @Software: PyCharm
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.map = {}

    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        self.map_in(pHead1)
        self.map_in(pHead2)
        last_item = None
        new_head = None
        keys_sort = sorted(list(self.map.keys()))
        for key in keys_sort:
            node_list = self.map[key]
            for i in range(len(node_list)):
                node = node_list[i]
                if i == 0:
                    if not new_head:
                        new_head = node
                    if last_item:
                        last_item.next = node
                if i == len(node_list) - 1:
                    last_item = node
                else:
                    node.next = node_list[i + 1]
        return new_head

    def map_in(self, node):
        if node:
            node_list = self.map.get(node.val, [])
            node_list.append(node)
            self.map[node.val] = node_list
            if node.next:
                self.map_in(node.next)


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node3
    node3.next = node5
    node2.next = node4
    node4.next = node6
    s = Solution()
    nl = s.Merge(node1, node2)
    while nl.next:
        print(nl.val)
        nl = nl.next
