import pygame


from dino_runner.components.dino import Dino
from dino_runner.utils import text_utils
from dino_runner.utils.constants import (
    BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
)   

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Dino()
        self.obstacles = []

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        pygame.display.update()