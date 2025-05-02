from pygame import *
from random import randint
from time import sleep

FPS = 60
clock = time.Clock()

# Окно
H = 550
W = 900
window = display.set_mode((W, H))
display.set_caption('Doors Clicker')
bg = transform.scale(image.load('Koridor.jpg'), (W, H))

"""Классы"""

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[MOUSEBUTTONDOWN]:
            pass

class Upgrade(GameSprite):
    def update(self):
        pass

class LeftandRight(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[MOUSEBUTTONDOWN]:
            pass

# Очки
score = 0

# Текст
font.init()
font1 = font.SysFont('Arial', 36)

# Музыка
mixer.init()
mixer.music.load('Music_Doors.ogg')
mixer.music.set_volume(0.3)
mixer.music.play()

# Спрайты
button = Player("Button.png", 150, 200, 150, 150)
upgrades = Upgrade("Updates_list.png", 380, 10, 520, 520)

# Цикл
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(bg, (0, 0))

        button.reset()
        upgrades.reset()

        button.update()
        upgrades.update()

        # ОТрисовка текст
        #text_score = font1.render("Счёт: " + str(score), 1, (255, 255, 255))
        #text_lost = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        #window.blit(text_score, (10, 20))
        #window.blit(text_lost, (10, 50))

        display.update()
    clock.tick(FPS)
