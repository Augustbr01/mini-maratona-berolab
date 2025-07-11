import pygame

from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING, DEFAULT_TYPE, SHIELD_TYPE

class Dino:
    X_POS = 200 ## Inicia a posição X do Dino
    Y_POS = 350 ## Inicia a posição Y do Dino
    Y_POS_DUCK = 380 ## Inicia a posição Y do Dino quando ele está agachado
    JUMP_VEL = 8.5 ## Velocidade do pulo do Dino

    def __init__(self): 
        ## Define as imagens do Dino para cada ação
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        ## Define o estado de ação do dino
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        ## Define o inicio dos passos do dino
        self.step_index = 0

        ## Define o tipo do dino
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.rect.width -= 7
        self.rect.height -= 7

    ## Atualiza o estado do dino com base nos inputs do usuário
    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        ## Print pra debug do estado (temporario, vai ser removido depois)
        print("duck:", self.dino_duck, "run:", self.dino_run, "jump:", self.dino_jump)

        ## Verifica os inputs do usuário e atualiza o estado do dino
        if user_input[pygame.K_w] and not self.dino_jump and not self.dino_duck: ## Se o usuário pressionar a tecla W, o dino vai pular
            self.dino_jump = True 
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_s] and not self.dino_jump: ## Se o usuário pressionar a tecla S, o dino vai agachar
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not user_input[pygame.K_s]: ## Se o usuário não estiver pressionando a tecla S e o dino não estiver pulando, o dino vai correr
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
        
        ## Atualiza e reseta os passos do dino 
        if self.step_index >= 10: 
            self.step_index = 0
        

        
    def run(self):
        self.image = self.run_img[self.step_index // 5] ## Atualiza a imagem do dino para a imagem de corrida conforme muda o step Index
        self.rect.y = self.Y_POS ## Atualiza a posição Y do dino para a posição normal
        self.step_index += 1 ## Incrementa o step index para a próxima imagem

    def duck(self):
        self.image = self.duck_img[self.step_index // 5] ## Atualiza a imagem do dino para a imagem de agachamento conforme muda o step Index
        self.rect.y = self.Y_POS_DUCK ## Atualiza a posição Y do dino para a posição de agachamento
        self.step_index += 1 ## Incrementa o step index para a próxima imagem

    def jump(self): 
        self.image = self.jump_img ## Atualiza a imagem do dino para a imagem de pulo
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 3.5 ## Atualiza a posição Y do dino para cima conforme a velocidade do pulo
            self.jump_vel -= 1 ## Diminui a velocidade do pulo para simular a gravidade

        if self.jump_vel < -self.JUMP_VEL: ## Se a velocidade do pulo for menor que a velocidade inicial do pulo, o dino vai voltar para a posição normal
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL ## Reseta a velocidade do pulo

        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y)) ## Desenha o dino na tela na posição X e Y atual