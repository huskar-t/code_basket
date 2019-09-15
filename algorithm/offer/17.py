# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 15:29
# @Author  : TanXueFeng
# @Site    : 
# @File    : 17.py
# @Software: PyCharm
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
# todo
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.stack = []

    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return False
        pre2 = list(self.pre_traversal(pRoot2))
        pre1 = list(self.pre_traversal(pRoot1))
        s1 = "".join(str(i) for i in pre1)
        s2 = "".join(str(i) for i in pre2)
        return s1.count(s2) > 0

    def pre_traversal(self, node):
        self.stack.append(node)
        while self.stack:
            u = self.stack.pop()
            if u.right:
                self.stack.append(u.right)
            if u.left:
                self.stack.append(u.left)
            yield u.val


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [1, 2, 3]
    sa = "".join(str(i) for i in a)
    sb = "".join(str(i) for i in b)
    print(sa.count(sb) > 0)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node2 = TreeNode(2)
    node8.left = node9
    node8.right = node2
    s = Solution()
    print(list(s.pre_traversal(node8)))