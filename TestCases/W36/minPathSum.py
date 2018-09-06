class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        row = len(grid)     #行
        col = len(grid[0])  #列

        for i in range(row):
            for j in range(col):
                if i == 0 and j ==0:
                    pass
                elif i == 0 and j != 0:      #最上面一行
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0 and i != 0:      #最左边一列
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        return grid[row-1][col-1]