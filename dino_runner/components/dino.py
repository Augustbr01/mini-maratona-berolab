import pygame
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING, DEFAULT_TYPE, SHIELD_TYPE

class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        print("duck:", self.dino_duck, "run:", self.dino_run, "jump:", self.dino_jump)



        if user_input[pygame.K_w] and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_s] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not user_input[pygame.K_s]:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
        
        if self.step_index >= 10:
            self.step_index = 0

        
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
