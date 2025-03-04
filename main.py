import pygame
import random

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")
color_snake = (40, 100, 10)
color_apple = (255, 0, 0)
clock = pygame.time.Clock()

cell_size = 20
snake_speed = 5
snake_length = 3
snake_body = []
snake_direction ="right"
snake_newdirection ="right"

for i in range(snake_length):
    snake_body.append(pygame.Rect((screen_width/2) - (cell_size*i), screen_height/4, cell_size, cell_size)
)
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.flip()
    
    for i in range(len(snake_body)):
        pygame.draw.circle(screen, color_snake, snake_body[i].center, cell_size/2)

pygame.quit()