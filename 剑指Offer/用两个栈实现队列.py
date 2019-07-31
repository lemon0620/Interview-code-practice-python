# -*- coding:utf-8 -*-
'''
栈和队列的区别为：
队列是先进先出的，就像一条路，有一个入口和一个出口。
栈像一个箱子，后放的在上边，所以后进后出。
栈是限定只能在表的一端进行插入和删除操作的线性表。队列是限定只能在表的一端进行插入和另一端进行删除操作的线性表。
'''
class Solution:
    def __init__(self):
        self.stack_A = []
        self.stack_B = []
    
    def push(self, node):
        # write code here
        self.stack_A.append(node)
    def pop(self):
        # return xx
        if self.stack_B:
            return self.stack_B.pop()
        elif not self.stack_A:
            return None
        else:
            while self.stack_A:
                self.stack_B.append(self.stack_A.pop())
            return self.stack_B.pop()