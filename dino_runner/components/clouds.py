import pygame
import random

from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH 

class Cloud: ## Classe que representa uma nuvem no jogo
    def __init__(self):
        self.image = CLOUD ## Carrega a imagem da nuvem direto dos constants
        self.x = random.randint(1100, 1500)  # Posição X inicial da nuvem, aleatória entre 1100 e 1500
        self.y = random.randint(20, 150) ## Posição Y inicial da nuvem, aleatória entre 20 e 150
        self.width = self.image.get_width() ## Define a width largura da imagem da nuvem

    def update(self, game_speed):
        self.x -= game_speed // 1.5  # Atualiza a posição X da nuvem com base na velocidade do jogo

        if self.x < -self.width: # Se a nuvem sair da tela
            ## Reinicia a posição da nuvem
            self.x = random.randint(1100, 1500) 
            self.y = random.randint(20, 150) 

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y)) # Desenha a nuvem na tela na posição X e Y atual
