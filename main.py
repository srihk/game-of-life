# Example file showing a circle moving on screen
import pygame
from cell import Cell
import random

grid = []

def buildGrid():
    w = screen.get_width()
    h = screen.get_height()

    for i in range(0, w, 40):
        row = []
        for j in range(0, h, 40):
            state = Cell.State.ALIVE
            if (int(random.random() * 10) % 2 == 0):
                state = Cell.State.DEAD
            row.append(Cell(pygame.Rect((i, j), (40, 40)), state))
        grid.append(row)

def drawGrid():
    for row in grid:
        for cell in row:
            pygame.draw.rect(screen, cell.getColor(), cell.rect)

def isValid(i: int, j: int) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    if (i >= 0 and i < rows and j >= 0 and j < cols):
        return True
    
    return False

def neighborCount(i: int, j: int, state: Cell.State):
    offsets = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]
    count = 0;
    for offset in offsets:
        if (isValid(i + offset[0], j + offset[1]) and grid[i + offset[0]][j + offset[1]].state == state):
            count += 1
    
    return count

def updateGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            liveNeighborCount = neighborCount(i, j, Cell.State.ALIVE)
            if (
                grid[i][j].state == Cell.State.ALIVE 
                and (liveNeighborCount < 2 or liveNeighborCount > 3)
            ):
                grid[i][j].state = Cell.State.DEAD
            elif (grid[i][j].state == Cell.State.DEAD and liveNeighborCount == 3):
                grid[i][j].state = Cell.State.ALIVE


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
frameCount = 0

buildGrid()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    drawGrid()

    # keys = pygame.key.get_pressed()
    frameCount += 1
    if (frameCount % 60 == 0):
        updateGrid()
        prevTime = clock.get_rawtime()
    # if clock.tick(60) / 1000 == 1:
    #     player_pos.y += 40
    # if clock.tick(60) / 1000 == 1:
    #     player_pos.x -= 40
    # if clock.tick(60) / 1000 == 1:
    #     player_pos.x += 40

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
