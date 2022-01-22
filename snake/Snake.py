import pygame
import Game
from pygame.locals import *


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("snake/images/snake.svg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= Game.SIZE
        if self.direction == 'right':
            self.x[0] += Game.SIZE
        if self.direction == 'up':
            self.y[0] -= Game.SIZE
        if self.direction == 'down':
            self.y[0] += Game.SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)