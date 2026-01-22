import pygame
import sys
from environment import Environment
from robot import Robot

# Grid definition
grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

CELL_SIZE = 100
WIDTH = HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-Time Robot Navigation Simulation")

clock = pygame.time.Clock()

env = Environment(grid)
robot = Robot(0, 0, 'E', env)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (200, 0, 0)

def draw_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

            if grid[i][j] == 1:
                pygame.draw.rect(screen, RED, rect)

def draw_robot():
    rect = pygame.Rect(
        robot.y * CELL_SIZE + 20,
        robot.x * CELL_SIZE + 20,
        CELL_SIZE - 40,
        CELL_SIZE - 40
    )
    pygame.draw.rect(screen, BLUE, rect)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    robot.move()

    screen.fill(WHITE)
    draw_grid()
    draw_robot()
    pygame.display.flip()

    clock.tick(2)  # speed control (FPS)
