from pygame import *
mixer.init()

win = display.set_mode((700, 700))
win.fill((30, 235, 197))

game = True
finish = False
clock = time.Clock()
fps = 50
mixer.music.load('zabivnaya_music.mp3')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, image_p, x, y, speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(image_p), (wight, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed

racket1 = Player('seal.png', 30, 50, 5, 100, 100)
racket2 = Player('seal.png', 570, 50, 5, 100, 100)
ball = GameSprite('ball.png', 250, 250, 3, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True:
            win.fill((30, 235, 197))
            racket1.update_l()
            racket2.update_r()
            racket1.reset()
            racket2.reset()
            ball.reset()
        display.update()
        clock.tick(fps)