# -*- coding:utf-8 -*-

'''
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。


'''

class Solution:
    def __init__(self):
        # 存储当前字符
        self.alist = []
        # 存储当前字符及其出现次数，出现大于1次，就设成2次
        self.adict = {}
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return '#'
        else:
            return self.alist[0]
        
    def Insert(self, char):
        # write code here
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        else:
            self.adict[char] = 2
        