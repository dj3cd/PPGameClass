from parametri import *
from image import *


def print_text(message, x, y, font_color = (252, 3, 190), font_type="abc.ttf", font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


