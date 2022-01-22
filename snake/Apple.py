import pygame
import Game
from pygame.locals import *
import random

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("snake/images/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*Game.SIZE
        self.y = random.randint(1,19)*Game.SIZE