# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

思路
用一个队列保留要打印的结点，打印队列最开始的root的值，将其左子树和右子树压入队列
'''
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res