# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import numpy as np
from math import *


WIDTH = 1100
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
center = np.array([(HEIGHT-20)//2, (HEIGHT-20)//2])
r = (HEIGHT//2)-37

class pg_city(pygame.sprite.Sprite):
    def __init__(self, money, id, center, next_id, prev_id, is_last=False):
        self.money = money
        self.points = 0
        self.money_tospend = 0
        self.attack = 0
        self.defence = 0
        self.id = id
        self.next_id = next_id
        self.prev_id = prev_id
        self.is_last = is_last 
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
text = main_text(500, 60, WIDTH/2, HEIGHT/3)
text_goal = main_text(500,60, WIDTH/2, HEIGHT/3+60)
sprites.add(circle_, text, text_goal)

ang = 360 / n
angle = 0
cities = []

for i in range(n):
    if i+2 > n:
        next_id = 0
        is_last = True
    else:
        next_id = i+1
        is_last = False

    centre = np.array([r*cos(np.deg2rad(angle)), r*sin(np.deg2rad(angle))]) + np.array([WIDTH//2, HEIGHT//2])

    cities.append(pg_city(id=i, center=centre, money=l, next_id=next_id, prev_id=i-1, is_last=is_last))
    sprites.add(cities[i])
    angle += ang

cities[0].picked = True
for city in cities:
    print("id:",city.id, "last:", city.is_last)

def pg_update():
    sprites.update()
    screen.fill(GrAY)
    sprites.draw(screen)
    pygame.display.flip()
# Цикл игры
running = True
cyber_move = 1
current = 0
previous = -1


while running:
    # Держим цикл на правильной скорости
    clock.tick(30)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pg_update()
    if cyber_move-1 != k*2:
        text.text = "Ход игрока: "+str(current)+" ход: "+str(cyber_move//2) 
        if cyber_move % 2 != 0: text_goal.text = "Определение бюджета"
        else: text_goal.text = "Распределение бюджета"
        cities[current].picked = True
        cities[previous].picked = False
        pg_update()

        if cyber_move % 2 != 0:
            money = int(input("Игрок "+str(current)+" расходы на "+str(cyber_move//2)+" раунд("+str(cities[current].money)+"):"))
            if(cities[current].money < money):
                cities[current].money_tospend = 0
            else:
                cities[current].money_tospend = money
                cities[current].money -= money
    
        else:
            deff = int(input("Игрок "+str(current)+" в оборону("+str(cities[current].money_tospend)+"):"))
            atk =  int(input("Игрок "+str(current)+" в атаку("+str(cities[current].money_tospend-deff)+"):"))
            if(cities[current].money_tospend < deff+atk):
                cities[current].money += cities[current].money_tospend
                cities[current].money_tospend = 0
                cities[current].defence += 0
                cities[current].attack += 0
            else:
                cities[current].defence += deff
                cities[current].attack += atk
        
        previous = current
        current = cities[current].next_id

        if current == 0:
            if cyber_move % 2 ==0:
                for id in range(len(cities)):
                    prev = cities[id].prev_id
                    next = cities[id].next_id

                    diff_atk = cities[id].attack - cities[next].defence
                    if diff_atk > 0: cities[id].attack = diff_atk
                    else:
                        cities[id].attack = 0
                        diff_atk = 0
                    diff_def = cities[id].defence - cities[prev].attack
                    if diff_def > 0:
                        cities[id].defence = diff_def
                        diff_def = 0
                    else: cities[id].defence = 0

                    cities[id].points += diff_atk + diff_def
                    print("Город", id, "защищается от", prev, cities[prev].attack, "-", cities[id].defence, "=", diff_def)
                    print("Город", id, "нападает на", next, cities[id].attack, "-", cities[next].defence, "=", diff_atk)
            cyber_move += 1
    else:
        text.text = "Ходы закончились"

    pg_update()

pygame.quit()