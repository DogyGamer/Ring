# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import numpy as np
from math import *


WIDTH = 800
HEIGHT = 800
FPS = 30

deg2rad = pi/180

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GrAY = (104,104,104)
blevotnya = (143, 254, 9)
green_dark = (20,100,30)

# Создаем игру и окно

r = (HEIGHT//2)-37
center = np.array([(HEIGHT-20)//2, (HEIGHT-20)//2])

class pg_city(pygame.sprite.Sprite):
    def __init__(self, id, center):
        self.id = id
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = center

class cirlce(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((HEIGHT-20, HEIGHT-20))
        self.image.fill(GrAY)
        self.circle = pygame.draw.circle(self.image, green_dark, center, r, 12)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ring")
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
circle_ = cirlce()
sprites.add(circle_)

n = int(input())
ang = 360 / n
angle = 0
cities = {}
print("ang", ang)
for i in range(n):
    centre = np.array([r*cos(np.deg2rad(angle)), r*sin(np.deg2rad(angle))]) + np.array([WIDTH//2, HEIGHT//2])
    cities[i] = pg_city(i, centre)
    sprites.add(cities[i])
    print("angle", angle)
    angle += ang

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    sprites.update()
    # Рендеринг
    screen.fill(GrAY)
    sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()