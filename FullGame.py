import random
from Button import *
from effects import *
from Object import *
import parametri as p
from sounds import *
import image as m
from image import *
from parametri import display
from Save import *



class Game:
    def __init__(self):
        pygame.display.set_caption('PP_Jump_Game')
        pygame.display.set_icon(icon)

        self.block_options = [20, 430, 50, 450, 25, 420]
        self.img_counter = 0
        self.hp = 2
        self.make_jump = False
        self.jump_counter = 30
        self.scores = 0
        self.max_scores = 0
        self.max_above = 0
        self.land = pygame.image.load('land.png')
        self.checkprob = 1
        self.checkprob2 = 1
        self.pers_img = [pygame.image.load('anticrash.png'), pygame.image.load('anticrash.png'), pygame.image.load('anticrash.png')]
        self.heart = Object(p.display_width, 200, 35, m.hp_img, 6)
        self.save_data = Save()
        self.x = 1 #для рестарта
        self.max_scores_end = 0


    def cont(self):
        self.max_scores = self.save_data.get("max")
        self.scores = self.max_scores
        while self.game_cycle():
            pass

    def newgame(self):
        self.scores = 0
        self.save_data.save()
        self.save_data.add("max", self.scores)
        while self.game_cycle():
            pass

    def show_menu(self):
        menu_background = pygame.image.load("menu.png")

        pygame.mixer.music.load("mainmenu.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        quit_btn = Button(60, 40)
        lvl_btn1 = Button(200, 60)
        lvl_btn2 = Button(200, 60)
        pers_btn1 = Button(200, 60)
        pers_btn2 = Button(200, 60)
        terr_btn1 = Button(200, 60)
        terr_btn2 = Button(200, 60)
        sound_btn = Button(70, 40)
        sound_btn1 = Button(95, 40)
        cont_btn = Button(120, 40)
        nwg_btn = Button(120, 40)
        show = True

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            display.blit(menu_background, (0, 0))
            quit_btn.draw(730, 550, "Quit", quit, 20)
            lvl_btn1.draw(25, 300, "Cosmic", self.choose_lvl1, 20)
            lvl_btn2.draw(25, 200, "Forest", self.choose_lvl2, 20)
            pers_btn1.draw(310, 200, "Common outfit", self.choose_pers1, 20)
            pers_btn2.draw(310, 300, "Custom outfit", self.choose_pers2, 20)
            terr_btn1.draw(575, 300, "Cosmic blocks", self.choose_terr1, 20)
            terr_btn2.draw(575, 200, "Forest blocks", self.choose_terr2, 20)
            sound_btn.draw(25, 540, "Mute", self.mute, 20)
            sound_btn1.draw(100, 540, "Unmute", self.unmute, 20)
            cont_btn.draw(420, 150, "Continue", self.cont, 20)
            nwg_btn.draw(280,150, "New Game", self.newgame, 20)

            pygame.display.update()
            clock.tick(60)

    def mute(self):

        pygame.mixer.music.set_volume(0)

    def unmute(self):

        pygame.mixer.music.set_volume(0.7)

    def escpm(self):
        self.max_scores = self.scores
        self.scores = 0
        self.save_data.save()
        self.save_data.add("max", self.max_scores)
        self.show_menu()

    def choose_lvl1(self):

        self.land = pygame.image.load('land.png')

        if self.checkprob == 1:
            return
        if self.checkprob2 == 1:
            return
        #if self.checkprob2 <= 0 and self.checkprob <= 0:
            #while self.game_cycle():
                #pass

    def choose_pers1(self):

        self.pers_img = [pygame.image.load('pers0_b.png'), pygame.image.load('pers1_b.png'), pygame.image.load('pers2_b.png')]
        self.checkprob = self.checkprob - 1

        return

    def choose_terr1(self):

        m.block_img = [pygame.image.load('block0.png'), pygame.image.load('block1.png'), pygame.image.load('block2.png')]  # 0 - некрасивая леши | 1- коробка мирэа | 2 - красивая леши
        m.block_options = [20, 430, 50, 450, 25, 420]

        m.down_image = [pygame.image.load('down0.png'), pygame.image.load('down1.png')]

        m.up_image = [pygame.image.load('rock0.png'), pygame.image.load('rock1.png')]
        self.checkprob2 = self.checkprob2 - 1

        return

    def choose_lvl2(self):

        self.land = pygame.image.load('land2.png')

        if self.checkprob == 1:
            return
        if self.checkprob2 == 1:
            return
        #if self.checkprob2 <= 0 and self.checkprob <= 0:
            #while self.game_cycle():
                #pass

    def choose_pers2(self):

        self.pers_img = [pygame.image.load('pers0_z.png'), pygame.image.load('pers1_z.png'), pygame.image.load('pers2_z.png')]
        self.checkprob = self.checkprob - 1

        return

    def choose_terr2(self):

        m.block_img = [pygame.image.load('block0_z.png'), pygame.image.load('block1_z.png'), pygame.image.load('block2_z.png')]  # 0 - некрасивая леши | 1- коробка мирэа | 2 - красивая леши
        self.block_options = [20, 430, 50, 450, 25, 420]

        m.down_image = [pygame.image.load('down0_z.png'), pygame.image.load('down1_z.png')]

        m.up_image = [pygame.image.load('up0_z.png'), pygame.image.load('up1_z.png')]

        self.checkprob2 = self.checkprob2 - 1

        return

    def game_cycle(self):

        game = True
        block_arr = []
        self.create_block_arr(block_arr)
        # land = pygame.image.load('land1.png')

        up, down = self.open_random_objects()

        # = Object(p.display_width, 200, 35, m.hp_img, 6)

        button1 = Button(70, 40)
        button2 = Button(95, 40)
        button3 = Button(75, 30)
        button4 = Button(70, 40)

        #self.scores = 0
        self.make_jump = False
        self.jump_counter = 30
        p.usr_y = p.display_height - p.user_height - 110
        self.hp = 2

        pygame.mixer.music.load("background.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.make_jump = True
            if keys[pygame.K_ESCAPE]:
                self.pause()

            if self.make_jump:
                self.jump()

            self.count_scores(block_arr)

            display.blit(self.land, (0, 0))

            print_text('Scores: ' + str(self.scores), 600, 10)
            button1.draw(25, 540, "Mute", self.mute, 20)
            button2.draw(100, 540, "Unmute", self.unmute, 20)
            button3.draw(730, 5, "Menu", self.escpm, 20)

            self.draw_array(block_arr)
            self.move_objects(down, up)

            self.draw_pers()
            self.heart.move()
            self.heart_plus(self.heart)

            if self.check_collision(block_arr):
                pygame.mixer.music.stop()
                game = False

            self.show_health()

            pygame.display.update()
            clock.tick(60)  # один кадр продолжается 60мс

        return self.game_over()

    def jump(self):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pygame.mixer.Sound.play(jump_sound)
            if self.jump_counter == -25:
                pygame.mixer.Sound.play(jump_sound)

            p.usr_y -= self.jump_counter / 2
            self.jump_counter -= 1
        else:
            self.jump_counter = 30
            self.make_jump = False

    def create_block_arr(self, array):
        choice = random.randrange(0, 3)
        img = block_img[choice]
        width = self.block_options[choice * 2]
        height = self.block_options[choice * 2 + 1]
        array.append(Object(p.display_width + 20, height, width, img, 3))

        choice = random.randrange(0, 3)
        img = block_img[choice]
        width = self.block_options[choice * 2]
        height = self.block_options[choice * 2 + 1]
        array.append(Object(p.display_width + 300, height, width, img, 3))

        choice = random.randrange(0, 3)
        img = block_img[choice]
        width = self.block_options[choice * 2]
        height = self.block_options[choice * 2 + 1]
        array.append(Object(p.display_width + 600, height, width, img, 3))

    @staticmethod
    def find_radius(array):
        maximum = max(array[0].x, array[1].x, array[2].x)

        if maximum < p.display_width:

            radius = p.display_width
            if radius - maximum < 50:
                radius += 250
        else:
            radius = maximum

        choice = random.randrange(0, 5)
        if choice == 0:
            radius += random.randrange(10, 15)
        else:
            radius += random.randrange(250, 400)

        return radius

    def draw_array(self, array):
        for block in array:
            check = block.move()
            if not check:
                self.object_return(array, block)

    def object_return(self, objects, obj):
        radius = self.find_radius(objects)

        choice = random.randrange(0, 3)
        img = block_img[choice]
        width = self.block_options[choice * 2]
        height = self.block_options[choice * 2 + 1]

        obj.return_self(radius, height, width, img)

    @staticmethod
    def open_random_objects():
        choice = random.randrange(0, 2)
        img_of_down = down_image[choice]

        choice = random.randrange(0, 2)
        img_of_up = up_image[choice]

        down = Object(display_width, display_height - 80, 10, img_of_down, 10)
        up = Object(display_width, 10, 70, img_of_up, 14)

        return up, down

    @staticmethod
    def move_objects(down, up):
        check = down.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_down = down_image[choice]
            down.return_self(p.display_width, 500 + random.randrange(10, 80), down.width, img_of_down)

        check = up.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_up = up_image[choice]
            up.return_self(p.display_width, random.randrange(10, 100), up.width, img_of_up)  # высота камней

    def draw_pers(self):

        if self.img_counter == 9:
            self.img_counter = 0

        display.blit(self.pers_img[self.img_counter // 3], (p.usr_x, p.usr_y))
        self.img_counter += 1

    @staticmethod
    def pause():
        paused = True

        pygame.mixer.music.pause()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text("Paused ! Press enter to continue !", 100, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            pygame.display.update()
            clock.tick(15)

        pygame.mixer.music.unpause()

    def check_collision(self, barriers):
        for barrier in barriers:

            if p.usr_y + p.user_height >= barrier.y:
                if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                    if self.check_hp():
                        self.object_return(barriers, barrier)
                        return False
                    else:
                        return True
                elif barrier.x <= p.usr_x + p.user_width <= barrier.x + barrier.width:
                    if self.check_hp():
                        self.object_return(barriers, barrier)
                        return False
                    else:
                        return True

        return False

    def count_scores(self, barriers):
        above_block = 0

        if -20 <= self.jump_counter < 25:
            for barrier in barriers:
                if p.usr_y + p.user_height - 5 <= barrier.y:

                    if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                        above_block += 1

                    elif barrier.x <= p.usr_x + p.user_width <= barrier.x + barrier.width:
                        above_block += 1

            self.max_above = max(self.max_above, above_block)
        else:
            if self.jump_counter == -30:
                self.scores += self.max_above
                self.max_above = 0

    def restart(self):
        self.scores = 0
        self.x = 0

    def escpm1(self):
        self.scores = 0
        self.show_menu()

    def game_over(self):

        if self.scores > self.max_scores:
            self.max_scores = self.scores
        stopped = True
        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            button3 = Button(75, 30)
            button4 = Button(90, 40)

            print_text("G a m e    o v e r ! ", 250, 260, font_size=30)
            button3.draw(730, 5, "Menu", self.escpm1, 20)
            button4.draw(310, 310, "Restart", self.restart, 20)

            # print_text('Max scores: ' +str(self.max_scores), 300, 400)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.scores = 0
                return True
            if self.x == 0:
                self.x = 1
                return True

            if keys[pygame.K_ESCAPE]:
                pygame.mixer.music.load("mainmenu.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
                return False

            pygame.display.update()
            clock.tick(15)

    def show_health(self):
        show = 0
        x = 20
        while show != self.hp:
            display.blit(hp_img, (x, 20))
            x += 40
            show += 1

    def check_hp(self):
        self.hp -= 1
        if self.hp == 0:
            pygame.mixer.Sound.play(lose_sound)
            return False

        else:
            pygame.mixer.Sound.play(fail_sound)
            return True

    def heart_plus(self, heart):

        if heart.x <= -heart.width:
            radius = p.display_width + random.randrange(500, 2000)
            heart.return_self(radius, heart.y, heart.width, hp_img)

        if p.usr_x <= heart.x <= p.usr_x + p.user_width:
            if p.usr_y <= heart.y <= p.usr_y + p.user_height:
                pygame.mixer.Sound.play(hp_get_sound)
                if self.hp < 5:
                    self.hp += 1

                radius = p.display_width + random.randrange(500, 1700)
                heart.return_self(radius, heart.y, heart.width, hp_img)
