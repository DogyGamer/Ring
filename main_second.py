# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import numpy as np
from math import *


WIDTH = 800
HEIGHT = 800
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GrAY = (248,248,248)
GOLD =(218,165,32)
blevotnya = (143, 254, 9)
green_dark = (20,100,30)
# Создаем игру и окно

iter = 0
last_iter = -1

r = (HEIGHT//2)-37
center = np.array([(HEIGHT-20)//2, (HEIGHT-20)//2])

class pg_city(pygame.sprite.Sprite):
    def __init__(self, money, id, center, next_id, prev_id):
        self.money = money
        self.id = id
        self.next_id = next_id
        self.prev_id = prev_id
        self.picked = False

        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 35)
        self.textSurf = self.font.render(str(id), 2, GOLD)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.image.blit(self.textSurf, [50/2 - W/2, 50/2 - H/2])
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()

        if(self.picked):
            self.image.fill(GREEN)
            self.image.blit(self.textSurf, [50/2 - W/2, 50/2 - H/2])
        else:
            self.image.fill(BLUE)
            self.image.blit(self.textSurf, [50/2 - W/2, 50/2 - H/2])

class cirlce(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((HEIGHT-20, HEIGHT-20))
        self.image.fill(GrAY)
        self.circle = pygame.draw.circle(self.image, green_dark, center, r, 12)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

class main_text(pygame.sprite.Sprite):
    def __init__(self, size_x, size_y, x,y):
        self.text = ""
        self.size_x = size_x
        self.size_y = size_y

        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 35)
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill(GrAY)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        self.image.fill(GrAY)
        self.textSurf = self.font.render(self.text, 2, GOLD)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.size_x/2 - W/2, self.size_y/2 - H/2])

n = int(input("сколько городов: "))
l = int(input("скильки гривень: "))
k = int(input("сколько ходов: "))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ring")
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
circle_ = cirlce()
text = main_text(400, 60, WIDTH/2, HEIGHT/3)
sprites.add(circle_, text)

ang = 360 / n
angle = 0
cities = []


for i in range(n):
    if i+2 > n:
        next_id = 0
    else:
        next_id = i+1

    centre = np.array([r*cos(np.deg2rad(angle)), r*sin(np.deg2rad(angle))]) + np.array([WIDTH//2, HEIGHT//2])

    cities.append(pg_city(id=i, center=centre, money=l, next_id=next_id, prev_id=i-1))
    sprites.add(cities[i])
    angle += ang

# Цикл игры
running = True
current = 0
previous = -1
while running:
    # Держим цикл на правильной скорости
    clock.tick(1)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    text.text = "Ход игрока: "+str(current) 
    cities[current].picked = True
    cities[previous].picked = False
    previous = current
    current = cities[current].next_id

    sprites.update()
    # Рендеринг
    screen.fill(GrAY)
    sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()