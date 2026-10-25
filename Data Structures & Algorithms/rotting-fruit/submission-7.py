class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while fresh > 0:
            flag = False

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            row, col = r + dr, c + dc

                            if (0 <= row < rows and
                                0 <= col < cols and
                                grid[row][col] == 1):
                                grid[row][col] = 3
                                flag = True

            if not flag:
                return -1

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
                        fresh -= 1

            time += 1

        return time
