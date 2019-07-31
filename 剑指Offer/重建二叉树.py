# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
这里利用了前序遍历和中序遍历的特性。
前序遍历的遍历顺序：root->left->right
中序遍历的遍历顺序: left->root->right
所以，前序遍历的第一个值就是二叉树的root。在中序遍历中找到root的位置，其左边是左子树的数字集合，右边是右子树的数字集合。
同理，前序遍历除root外的前root_idx个词为左子树的前序遍历，后序遍历root_idx前面的序列为左子树的中序遍历。右子树同理。
利用递归进行二叉树的重建。
'''
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        
        root.left = self.reConstructBinaryTree(pre[1:val+1], tin[:val])
        root.right = self.reConstructBinaryTree(pre[val+1:], tin[val+1:])
        
        return root