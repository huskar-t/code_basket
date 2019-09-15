# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 22:13
# @Author  : TanXueFeng
# @Site    : 
# @File    : 4.py
# @Software: PyCharm
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not tin:
            return
        if len(tin) == 1:
            return TreeNode(tin[0])
        root = pre[0]
        tin_index = pre_index = -1
        exist = False
        for i in range(len(pre)):
            if exist:
                break
            for j in range(len(tin)):
                if pre[i] == tin[j]:
                    root = pre[i]
                    exist = True
                    pre_index = i
                    tin_index = j
                    break
        if not exist:
            raise Exception("input error")
        left_tree_tin = tin[:tin_index]
        right_tree_tin = tin[tin_index + 1:]
        tree_pre = pre[pre_index + 1:]
        root_node = TreeNode(root)
        root_node.left = self.reConstructBinaryTree(tree_pre, left_tree_tin)
        root_node.right = self.reConstructBinaryTree(tree_pre, right_tree_tin)
        return root_node


if __name__ == '__main__':
    s = Solution()
    print(s.reConstructBinaryTree([1,2,4,3,5,6],[4,2,1,5,3,6]))
