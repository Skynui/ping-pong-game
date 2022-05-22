from pygame import *
import random
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < w_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < w_width - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
w_width = 1540
w_height = 800
window = display.set_mode((w_width, w_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('img/spr1.png', 30, 400, 50, 150, 4)
racket2 = Player('img/spr2.png', 1460, 400, 50, 150, 4)
ball = GameSprite('img/spr3.png', (w_width/2), (w_height/2), 50, 50, 4)

font.init()
font = font.Font(None, 35)
lose1_1 = font.render('ИГРОК 1 - LOX!', True, (180, 0, 0))
lose2_1 = font.render('ИГРОК 2 - LOX!', True, (180, 0, 0))
lose1_2 = font.render('ИГРОК 1 - LOX-O-PEDRO!', True, (180, 0, 0))
lose2_2 = font.render('ИГРОК 2 - LOX-O-PEDRO!', True, (180, 0, 0))
lose1_3 = font.render('ЛОХ 1 - ЛОХ!', True, (180, 0, 0))
lose2_3 = font.render('ЛОХ 2 - ЛОХ!', True, (180, 0, 0))

lose1 = [lose1_1, lose1_2, lose1_3]
lose2 = [lose2_1, lose2_2, lose2_3]

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish !=True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > w_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(random.choice(lose1), (700, 400))
            game_over = True

        if ball.rect.x > w_width:
            finish = True
            window.blit(random.choice(lose2), (700, 400))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)