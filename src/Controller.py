# importing libraries
import pygame
import time
import random

from src import snake
from src import apple

pygame.init()

window_x = 480
window_y = 480

game_window = pygame.display.set_mode((window_x, window_y))
background = pygame.image.load("background.jpg")

# frames/sec controller
fps = pygame.time.Clock()

# setting default snake direction towards rihgt
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render('Game Over | Score: ' + str(score),
                                       True, 'red')
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x / 2, window_y / 2)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(5)
    pygame.quit()
    quit()


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
        snake.position[1] -= 40
    if direction == 'DOWN':
        snake.position[1] += 40
    if direction == 'LEFT':
        snake.position[0] -= 40
    if direction == 'RIGHT':
        snake.position[0] += 40

    # snake growing
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == apple.position[0] and snake.position[
            1] == apple.position[1]:
        score += 1
        apple.spawn = False
    else:
        snake.body.pop()

    if not apple.spawn:
        apple.position = [
            random.choice(apple.x_coordinates),
            random.choice(apple.y_coordinates)
        ]

    apple.spawn = True
  
    #snake & apple location!
    for pos in snake.body:
      snake.snake()
      apple.apple()

    # for when the snake dies :(
    if snake.position[0] < 0 or snake.position[0] > window_x - 10:
        game_over()
    if snake.position[1] < 0 or snake.position[1] > window_y - 10:
        game_over()

    # eating the apple!
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            game_over()

    # what's the score lol
    show_score(1, 'white', 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake.speed)
