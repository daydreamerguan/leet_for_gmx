
FULL_SET = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.valid_set = set()
        self.answer = ""

class Solution(object):

    def init_row_valid_set(self, board):
        row_set_list = []
        for x in xrange(0, 9):
            row_set = set()
            for y in xrange(0, 9):
                if board[x][y] == ".":
                    continue
                row_set.add(board[x][y])
            row_set_list.append(row_set)
        return row_set_list

    def init_col_valid_set(self, board):
        col_set_list = []
        for x in xrange(0, 9):
            col_set = set()
            for y in xrange(0, 9):
                if board[y][x] == ".":
                    continue
                col_set.add(board[y][x])
            col_set_list.append(col_set)
        return col_set_list

    def init_subbox_valid_set(self, board):
        subbox_set_list = []
        for sub_x in xrange(0, 3):
            sub_row_list = []
            for sub_y in xrange(0, 3):
                box_set = set()
                for x in xrange(0, 3):
                    for y in xrange(0, 3):
                        real_x = sub_x * 3 + x
                        real_y = sub_y * 3 + y
                        if board[real_x][real_y] == ".":
                            continue
                        box_set.add(board[real_x][real_y])
                sub_row_list.append(box_set)
            subbox_set_list.append(sub_row_list)
        return subbox_set_list


    def trySolve(self, node, answer, solved_row, solved_col, solved_subboxes):
        sub_box_x = node.x / 3
        sub_box_y = node.y / 3
        solved_row[node.x].add(answer)
        solved_col[node.y].add(answer)
        solved_subboxes[sub_box_x][sub_box_y].add(answer)
        node.answer = answer
    
    def recoverSolved(self, node, answer, solved_row, solved_col, solved_subboxes):
        sub_box_x = node.x / 3
        sub_box_y = node.y / 3
        solved_row[node.x].remove(answer)
        solved_col[node.y].remove(answer)
        solved_subboxes[sub_box_x][sub_box_y].remove(answer)
        node.answer = ""

    def getValidSet(self, x, y, solved_row, solved_col, solved_subboxes):
        sub_box_x = x / 3
        sub_box_y = y / 3
        return FULL_SET.difference(solved_row[x], solved_col[y], solved_subboxes[sub_box_x][sub_box_y])


    def recursiveSolveSudoku(self, waiting_node_list, node_count, index, solved_row, solved_col, solved_subboxes):
        if index >= node_count:
            return True
        cnt_node = waiting_node_list[index]
        waiting_answer_list = self.getValidSet(cnt_node.x, cnt_node.y, solved_row, solved_col, solved_subboxes)
        if not waiting_answer_list:
            return False
        for answer in waiting_answer_list:
            self.trySolve(cnt_node, answer, solved_row, solved_col, solved_subboxes)
            ret = self.recursiveSolveSudoku(waiting_node_list, node_count, index + 1, solved_row, solved_col, solved_subboxes)
            if ret:
                return True
            self.recoverSolved(cnt_node, answer, solved_row, solved_col, solved_subboxes)
        return False


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        solved_row = self.init_row_valid_set(board)
        solved_col = self.init_col_valid_set(board)
        solved_subboxes = self.init_subbox_valid_set(board)
        waiting_node_list = []
        for x in xrange(0, 9):
            for y in xrange(0, 9):
                if board[x][y] != ".":
                    continue
                new_node = Node(x, y)
                sub_box_x = x / 3
                sub_box_y = y / 3
                new_node.valid_set = FULL_SET.difference(solved_row[x], solved_col[y], solved_subboxes[sub_box_x][sub_box_y])
                waiting_node_list.append(new_node)
        self.recursiveSolveSudoku(waiting_node_list, len(waiting_node_list), 0, solved_row, solved_col, solved_subboxes)
        for node in waiting_node_list:
            # assert node.answer, "should have valid answer"
            board[node.x][node.y] = node.answer

if __name__ == '__main__':
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Solution().solveSudoku(board)
    print board

