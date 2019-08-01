# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

'''

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead.next:
            return None
        # write code here
        MeetingNode = self.MeetingNode(pHead)
        if not MeetingNode:
            return None
        
        NodeOfLoop = 1
        FlagNode = MeetingNode
        # 从相遇点定义一个指针，指针向后移动到相遇点即为环的节点数NodeOfLoop
        while FlagNode.next != MeetingNode:
            NodeOfLoop += 1
            FlagNode = FlagNode.next

        # 两个指针都位于首位，让其中一个节点向前走环的节点数步，然后第二个指针走，当两个指针相遇时，即为环节点入口
        pFast = pHead
        pSlow = pHead
        for i in range(NodeOfLoop):
            pFast = pFast.next
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next
        return pFast

    # 定义快慢指针，如果有环，快慢指针一定会相遇
    def MeetingNode(self, pHead):
        if not pHead:
            return None
        pSlow = pHead.next
        pFast = pSlow.next
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next.next
        return pSlow
            