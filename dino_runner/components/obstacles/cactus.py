import random
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self):
        if random.randint(0, 1) == 0:
            cactus_list = SMALL_CACTUS
            y_pos = 365
        else:
            cactus_list = LARGE_CACTUS
            y_pos = 340

        image = random.choice(cactus_list)

        super().__init__(image, 0)
        self.rect.y = y_pos