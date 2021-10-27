class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result_list = []
        state = 0
        start_col = 0
        start_row = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[0]) - 1
        handle_map = {
            0: self.trimFirstRow,
            1: self.trimLastCol,
            2: self.trimLastRow,
            3: self.trimFirstCol
        }
        while end_row >= start_row and end_col >= start_col:
            handle = handle_map[state]
            state, start_row, end_row, start_col, end_col = handle(matrix, start_row, end_row, start_col, end_col, result_list)
        return result_list



    def trimFirstRow(self, matrix, start_row, end_row, start_col, end_col, result_list):
        for col in xrange(start_col, end_col + 1):
            result_list.append(matrix[start_row][col])
        return 1, start_row + 1, end_row, start_col, end_col

    def trimLastCol(self, matrix, start_row, end_row, start_col, end_col, result_list):
        for row in xrange(start_row, end_row + 1):
            result_list.append(matrix[row][end_col])
        return 2, start_row, end_row, start_col, end_col - 1

    def trimLastRow(self, matrix, start_row, end_row, start_col, end_col, result_list):
        for col in xrange(end_col, start_col - 1, -1):
            result_list.append(matrix[end_row][col])
        return 3, start_row, end_row - 1, start_col, end_col

    def trimFirstCol(self, matrix, start_row, end_row, start_col, end_col, result_list):
        for row in xrange(end_row, start_row - 1, -1):
            result_list.append(matrix[row][start_col])
        return 0, start_row, end_row, start_col + 1, end_col

if __name__ == '__main__':
    print Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
