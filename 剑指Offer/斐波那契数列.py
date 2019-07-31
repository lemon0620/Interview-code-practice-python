# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n]