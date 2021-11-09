class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_count = len(matrix)
        col_count = 0
        if row_count > 0:
            col_count = len(matrix[0])
        size = row_count * col_count
        return self.searchMatrixRange(matrix, target, 0, size, size, col_count)

    def searchMatrixRange(self, matrix, target, start, end, size, col_size):
        if start >= end:
            return False

        mid = (start + end) / 2
        mid_row = mid /  col_size
        mid_col = mid % col_size
        cmp_result = cmp(target, matrix[mid_row][mid_col]) 
        if cmp_result == 0:
            return True
        elif cmp_result < 0:
            return self.searchMatrixRange(matrix, target, start, mid, size, col_size)
        else:
            return self.searchMatrixRange(matrix, target, mid + 1, end, size, col_size)

if __name__ == '__main__':
    print Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 100)