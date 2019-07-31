# -*- coding:utf-8 -*-

'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路
利用辅助栈，永远保留当前的最小值。
'''
class Solution:
    def __init__(self):
        self.Stack = []
        self.MinStack = []
        
    def push(self, node):
        # write code here
        self.Stack.append(node)
        if self.MinStack == [] or node < self.min():
            self.MinStack.append(node)
        else:
            self.MinStack.append(self.min())
        
    def pop(self):
        # write code here
        if self.Stack == [] or self.MinStack == []:
            return None
        self.Stack.pop()
        self.MinStack.pop()
        
    def top(self):
        # write code here
        return self.Stack[-1]
    
    def min(self):
        # write code here
        return self.MinStack[-1]