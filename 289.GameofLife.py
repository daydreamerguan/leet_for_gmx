class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(0, row):
            for j in range(0, col):
                self.make_next_gen(board, i, j, row, col)
        for i in range(0, row):
            for j in range(0, col):
                board[i][j] = int(board[i][j] / 2)

    def make_next_gen(self, board, x, y, row, col):
        live_neighbors = 0
        neighbors_pair = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        total_neighbors = 0
        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                if x_offset == 0 and y_offset == 0:
                    continue
                nx = x + x_offset
                ny = y + y_offset
        # for nx, ny in neighbors_pair:
                if 0 <= nx < row and 0 <= ny < col:
                    total_neighbors += 1
                    if board[nx][ny] & 1 != 0:
                        live_neighbors += 1 
        dead_neighbors = total_neighbors - live_neighbors
        # print(x, y, "live", live_neighbors, "dead", dead_neighbors)
        if board[x][y] & 1 != 0:
            if 3 >= live_neighbors >= 2:
                board[x][y] += 2
        else:
            if live_neighbors == 3:
                board[x][y] += 2

if __name__ == '__main__':
    Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])