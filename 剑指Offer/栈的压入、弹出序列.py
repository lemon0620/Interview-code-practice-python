# -*- coding:utf-8 -*-
'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

思路
利用辅助栈
'''
class Solution:
    def __init__(self):
        self.tmpstack = []
    def IsPopOrder(self, pushV, popV):
        # write code here
        for i in range(len(pushV)):
            if pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            else:
                self.tmpstack.append(pushV.pop(0))
        while self.tmpstack:
            if self.tmpstack.pop() != popV.pop(0):
                       return False
        return True