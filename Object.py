from parametri import display



class Object:
    def __init__(self, x, y, widht, image, speed):
        self.x = x
        self.y = y
        self.width = widht
        self.image = image
        self.speed = speed

    # функция передвижения кактуса
    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            # pygame.draw.rect(display, (224, 121, 39), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))