# -*- coding:utf-8 -*-

'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

*什么是二叉搜索树？
    二叉查找树。它或者是一颗空树，或者是具有下列性质的二叉树；若它的左子树不空，则左子树上所有结点的值均小于它的根节点的值；若它的右子树不空，则右子树上所有结点的值均大于它的根节点的值；它的左、右子树也分别为二叉排序树。
   
思路
后序遍历： left->right->root
数组的最后一个值是root，此时，数组可以分成两个部分：小于root的部分为左子树，大于root的部分为右子树。再依次递归判断其左子树和右子树。
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        
        root = sequence[-1]
        
        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1
            
        for node in sequence[i:-1]:
            if node < root:
                return False
            i += 1

        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence)-2 and left:
            right = self.VerifySquenceOfBST(sequence[i:])
        return left and right