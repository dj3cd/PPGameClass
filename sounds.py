import pygame

pygame.init()

pygame.mixer.init()

jump_sound = pygame.mixer.Sound("kick.wav")
fail_sound = pygame.mixer.Sound("collabs.wav")
lose_sound = pygame.mixer.Sound('fail.wav')  # конец хп
hp_get_sound = pygame.mixer.Sound('hpget.wav')  # подбор хп
button_sound = pygame.mixer.Sound("button.wav")