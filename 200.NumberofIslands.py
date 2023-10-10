class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ret = 0
        grid_height = len(grid)
        if grid_height == 0:
            return ret
        grid_width = len(grid[0])
        grid_state = [[0 for i in xrange(grid_width)] for j in xrange(grid_height)]
        for i in xrange(0, grid_height):
            for j in xrange(0, grid_width):
                if grid_state[i][j] != 0:
                    continue
                if grid[i][j] != "1":
                    continue
                self.dfs(grid, grid_state, i, j, grid_height, grid_width)
                ret += 1
        return ret

    def dfs(self, grid, grid_state, i, j, grid_height, grid_width):
        if i < 0 or i >= grid_height:
            return
        if j < 0 or j >= grid_width:
            return
        if grid_state[i][j] == 1:
            return
        if grid[i][j] != "1":
            return
        grid_state[i][j] = 1
        self.dfs(grid, grid_state, i + 1, j, grid_height, grid_width)
        self.dfs(grid, grid_state, i - 1, j, grid_height, grid_width)
        self.dfs(grid, grid_state, i, j + 1, grid_height, grid_width)
        self.dfs(grid, grid_state, i, j - 1, grid_height, grid_width)
