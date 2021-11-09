class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_count = len(matrix)
        col_count = 0
        if row_count > 0:
            col_count = len(matrix[0])

            zero_row = set()
            zero_col = set()
            for i in xrange(0, row_count):
                for j in xrange(0, col_count):
                    if matrix[i][j] == 0:
                        zero_row.add(i)
                        zero_col.add(j)
            for modify_row in zero_row:
                for i in xrange(0, col_count):
                    matrix[modify_row][i] = 0

            for modify_col in zero_col:
                for i in xrange(0, row_count):
                    matrix[i][modify_col] = 0
