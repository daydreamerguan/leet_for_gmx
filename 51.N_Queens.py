class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        matrix = []
        for i in xrange(0, n):
            line = []
            for j in xrange(0, n):
                line.append(0)
            matrix.append(line)
        list_result = []
        self.solveMatrix(matrix, n, list_result, 0, [])
        output_result = []
        for result in list_result:
            result_max = []
            for i in xrange(0, n):
                line = []
                for j in xrange(0, n):
                    if result[i] != j:
                        line.append(".")
                    else:
                        line.append("Q")
                result_max.append("".join(line))
            output_result.append(result_max)
        return output_result



    def checkPosValid(self, matrix, i, j, n):
        return matrix[i][j] == 0

    def markPosState(self, matrix, i, j, n, isValid):
        plus_num = 1 if not isValid else -1
        marked_indexes_set = set()
        # col
        for index in xrange(0, n):
            if (index, j) not in marked_indexes_set:
                marked_indexes_set.add((index, j))
        # line
        for index in xrange(0, n):
            if (i, index) not in marked_indexes_set:
                marked_indexes_set.add((i, index))

       
        for index in xrange(0, n):
            diff = index - i
            cnt_col = j + diff
            # cross line
            if (index, cnt_col not in marked_indexes_set) and n > cnt_col >= 0:
                marked_indexes_set.add((index, cnt_col))
            anti_cross_col = j - diff
            if (index, anti_cross_col not in marked_indexes_set) and n > anti_cross_col >= 0:
                marked_indexes_set.add((index, anti_cross_col))

        for item in marked_indexes_set:
            matrix[item[0]][item[1]] += plus_num

    def solveMatrix(self, matrix, n, q_list, index, cnt_res):

        if index >= n:
            new_res = [x for x in cnt_res]
            q_list.append(new_res)
            return
        for col in xrange(0, n):
            if not self.checkPosValid(matrix, index, col, n):
                continue
            self.markPosState(matrix, index, col, n, False)
            cnt_res.append(col)
            self.solveMatrix(matrix, n, q_list, index + 1, cnt_res)
            cnt_res.pop()
            self.markPosState(matrix, index, col, n, True)

if __name__ == '__main__':
    Solution().solveNQueens(4)