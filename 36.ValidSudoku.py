class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.checkRow(board) and self.checkCol(board) and self.checkSubBox(board)

    def checkRow(self, board):

        for i in xrange(0, 9):
            row_set = set()
            for j in xrange(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
        return True

    def checkCol(self, board):
        for i in xrange(0, 9):
            row_set = set()
            for j in xrange(0, 9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_set:
                    return False
                row_set.add(board[j][i])
        return True

    def checkSubBox(self, board):
        for sub_x_index in xrange(0, 3):
            for sub_y_index in xrange(0, 3):
                box_set = set() 
                for box_x_index in xrange(0, 3):
                    for box_y_index in xrange(0, 3):
                        index_x = sub_x_index * 3 + box_x_index
                        index_y = sub_y_index * 3 + box_y_index
                        if board[index_x][index_y] == ".":
                            continue
                        if board[index_x][index_y] in box_set:
                            return False
                        box_set.add(board[index_x][index_y])

        return True