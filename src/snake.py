import pygame 
from src import Controller

position = [0, 0]
body = [[100, 42.5]]
speed = 5


def snake():
    pygame.draw.rect(Controller.game_window, 'forestgreen',
                     pygame.Rect(position[0], position[1], 40, 40))
    
  