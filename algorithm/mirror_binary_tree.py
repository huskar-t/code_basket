# encoding: utf-8
# 判断一颗二叉树是否为镜像对称
# 解法：判断一个数是否为镜像对称：先判断根，在判断左右子树。如果左右子树都为空那就是，如果左右子树不是同时为空那就不是
#
# 当左右子树都存在的时候，判断他们的值是否相等,如果相等那么就递归的对他们的子节点判断（左边的左=右边的右；左边的右==右边的左）


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def mirror(self, root):
        # write code here
        if root:
            root.left, root.right = root.right, root.left
            self.mirror(root.left)
            self.mirror(root.right)


if __name__ == '__main__':
    tree = [None for i in range(8)]
    for i in range(1, 4):
        root = tree[i] if tree[i] else TreeNode(i)
        left_node = tree[2 * i] if tree[2 * i] else TreeNode(2 * i)
        right_node = tree[2 * i + 1] if tree[2 * i + 1] else TreeNode(2 * i + 1)
        root.left = left_node
        root.right = right_node
        tree[i] = root
        tree[2 * i] = left_node
        tree[2 * i + 1] = right_node
    s1 = tree[1].left
    solution = Solution()
    # 生成镜像树
    solution.mirror(tree[1])
    s2 = tree[1].right
    print(s2 == s1)
