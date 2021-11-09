class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board_width = len(board)
        board_heigth = len(board[0])
        visited_board = []
        for i in xrange(0, board_width):
            cnt_line = [0 for x in xrange(0, board_heigth)]
            visited_board.append(cnt_line)

        for i in xrange(0, board_width):
            for j in xrange(0, board_heigth):
                if self.search(board, word, 0, visited_board, i, j, board_width, board_heigth):
                    return True
        return False


    def search(self, board, word, index, visited_board, cnt_x, cnt_y, board_width, board_heigth):
        # print cnt_x, cnt_y,  word[index]
        if visited_board[cnt_x][cnt_y] != 0:
            return False
        if board[cnt_x][cnt_y] != word[index]:
            return False
        
        index += 1
        visited_board[cnt_x][cnt_y] = 1
        if index == len(word):
            return True

        left_x = cnt_x - 1
        left_y = cnt_y
        if left_x >= 0 and left_x < board_width:
            ret = self.search(board, word, index, visited_board, left_x, left_y, board_width, board_heigth)
            if ret:
                return ret

        right_x = cnt_x + 1
        right_y = cnt_y
        if right_x >= 0 and right_x < board_width:
            ret = self.search(board, word, index, visited_board, right_x, right_y, board_width, board_heigth)
            if ret:
                return ret

        up_x = cnt_x
        up_y = cnt_y - 1
        if up_y >= 0 and up_y < board_heigth:
            ret = self.search(board, word, index, visited_board, up_x, up_y, board_width, board_heigth)
            if ret:
                return ret

        down_x = cnt_x
        down_y = cnt_y + 1
        if down_y >= 0 and down_y < board_heigth:
            ret = self.search(board, word, index, visited_board, down_x, down_y, board_width, board_heigth)
            if ret:
                return ret

        visited_board[cnt_x][cnt_y] = 0
        return False

if __name__ == '__main__':
    print Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    print Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")



        