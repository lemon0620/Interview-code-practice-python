# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

*什么是平衡二叉树？
平衡二叉树又称为AVL树，且具有一下性质：它是一颗空树或它的左右两个子树的高度差的绝对值不超过1，而且左右两个子树都是一颗平衡二叉树。

思路
根据二叉树的性质进行递归判断即可
'''

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            # 返回True是因为这是最后的判断依据，在不断递归中，最后是叶子节点，即终止，如果叶子节点时，依然左右子树之差小于1，那么就是平衡二叉树，返回True
            return True
        depth1 = self.GetDepth(pRoot.left)
        depth2 = self.GetDepth(pRoot.right)
        if abs(depth1 - depth2) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def GetDepth(self, root):
        if not root:
            return 0
        return max(self.GetDepth(root.left), self.GetDepth(root.right)) + 1