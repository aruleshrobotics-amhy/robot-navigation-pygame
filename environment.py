class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_obstacle(self, x, y):
        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
            return True
        return self.grid[x][y] == 1
