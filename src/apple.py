import pygame


class apple(pygame.sprite.Sprite):
  def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)

      self.rect.x = x
      self.rect.y = y
      