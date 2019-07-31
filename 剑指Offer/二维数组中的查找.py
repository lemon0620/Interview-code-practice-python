# -*- coding:utf-8 -*-

'''
由于数组从左到右递增，从上到下递增，所以从数组的右上角开始找起。若当前的数字比右上角的数值大，则删除第一行的数据；若当前的数字比右上角的数值小，则删除最后一列的数据。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        column = len(array[0])
        
        i = 0
        j = column - 1
        while i < row and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i += 1
            elif target < array[i][j]:
                j -= 1
        return False