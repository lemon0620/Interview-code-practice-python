# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

left->root->right

'''

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return
        # 该节点有右子节点，那么该节点的下一个节点就是有自己节点的最左节点
        if pNode.right != None:
            pNode = pNode.right
            while pNode.left != None:
                pNode = pNode.left
            return pNode
        # 该节点没有右子节点
        # 该节点为父节点的左子节点
        elif pNode.next != None and pNode.next.left == pNode:
            return pNode.next
        # 该节点为父节点的右子节点，它的下一个节点就是其父节点作为父节点的左子节点的下一个节点
        elif pNode.next != None and pNode.next.right == pNode:
            while pNode.next != None and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode.next
        else:
            # 节点无父节点，即节点为根节点
            return pNode.next
        