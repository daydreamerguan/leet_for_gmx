# not best solution
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        max_l_size_matrix = self.init_matrix_size_int_matrix(matrix)
        for i in range(0, row):
            for j in range(0, col):
                max_l_size_matrix[i][j] = self.get_max_l_size(matrix, row, col, i, j)
        # print(matrix)
        # print(max_l_size_matrix)
        max_size = 0
        for i in range(0, row):
            for j in range(0, col):
                max_size = max(max_size, self.count_max_square_size(max_l_size_matrix, row, col, i, j))
        return max_size ** 2

    def count_max_square_size(self, matrix, row, col, i, j):
        ret_size = 0
        while i + ret_size < row and j + ret_size < col:
            cnt_row = i + ret_size
            cnt_col = j + ret_size
            if matrix[cnt_row][cnt_col] > ret_size:
                ret_size += 1
                continue
            break
        # print(i, j, ret_size)
        return ret_size

    def get_max_l_size(self, matrix, row, col, i, j):
        ret_size = 0
        while i - ret_size >= 0 and j - ret_size >= 0:
            cnt_row = i - ret_size
            cnt_col = j - ret_size
            if matrix[i][cnt_col] == "1" and matrix[i - ret_size][j] == "1":
                ret_size += 1
                continue
            break
        return ret_size

    def init_matrix_size_int_matrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        return [[0 for j in range(0, col)] for i in range(0, row)]

if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Solution().maximalSquare(matrix)