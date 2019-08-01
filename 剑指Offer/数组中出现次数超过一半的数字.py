# -*- coding:utf-8 -*-
'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

思路
先找出出现次数最多的数字
再计算该数字出现的次数是否大于一半
'''

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        number = numbers[0]
        for i in numbers[1:]:
            if number == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    number = i
                    count += 1

        sum = 0
        for j in numbers:
            if j == number:
                sum += 1

        return number if sum > len(numbers) // 2 else 0
        