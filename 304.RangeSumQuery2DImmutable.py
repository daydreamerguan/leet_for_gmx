class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.value_matrix = []
        row = len(matrix)
        col = 0
        if row > 0:
            col = len(matrix[0])

        for i in range(0, row):
            cnt_line = []
            for j in range(0, col):
                left_value = 0
                up_value = 0
                repeat_value = 0
                if j != 0:
                    left_value = cnt_line[-1]
                if i != 0:
                    up_value = self.value_matrix[i - 1][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    repeat_value = self.value_matrix[i - 1][j - 1]
                cnt_line.append(matrix[i][j] + up_value + left_value - repeat_value)
            self.value_matrix.append(cnt_line)
        print(self.value_matrix)


    def sumRegion(self, row1, col1, row2, col2):
        if(row2 < row1 or col2 < col1):
            return 0
        if(row1 == 0 and col1 == 0):
            return self.value_matrix[row2][col2]

        return self.sumRegion(
            0, 0, row2, col2) - self.sumRegion(0, 0, row1 - 1, col2) - self.sumRegion(0, 0, row2, col1 - 1) + self.sumRegion(0, 0, row1 - 1, col1 - 1)
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    print(obj.sumRegion(2,1,4,3))
    print(obj.sumRegion(1,1,2,2))
    print(obj.sumRegion(1,2,2,4))
