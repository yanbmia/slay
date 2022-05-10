import pygame


class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      
      self.rect.x = x
      self.rect.y = y

  def move(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        self.rect.x = self.rect.x - 1
    elif keys[pygame.K_RIGHT]:
        self.rect.x = self.rect.x + 1
    elif keys[pygame.K_UP]:
        self.rect.y = self.rect.y + 1
    elif keys[pygame.K_DOWN]:
        self.rect.y = self.rect.y - 1

      
    
  