import pygame
from enum import Enum

class Cell:
    class State(Enum):
        ALIVE = 0
        DEAD = 1

    def __init__(self, rect: pygame.Rect, state: State):
        self.rect = rect
        self.state = state

    def getColor(self):
        if self.state == self.State.DEAD:
            return "black"
        else:
            return "red"
