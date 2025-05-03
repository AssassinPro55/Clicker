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
        pass

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Upgrade(GameSprite):
    def update(self):
        pass

# Очки
score = 0

# Текст
font.init()
font1 = font.SysFont('Arial', 45)

# Музыка
mixer.init()
mixer.music.load('Music_Doors.ogg')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Спрайты
button = Player("Button.png", 110, 200, 150, 150)
upgrades = Upgrade("Updates_list.png", 380, 10, 520, 520)

# Цикл
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button.collidepoint(x, y):
                score += 1
            


    if finish != True:
        window.blit(bg, (0, 0))

        button.reset()
        upgrades.reset()

        button.update()
        upgrades.update()

        # ОТрисовка текст
        text_score = font1.render("Баллы: " + str(score), 1, (255, 255, 255))
        window.blit(text_score, (10, 20))

        display.update()
    clock.tick(FPS)
