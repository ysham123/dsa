class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        count = 0

        def dfs(x,y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == "0":
                return
            grid[x][y] = "0"

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count

            #time: O(m * n), space: O(m * n) 