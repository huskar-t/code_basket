# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 22:50
# @Author  : TanXueFeng
# @Site    : 
# @File    : 5.py
# @Software: PyCharm
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
class Solution:
    def __init__(self):
        self.stack1 = []

    def push(self, node):
        self.stack1.append(node)
        # write code here

    def pop(self):
        stack2 = []
        for i in range(len(self.stack1)):
            stack2.append(self.stack1.pop())
        s = stack2.pop()
        for i in range(len(stack2)):
            self.stack1.append(stack2.pop())
        return s

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
