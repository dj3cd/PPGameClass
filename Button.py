from sounds import *
from effects import *
from parametri import *


class Button:
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height
        self.inactive = (67, 33, 94)
        self.active_color = (118, 109, 190)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.widht and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, self.widht, self.height))

            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(100)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        else:
            pygame.draw.rect(display, self.inactive, (x, y, self.widht, self.height))

        print_text(message=message, x=x + 10, y=y + 10, font_size=font_size)