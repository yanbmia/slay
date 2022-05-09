# importing libraries
import pygame
import time
import random

snake_speed = 5

# Initialising pygame
pygame.init()

# Window size
window_x = 480
window_y = 480

game_window = pygame.display.set_mode((window_x, window_y))

background = pygame.image.load("background.jpg")

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [0, 0]
# [2.5,40,80,120,160,200,240,280,320,360,400,440,480]
# [2.5, 42.5, 82.5, 122.5 ,162.5,202.5,242.5,282.5,322.5,362.5,402.5,442.5,482.5]
# defining first 4 blocks of snake body
snake_body = [[100, 42.5]]
# fruit position
x_coordinates = [0,40,80,120,160,200,240,280,320,360,400,440,480]
y_coordinates = [0,40,80,120,160,200,240,280,320,360,400,440,480]
apple_position = [
    random.choice(x_coordinates),
    random.choice(y_coordinates)
]

apple_img = pygame.image.load('apple.png')
apple_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render('Game Over | Score: ' + str(score),
                                       True, 'red')
    #game_over_surface = my_font.render('End Game: ' + str(score), True, 'red')

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 2)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(5)
    pygame.quit()
    quit()

def snake():
  pygame.draw.rect(game_window, 'forestgreen',
                         pygame.Rect(pos[0], pos[1], 40, 40))
def apple():
  pygame.draw.rect(game_window, 'gray',
                     pygame.Rect(apple_position[0], apple_position[1], 40, 40))
  #game_window.blit(apple_img, apple_position)

  

# Main Function
while True:
    game_window.blit(background, (0, 0))
    # key clicks
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # for when multiple clicks are pressed
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # user controlled snake
    if direction == 'UP':
        snake_position[1] -= 40
    if direction == 'DOWN':
        snake_position[1] += 40
    if direction == 'LEFT':
        snake_position[0] -= 40
    if direction == 'RIGHT':
        snake_position[0] += 40

    # snake growing
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[
            1] == apple_position[1]:
        score += 1
        apple_spawn = False
    else:
        snake_body.pop()

    if not apple_spawn:
        apple_position = [
            random.choice(x_coordinates),
            random.choice(y_coordinates)
        ]

    apple_spawn = True
    #background color
    #game_window.fill('gray')
  
    #snake & apple location!
    for pos in snake_body:
      snake()
      apple()
        #pygame.draw.rect(game_window, 'forestgreen',
                         #pygame.Rect(pos[0], pos[1], 40, 40))
    #pygame.draw.rect(game_window, 'red',
                     #pygame.Rect(apple_position[0], apple_position[1], 40, 40))
    #apple = pygame.image.load("apple.png")

      
  

    # for when the snake dies :(
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # eating the apple!
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # what's the score lol
    show_score(1, 'white', 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake_speed)
