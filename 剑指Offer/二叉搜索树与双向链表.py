# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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