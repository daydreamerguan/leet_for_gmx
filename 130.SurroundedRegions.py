class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        board_width = len(board)
        board_height = 0
        if board_width:
            board_height = len(board[0])
        connected_area_list = self.getAreasConnectedList(board)
        for area in connected_area_list:
            if self.checkConnected_area(board_width, board_height, area):
                for (i, j) in area:
                    board[i][j] = 'X'
    

    def checkConnected_area(self, width, height, connected_set):
        for (i, j) in connected_set:
            if i == 0 or i == width - 1:
                return False
            if j == 0 or j == height - 1:
                return False
        return True
    

    def dfsFindConnectedArea(self, i, j, unvisited_set, width, height, connected_set):
        if (i, j) not in unvisited_set:
            return
        if i < 0 or i >= width:
            return
        if j < 0 or j >= height:
            return
        unvisited_set.remove((i, j))
        connected_set.add((i, j))
        self.dfsFindConnectedArea(i - 1, j, unvisited_set, width, height, connected_set)
        self.dfsFindConnectedArea(i + 1, j, unvisited_set, width, height, connected_set)
        self.dfsFindConnectedArea(i, j + 1, unvisited_set, width, height, connected_set)
        self.dfsFindConnectedArea(i, j - 1, unvisited_set, width, height, connected_set)


    def getAreasConnectedList(self, board):
        board_width = len(board)
        board_height = 0
        if board_width:
            board_height = len(board[0])
        ret_list = []
        unvisited_set = set();
        if not board_height:
            return ret_list
        for i in xrange(0, board_width):
            for j in xrange(0, board_height):
                if board[i][j] == 'O':
                    unvisited_set.add((i, j))

        for i in xrange(0, board_width):
            for j in xrange(0, board_height):
                if (i, j) in unvisited_set:
                    cnt_connected_set = set()
                    self.dfsFindConnectedArea(i, j, unvisited_set, board_width, board_height, cnt_connected_set)
                    ret_list.append(cnt_connected_set)
        return ret_list