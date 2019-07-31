# -*- coding:utf-8 -*-
'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
思路：
（1）暴力解法也可--Power
（2）快速幂算法
（3）使用递归，时间复杂度O(logn)
    当n为偶数，a^n =（a^n/2）*（a^n/2）
    当n为奇数，a^n = a^[(n-1)/2] * a^[(n-1)/2] * a

'''
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base ** exponent

    def fast_power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        e = abs(exponent)
        tmp = base
        res = 1
        while(e > 0):
            #如果最后一位为1，那么给res乘上这一位的结果
            if (e & 1 == 1):  ## & 是否为奇数
                res =res * tmp
            e = e >> 1   ## 二进制右移，少一位
            tmp = tmp * tmp
        return res if exponent > 0 else 1/res