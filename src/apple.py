import pygame

class apple(pygame.sprite.Sprite):
  def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
    
      self.image = pygame.image.load("apple.png")
      self.rect = self.image.get_rect()
    
      self.rect.x = x
      self.rect.y = y
      