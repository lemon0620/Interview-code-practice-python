# -*- coding:utf-8 -*-

'''
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
'''

class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except:
            return 0