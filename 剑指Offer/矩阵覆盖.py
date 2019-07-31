# -*- coding:utf-8 -*-
'''
题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：
变种的斐波那契数列
'''
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            res = [0, 1, 2]
            while len(res) <= number:
                res.append(res[-1] + res[-2])
            return res[number]