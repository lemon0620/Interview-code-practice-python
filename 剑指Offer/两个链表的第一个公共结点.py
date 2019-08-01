# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
题目描述
输入两个链表，找出它们的第一个公共结点。

思路：
得到两个链表的长度，再根据两链表的长度差，设立两个指针
'''

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        Length1 = self.GetLength(pHead1)
        Length2 = self.GetLength(pHead2)
        LengthDiff = abs(Length1 - Length2)

        if Length1 > Length2:
            pHeadLong = pHead1
            pHeadShort = pHead2
        else:
            pHeadLong = pHead2
            pHeadShort = pHead1

        for i in range(LengthDiff):
            pHeadLong = pHeadLong.next

        while pHeadLong != None and pHeadShort != None and pHeadLong != pHeadShort:
            pHeadLong = pHeadLong.next
            pHeadShort = pHeadShort.next

        return pHeadLong

    def GetLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length