
NEXT_NUM = 0
class Solution(object):
    def generateMatrix(self, n):
        global NEXT_NUM
        NEXT_NUM = 0
        """
        :type n: int
        :rtype: List[List[int]]
        """
        state = 0
        start_col = 0
        start_row = 0
        end_row = n - 1
        end_col = n - 1
        handle_map = {
            0: self.trimFirstRow,
            1: self.trimLastCol,
            2: self.trimLastRow,
            3: self.trimFirstCol
        }
        matrix = []
        for i in xrange(0, n):
            cnt_line = []
            for j in xrange(0, n):
                cnt_line.append(0)
            matrix.append(cnt_line)  
        while end_row >= start_row and end_col >= start_col:
            handle = handle_map[state]
            state, start_row, end_row, start_col, end_col = handle(matrix, start_row, end_row, start_col, end_col)
        return matrix

    def add_num(self, matrix, i, j):
        global NEXT_NUM
        NEXT_NUM += 1
        matrix[i][j] = NEXT_NUM

    def trimFirstRow(self, matrix, start_row, end_row, start_col, end_col):
        for col in xrange(start_col, end_col + 1):
            self.add_num(matrix, start_row, col)
        return 1, start_row + 1, end_row, start_col, end_col

    def trimLastCol(self, matrix, start_row, end_row, start_col, end_col):
        for row in xrange(start_row, end_row + 1):
            self.add_num(matrix, row, end_col)
        return 2, start_row, end_row, start_col, end_col - 1

    def trimLastRow(self, matrix, start_row, end_row, start_col, end_col):
        for col in xrange(end_col, start_col - 1, -1):
            self.add_num(matrix, end_row, col)
        return 3, start_row, end_row - 1, start_col, end_col

    def trimFirstCol(self, matrix, start_row, end_row, start_col, end_col):
        for row in xrange(end_row, start_row - 1, -1):
            self.add_num(matrix, row, start_col)
        return 0, start_row, end_row, start_col + 1, end_col

if __name__ == '__main__':
    print Solution().generateMatrix(1)
    print Solution().generateMatrix(3)
