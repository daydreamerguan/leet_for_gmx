class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        return self.findPath(0, 0, {}, grid, row, col)

    def findPath(self, x, y, result_dict, grid, row, col):
        if x == row - 1 and y == col - 1:
            return grid[x][y];
        if (x, y) in result_dict:
            return result_dict[(x, y)]
        result = 200 * 200 * 200
        if x < row - 1:
            result = min(self.findPath(x + 1, y, result_dict, grid, row, col), result)

        if y < col - 1:
            result = min(self.findPath(x, y + 1, result_dict, grid, row, col), result)
        result += grid[x][y]
        result_dict[(x, y)] = result
        return result
