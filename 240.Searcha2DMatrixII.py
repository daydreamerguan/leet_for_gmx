class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        return self.do_search(0, row, 0, col, matrix, target)

    def do_search(self, row_start, row_end, col_start, col_end, matrix, target):
        print("searching", row_start, row_end, col_start, col_end)
        if row_end <= row_start or col_start >= col_end:
            return False
        if target < matrix[row_start][col_start]:
            return False
        half_row = int((row_start + row_end) / 2)
        half_col = int((col_start + col_end) / 2)
        matrix_half = matrix[half_row][half_col]
        if matrix_half == target:
            return True
        elif matrix_half > target:
            return self.do_search(row_start, half_row, col_start, col_end, matrix, target
                ) or self.do_search(half_row, row_end, col_start, half_col, matrix, target)
            return self.do_search(row_start, half_row + 1, col_start, half_col + 1, matrix, target)
        else:
            return self.do_search(half_row + 1, row_end, col_start, col_end, 
                matrix, target) or self.do_search(row_start, half_row + 1, half_col + 1, col_end, matrix, target)



if __name__ == '__main__':
    m = [[3,3,8,13,13,18],[4,5,11,13,18,20],[9,9,14,15,23,23],[13,18,22,22,25,27],[18,22,23,28,30,33],[21,25,28,30,35,35],[24,25,33,36,37,40]]
    print(Solution().searchMatrix(m, 21))