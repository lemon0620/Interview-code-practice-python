# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


'''

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.IsSymmetrical(pRoot, pRoot)
    def IsSymmetrical(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IsSymmetrical(pRoot1.left, pRoot2.right) and self.IsSymmetrical(pRoot1.right, pRoot2.left)