from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Count fresh oranges and enqueue all rotten ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0

        # BFS
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))

        return time if fresh == 0 else -1

        #T:O(M*N), S:O(M*N)