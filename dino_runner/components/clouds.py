import pygame
import random

from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.x = random.randint(1100, 1500)
        self.y = random.randint(20, 150)
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.x -= game_speed // 1.5  # Move mais devagar que o chão

        if self.x < -self.width:
            self.x = random.randint(1100, 1500)
            self.y = random.randint(20, 150)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
