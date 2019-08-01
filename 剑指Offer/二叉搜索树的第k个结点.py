# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

思路
中序遍历

'''

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global result
        result = []
        middle = self.midorder(pRoot)
        if k <= 0 or len(middle) < k:
            return None
        else:
            return middle[k - 1]

    def midorder(self, pRoot):
        if not pRoot:
            return []
        self.midorder(pRoot.left)
        result.append(pRoot)
        self.midorder(pRoot.right)
        return result