# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。

思路
（1）粗暴解决，利用额外的数组存储链表节点
（2）巧妙法：两个指针，先让第一个指针和第二个指针都指向头结点，然后再让第一个指正走(k-1)步，到达第k个节点。然后两个指针同时往后移动，当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点了。
'''
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if k < 1 or k > len(res):
            return 
        return res[-k]