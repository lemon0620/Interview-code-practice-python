# -*- coding:utf-8 -*-
import operator

'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

* 解题思路：
 * 先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
 * 排序规则如下：
 * 若ab > ba 则 a > b，
 * 若ab < ba 则 a < b，
 * 若ab = ba 则 a = b；
 * 解释说明：
 * 比如 "3" < "31"但是 "331" > "313"，所以要将二者拼接起来进行比较
'''

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        # 在python3.x中已经没有cmp函数，要是用operator函数进行比较，cmp函数就是比较输入两个字符串之间大小的数字
        # cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
        # 是两两对象之间的比较，排序默认是从小到大，在这个函数内部实现的两两排序
        numbers.sort(cmp=lambda x, y: 1 if x + y > y + x else -1)
        if numbers[0] == '0':
            return 0
        else:
            # ''.join实现了字符串之间的连接
            return ''.join(numbers)