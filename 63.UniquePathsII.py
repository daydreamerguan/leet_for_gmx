class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        return self.findPath(0, 0, {}, obstacleGrid, row, col)

    def findPath(self, x, y, result_dict, obstacleGrid, row, col):
        if x == row - 1 and y == col - 1:
            return 1 if obstacleGrid[x][y] == 0 else 0
        if (x, y) in result_dict:
            return result_dict[x, y]

        result = 0
        if x < row - 1 and not obstacleGrid[x + 1][y]:
            result += self.findPath(x + 1, y, result_dict, obstacleGrid, row, col)

        if y < col - 1 and not obstacleGrid[x][y + 1]:
            result += self.findPath(x, y + 1, result_dict, obstacleGrid, row, col)
        result_dict[(x, y)] = result
        return result
        