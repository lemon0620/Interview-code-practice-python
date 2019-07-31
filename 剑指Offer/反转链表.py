# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
题目描述
输入一个链表，反转链表后，输出新链表的表头。

思路
利用temp结点
temp <- pHead.next //保留当前节点的下一个结点
pHead.next <- pre // 反转当前节点的链接，将其连接到前一个结点
pre <- pHead // 当前节点作为后一个结点的前一个节点
pHead <- temp // 将下一个结点赋值给当前节点
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = tmp
        return pre