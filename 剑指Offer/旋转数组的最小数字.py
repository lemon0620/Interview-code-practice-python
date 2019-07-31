# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        pre = -7e20
        for num in rotateArray:
            if num < pre :
                return num
            pre = num
             
        if len(rotateArray) == 0:
            return 0
        return rotateArray[0]

'''
解法二：二分法，寻找最小数值
'''