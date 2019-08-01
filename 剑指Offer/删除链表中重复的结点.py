# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


'''

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # write code here
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next

        # filter函数和map相似，但是filter是返回布尔值去去输入列表进行判断
        res = list(filter(lambda c: res.count(c) == 1, res))

        newlist = ListNode(0)
        pre = newlist
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return newlist.next
