# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

思路
利用中序遍历的思想，先给结点排序
再将结点的前后链接起来
'''
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        
        self.attr = []
        self.midorder(pRootOfTree)
        for i, v in enumerate(self.attr[:-1]):
            v.right = self.attr[i + 1]
            self.attr[i+1].left = v
        return self.attr[0]
    
    def midorder(self, root):
        if not root:
            return
        self.midorder(root.left)
        self.attr.append(root)
        self.midorder(root.right)