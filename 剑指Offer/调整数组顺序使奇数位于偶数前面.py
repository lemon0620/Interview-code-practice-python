# -*- coding:utf-8 -*-
'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

思路
类似于冒泡排序，遇见第一个偶数，与该偶数后遇到的第一个奇数互换位置
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(0, len(array)):
            for j in range(1, len(array)):
                if array[j] % 2 == 1 and array[j-1] % 2 == 0:
                    tmp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = tmp
        return array