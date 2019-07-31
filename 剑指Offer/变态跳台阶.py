# -*- coding:utf-8 -*-
'''
可找规律
'''
class Solution:
    def jumpFloorII(self, number):
        # write code here
        import math
        return math.pow(2,number-1)