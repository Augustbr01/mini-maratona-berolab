import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type

        if isinstance(image, list):

            self.rect = self.image[0].get_rect()
        else:
            self.rect = image.get_rect()

        self.rect.x = SCREEN_WIDTH



    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
    def draw(self, screen):
        if isinstance(self.image, list):
            screen.blit(self.image[0], self.rect)
        else:
            screen.blit(self.image, self.rect)
