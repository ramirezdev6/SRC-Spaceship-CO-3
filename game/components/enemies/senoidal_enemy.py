import pygame
import math
from game.components.enemies.enemy import Enemy

from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = 'left'
RIGHT = 'right'
class SenoidalEnemy(Enemy): #nombre - herencia // Mejorar nombre
    SPEED_Y = 0.75
    SPEED_X = 5

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X


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
            self.movement = LEFT if self.movement == RIGHT else RIGHT
            