import pygame
import random
import math
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = 'left'
RIGHT = 'right'
class Enemy_2(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 0.5

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(30 , 100)
        self.moving_index = 0

    def update(self, ships):
        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT

        if self.movement == LEFT:
            self.rect.x -= self.speed_x
            self.rect.y = self.Y_POS + int(50 * math.sin(self.rect.x / 50))
            self.Y_POS += self.speed_y
        else:
            self.rect.x += self.speed_x
            self.rect.y = self.Y_POS + int(50 * math.sin(self.rect.x / 50))  # Circular motion along the y-axis constantes: amplitud y frecuencia
            self.Y_POS += self.speed_y

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.rect.x = random.randint(0 , SCREEN_WIDTH)
            self.movement = LEFT if self.movement == RIGHT else RIGHT
            

    def draw(self, screen):
        screen.blit(self.image ,(self.rect.x, self.rect.y))