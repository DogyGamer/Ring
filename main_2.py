import math
import numpy as np
import pygame

WIDTH = 1024
HEIGHT = 768
FPS = 30
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# running = True


n = int(input("сколько городов: "))
l = int(input("скильки гривень: "))
k = int(input("сколько ходов: "))

class player(): #один класс не пидорас
    def __init__(self, money, id, next_id, prev_id): #кто изменит на l тот пидор
        self.money = money
        self.id = id
        self.next_id = next_id
        self.prev_id = prev_id
        print("city #"+str(id)+" money: "+str(money)+" next: "+str(next_id)+" prev: "+str(prev_id))

players = {}
for i in range(n):
    if i+2 > n:
        next_id = 0
    else:
        next_id = i+1
    players[i] = player(l, i, next_id, i-1)
