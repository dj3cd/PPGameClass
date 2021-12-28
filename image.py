import pygame

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PP_Game')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

block_img = [pygame.image.load('block0.png'), pygame.image.load('block1.png'),
             pygame.image.load('block2.png')]  # 0 - некрасивая леши | 1- коробка мирэа | 2 - красивая леши

down_image = [pygame.image.load('down0.png'), pygame.image.load('down1.png')]
up_image = [pygame.image.load('rock0.png'), pygame.image.load('rock1.png')]

hp_img = pygame.image.load("heart.png")