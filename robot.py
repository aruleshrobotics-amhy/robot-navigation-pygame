class Robot:
    def __init__(self, x, y, direction, environment):
        self.x = x
        self.y = y
        self.direction = direction
        self.env = environment

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def next_position(self):
        moves = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1)
        }
        dx, dy = moves[self.direction]
        return self.x + dx, self.y + dy

    def move(self):
        nx, ny = self.next_position()
        if not self.env.is_obstacle(nx, ny):
            self.x, self.y = nx, ny
        else:
            self.turn_right()
