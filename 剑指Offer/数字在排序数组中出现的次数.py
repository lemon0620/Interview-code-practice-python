# -*- coding:utf-8 -*-

'''
题目描述
统计一个数字在排序数组中出现的次数。


'''

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or k not in data:
            return 0
        if len(data) == 1 and k == data[0]:
            return 1
        
        half_idx = len(data) // 2 -1
        if data[half_idx] < k:
            return self.GetNumberOfK(data[half_idx+1:],k)
        else:
            return self.GetNumberOfK(data[:half_idx+1],k) + self.GetNumberOfK(data[half_idx+1:],k)
           
        