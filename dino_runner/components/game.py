import pygame
import random


from dino_runner.components.clouds import Cloud

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.dino import Dino
from dino_runner.utils import text_utils
from dino_runner.utils.constants import (
    BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS 
)   

class Game:
    def __init__(self):

        ## Configurações iniciais do jogo e do pygame
        pygame.init()
        pygame.display.set_caption(TITLE) ## Titulo da janela
        pygame.display.set_icon(ICON) ## Icone da janela
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) ## Tamanho da janela
        self.clock = pygame.time.Clock() ## FPS do jogo


        self.running = True ## Variavel que fala se o jogo tá rodando ou não
        self.player = Dino() ## Coloca o Dino dentro do componente Game

        self.obstacles = []

        ## Velocidade do Jogo
        self.game_speed = 10

        ## Lista de Nuvens
        self.clouds = [Cloud(), Cloud(), Cloud(), Cloud(), Cloud()]
       
        ## Coordenada inicial do Background
        self.x_pos_bg = 0
        self.y_pos_bg = 380
       



    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()



    def draw_background(self): ## Desenha o background do jogo
        imagem_width = BG.get_width() ## Pega a largura da imagem do background
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg)) ## Desenha o background na tela
        self.screen.blit(BG, (self.x_pos_bg + imagem_width, self.y_pos_bg)) ## Desenha o background novamente para criar o efeito de looping

        # Verifica se o background saiu da tela e reinicia a posição
        if self.x_pos_bg <= -imagem_width: 
            self.x_pos_bg = 0

        # Move o background para a esquerda de acordo com a velocidade do jogo
        self.x_pos_bg -= self.game_speed 

    def update(self):
        user_input = pygame.key.get_pressed() # Pega os inputs do usuário
        self.player.update(user_input) ## Atualiza o dino com os inputs do usuário
        
        for cloud in self.clouds: 
            cloud.update(self.game_speed)

        if len(self.obstacles) == 0:
            if random.randint(0, 1):
                self.obstacles.append(Bird())
            else:
                self.obstacles.append(Cactus())
        
        for obstacle in self.obstacles:
            obstacle.update(self.game_speed, self.obstacles)

            if self.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                self.running = False
            


    ## Desenha os componentes do jogo na tela em ordem de prioridade de cima pra baixo
    ## Primeiro limpa a tela com o fill, depois desenha o background, depois as nuvens, depois o dino
    def draw(self): 
        self.screen.fill((255, 255, 255))
        self.draw_background()
        for cloud in self.clouds:
            cloud.draw(self.screen)
        self.player.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        pygame.display.update()