import pygame

from dino_runner.components.clouds import Cloud

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
        self.clouds = [Cloud(), Cloud(), Cloud(), Cloud(), Cloud()]
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.game_speed = 10



    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()



    def draw_background(self):
        imagem_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + imagem_width, self.y_pos_bg))
        if self.x_pos_bg <= -imagem_width:
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        
        for cloud in self.clouds:
            cloud.update(self.game_speed)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        for cloud in self.clouds:
            cloud.draw(self.screen)

        self.player.draw(self.screen)
        pygame.display.update()