import pygame
import random

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")
green = (0, 255, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()

cell_size = 20
snake_speed = 5
snake_length = 3
snake_body = []

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()