import pygame
from image import *

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

# песронаж
user_width = 55
user_height = 75
usr_x = display_width // 3
usr_y = display_height - user_height - 110

# преграды
block_width = 20
block_height = 70
block_x = display_width - 50
block_y = display_height - block_height - 100

hp_img = pygame.transform.scale(hp_img, (35, 35))  # размер сердец

clock = pygame.time.Clock()
