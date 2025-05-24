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
score = 0
score_click = 1
bot_click = 0
price = {
    "krest": 20 ,
    "lighter": 200 ,
    "key": 1000,
    "zashigalka": 2000,
}
# Текст
font.init()
font1 = font.SysFont('Arial', 45)
font2 = font.SysFont('Arial', 23)

# Музыка
mixer.init()
mixer.music.load('Music_Doors.ogg')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Спрайты
button = Player("Button.png", 140, 260, 150, 150)
upgrades = Upgrade("Updates_list.png", 380, 10, 520, 520)
krest = Krest("Krest.jpg", 610, 90, 70, 200)
lighter = Lighter("Lighter.jpg", 610, 180, 70, 200)
key = Key("Key.jpg", 610, 270, 70, 200)
zashigalka = Zashigalka("Zashigalka.jpg", 610, 360, 70, 200)


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
                if score >= price['krest']:
                    score_click += 1
                    score -= price["krest"]
                    price["krest"] *= 2 
            if lighter.collidepoint(x, y):
                if score >= price['lighter']:
                    score_click += 10
                    score -= price["lighter"]
                    price["lighter"] *= 2 
            if key.collidepoint(x, y):
                if score >= price["key"] and finish != True:
                    bot_click += 50
                    score -= price["key"]
                    price["key"] += 500 
            if zashigalka.collidepoint(x, y):
                if score >= price["zashigalka"] and finish != True:
                    bot_click += 100
                    score -= price["zashigalka"]
                    price["zashigalka"] += 1000 

                    



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
        text_score_key_price = font2.render(f"Цена: {price['key']}", 1, (0, 0, 0))
        text_score_key_value = font2.render("+50 к клику бота", True, (0, 0, 0))
        text_score_krest_price = font2.render(f"Цена: {price['krest']}", 1, (0, 0, 0))
        text_score_krest_value = font2.render("+1 к клику", True, (0, 0, 0))
        text_score_lighter_price = font2.render(f"Цена: {price['lighter']}", 1, (0, 0, 0))
        text_score_lighter_value = font2.render("+10 к клику", True, (0, 0, 0))
        text_score_zashigalka_price = font2.render(f"Цена: {price['zashigalka']}", 1, (0, 0, 0))
        text_score_zashigalka_value = font2.render("+100 к клику бота", True, (0, 0, 0))
        window.blit(text_score, (10, 20))
        window.blit(text_click, (10, 70))
        window.blit(text_bot_click, (10, 120))
        window.blit(text_score_krest_price, (475, 100))
        window.blit(text_score_krest_value, (475, 125))
        window.blit(text_score_lighter_price, (475, 190))
        window.blit(text_score_lighter_value, (475, 215))
        window.blit(text_score_key_price, (465, 280))
        window.blit(text_score_key_value, (465, 305))
        window.blit(text_score_zashigalka_price, (460, 370))
        window.blit(text_score_zashigalka_value, (460, 395))

        display.update()
    clock.tick(FPS)
