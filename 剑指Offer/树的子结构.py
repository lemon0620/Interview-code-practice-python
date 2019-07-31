# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

思路
利用递归，从root开始判断，若不是，判断左子树，再判断右子树

'''
class Solution:
    def IsSubtree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val == root2.val:
            return self.IsSubtree(root1.left, root2.left) and self.IsSubtree(root1.right, root2.right)
        
    def HasSubtree(self, pRoot1, pRoot2):
        # write code her
        if not pRoot1 or not pRoot2:
            return False
        
        return self.IsSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
    
        
        
 