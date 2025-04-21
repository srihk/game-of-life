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

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
frameCount = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
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
    pygame.draw.rect(screen, "red", rect=pygame.Rect((player_pos), (40, 40)))

    # keys = pygame.key.get_pressed()
    frameCount += 1
    if (frameCount % 60 == 0):
        player_pos.y -= 40
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
