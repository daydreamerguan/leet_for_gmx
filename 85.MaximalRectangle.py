class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp_matrix = []
        matrix_row = len(matrix)
        if not matrix_row:
            return 0
        matrix_col = len(matrix[0])
        for i in xrange(0, matrix_row + 1):
            dp_line = []
            for j in xrange(0, matrix_col + 1):
                dp_line.append([0, 0])
            dp_matrix.append(dp_line)
        final_max_area = 0
        for i in xrange(0, matrix_row):
            for j in xrange(0, matrix_col):
                if matrix[i][j] == "0":
                    dp_matrix[i + 1][j + 1] = [0, 0]
                else:
                    new_item = [0, 0]
                    new_item[0] = dp_matrix[i][j + 1][0] + 1
                    new_item[1] = dp_matrix[i + 1][j][1] + 1
                    dp_matrix[i + 1][j + 1] = new_item
                    max_area = 0
                    cnt_i = i + 1
                    cnt_j = j + 1
                    height = 1
                    cnt_max_width = new_item[1]
                    while dp_matrix[cnt_i][cnt_j][0] != 0:
                        cnt_max_width = min(cnt_max_width, dp_matrix[cnt_i][cnt_j][1])
                        cnt_area = height * cnt_max_width
                        max_area = max(cnt_area, max_area)
                        cnt_i -= 1
                        height += 1

                    cnt_i = i + 1
                    cnt_j = j + 1
                    width = 1
                    cnt_max_height = new_item[0]
                    while dp_matrix[cnt_i][cnt_j][1] != 0:
                        cnt_max_height = min(cnt_max_height, dp_matrix[cnt_i][cnt_j][0])
                        cnt_area = width * cnt_max_height
                        max_area = max(cnt_area, max_area)
                        cnt_j -= 1
                        width += 1
                    final_max_area = max(max_area, final_max_area)
        return final_max_area
