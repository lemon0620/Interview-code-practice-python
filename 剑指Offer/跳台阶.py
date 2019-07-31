# -*- coding:utf-8 -*-
'''
抽象版的斐波那契数列
1 1
2 (1 1) (2) 2
3 (1 1 1) (1 2) (2 1) 3
4 (1 1 1 1) (1 2 1) (2 1 1) (1 1 2) (2 2) 5
5 (1 1 1 1 1) (2 1 1 1) (1 2 1 1) (1 1 2 1) (1 1 1 2) (1 2 2) (2 1 2) (2 2 1) 8
...
res[n] = res[n-1]+res[n-2]
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        res = [1,2]
        if number == 1:
            return 1
        elif number == 2:
            return 2
        
        while len(res) <= number:
            res.append(res[-1]+res[-2])

        return res[number-1]