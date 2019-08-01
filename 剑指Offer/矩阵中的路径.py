# -*- coding:utf-8 -*-

'''
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。


'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        # 模拟的字符矩阵
        markmatrix = [0] * (rows * cols)
        pathlength = 0
        # 从第一个开始递归，当然第一二个字符可能并不位于字符串之上，所以有这样一个双层循环找起点用的，一旦找到第一个符合的字符串，就开始进入递归，
        # 返回的第一个return Ture就直接跳出循环了。
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathlength, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathlength, markmatrix):
        # 说明已经找到该路径，可以返回True
        if len(path) == pathlength:
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathlength] and not \
                markmatrix[row * cols + col]:
            pathlength += 1
            markmatrix[row * cols + col] = True
            # 进行该值上下左右的递归
            hasPath = self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathlength, markmatrix)

            # 对标记矩阵进行布尔值标记
            if not hasPath:
                pathlength -= 1
                markmatrix[row * cols + col] = False
        return hasPath