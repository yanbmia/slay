import pygame
import random

from src import Controller

# fruit position
x_coordinates = [0,40,80,120,160,200,240,280,320,360,400,440]
y_coordinates = [0,40,80,120,160,200,240,280,320,360,400,440]

position = [
    random.choice(x_coordinates),
    random.choice(y_coordinates)
]

apple_img = pygame.image.load('apple.png')
spawn = True

def apple():
  pygame.draw.rect(Controller.game_window, 'red',
                     pygame.Rect(position[0], position[1], 40, 40))