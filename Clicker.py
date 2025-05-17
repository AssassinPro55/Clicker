from pygame import *
from random import randint
from time import time as timer

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

class Key(GameSprite):
    def update(self):
        pass

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Krest(GameSprite):
    def update(self):
        pass

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Lighter(GameSprite):
    def update(self):
        pass

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Zashigalka(GameSprite):
    def update(self):
        pass

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    
# Очки
score = 5000
score_click = 1
bot_click = 0
price_krest = {"krest": 20 }
price_lighter = {"lighter": 100 }
price_key = {"key": 300}
price_zashigalka = {"zashigalka": 5000}

# Текст
font.init()
font1 = font.SysFont('Arial', 45)

# Музыка
mixer.init()
mixer.music.load('Music_Doors.ogg')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Спрайты
button = Player("Button.png", 140, 260, 150, 150)
upgrades = Upgrade("Updates_list.png", 380, 10, 520, 520)
krest = Krest("Krest.jpg", 530, 90, 80, 230)
lighter = Lighter("Lighter.jpg", 530, 180, 80, 230)
key = Key("Key.jpg", 530, 270, 80, 230)
zashigalka = Zashigalka("Zashigalka.jpg", 530, 360, 80, 230)


# Цикл
start_time = timer()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button.collidepoint(x, y):
                score += score_click
            if krest.collidepoint(x, y):
                if score >= 10:
                    score_click += 1
                    score -= price_krest["krest"]
            if lighter.collidepoint(x, y):
                if score >= 100:
                    score_click += 10
                    score -= price_lighter["lighter"]
            if key.collidepoint(x, y):
                if score >= 300 and finish != True:
                    bot_click += 30
                    score -= price_key["key"]
            if zashigalka.collidepoint(x, y):
                if score >= 5000:
                    score -= price_zashigalka["zashigalka"]
                    window.blit(text_WIN, (300, 300))



    if finish != True:
        window.blit(bg, (0, 0))

        
        now_time = timer()
        if int(now_time) - int(start_time) == 3:
            score += bot_click
            start_time = now_time


        button.reset()
        upgrades.reset()
        key.reset()
        krest.reset()
        lighter.reset()
        zashigalka.reset()

        button.update()
        upgrades.update()
        key.update()
        krest.update()
        lighter.update()
        zashigalka.update()

        # ОТрисовка текст
        text_score = font1.render("Баллы: " + str(score), 1, (255, 255, 255))
        text_click = font1.render("За клик: " + str(score_click), 1, (255, 255, 255))
        text_bot_click = font1.render("За клик бота: " + str(bot_click), 1, (255, 255, 255))
        text_WIN = font1.render("YOU WIN!!!", (255, 255, 255))
        window.blit(text_score, (10, 20))
        window.blit(text_click, (10, 70))
        window.blit(text_bot_click, (10, 120))

        display.update()
    clock.tick(FPS)
