# -*- coding:utf-8 -*-

'''
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

'''

class Solution:
    def __init__(self):
        self.array = []

    def Insert(self, num):
        # write code here
        self.array.append(num)
        self.array.sort()

    def GetMedian(self, M):
        # write code here
        length = len(self.array)
        if length % 2 == 1:
            return self.array[length // 2]
        return (self.array[length // 2] + self.array[length // 2 - 1]) / 2.0