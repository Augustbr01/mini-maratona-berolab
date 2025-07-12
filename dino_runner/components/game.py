import pygame
import random

from dino_runner.components.clouds import Cloud
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.dino import Dino
from dino_runner.utils import text_utils
from dino_runner.utils.constants import (
    BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, RESET 
)   

class Game:
    def __init__(self):

        ## Configurações iniciais do jogo e do pygame
        pygame.init()
        pygame.display.set_caption(TITLE) ## Titulo da janela
        pygame.display.set_icon(ICON) ## Icone da janela
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) ## Tamanho da janela
        self.clock = pygame.time.Clock() ## FPS do jogo
        self.screen.fill((255, 255, 255))


        self.running = True
        self.playing = True
         ## Variavel que fala se o jogo tá rodando ou não
        self.player = Dino() ## Coloca o Dino dentro do componente Game

        self.obstacles = []

        ## Velocidade do Jogo
        self.game_speed = 20

        ## Lista de Nuvens
        self.clouds = [Cloud(), Cloud(), Cloud(), Cloud(), Cloud()]
       
        ## Coordenada inicial do Background
        self.x_pos_bg = 0
        self.y_pos_bg = 420

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if self.playing: ## Se o jogo não estiver rodando, mostra a tela de game over
                self.update()
                
            self.clock.tick(FPS)
            self.draw()

        pygame.quit() ## Fecha o pygame quando o jogo acaba
            
    
    def draw_background(self): ## Desenha o background do jogo
        imagem_width = BG.get_width() ## Pega a largura da imagem do background
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg)) ## Desenha o background na tela
        self.screen.blit(BG, (self.x_pos_bg + imagem_width, self.y_pos_bg)) ## Desenha o background novamente para criar o efeito de looping

        if self.playing:# Verifica se o background saiu da tela e reinicia a posição
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
            if random.randint(0, 1) == 0:
                self.obstacles.append(Cactus())      
            else:
                self.obstacles.append(Bird())
        
        for obstacle in self.obstacles:
            obstacle.update(self.game_speed, self.obstacles)

            if self.player.rect.colliderect(obstacle.rect):
                self.playing = False        
         
            
    def game_over(self):
        if not self.playing:
            image_width = GAMEOVER.get_width() ## Pega a largura da imagem do game over
            image_height = GAMEOVER.get_height()
            image_reset_width = RESET.get_width()
            image_reset_height = RESET.get_width()
             ## Pega a altura da imagem do game over
            self.screen.blit(GAMEOVER, (SCREEN_WIDTH // 2 - image_width // 2, (SCREEN_HEIGHT // 2 - image_height // 2) - 55))
            self.screen.blit(RESET, (SCREEN_WIDTH // 2 - image_reset_width // 2, SCREEN_HEIGHT // 2 - image_reset_height // 2))

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            reset_rect = RESET.get_rect()
            reset_rect.topleft = (SCREEN_WIDTH // 2 - image_reset_width // 2, SCREEN_HEIGHT // 2 - image_reset_height // 2 - 10)
            
            # Verifica clique no botão RESET
            if reset_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
                self.__init__()

            # Verifica barra de espaço
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.__init__()
            

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
        
        self.game_over()
        pygame.display.update()
        