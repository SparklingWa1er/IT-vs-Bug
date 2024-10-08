import pygame
import random
from config import *

class Bug:
    def __init__(self, x, y, speed, health, max_health):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.max_health = max_health
        self.slowed = False
        self.slow_timer = 0

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, MONSTER_SIZE, MONSTER_SIZE))

    def update(self):
        if self.slowed and pygame.time.get_ticks() > self.slow_timer:
            self.speed = 2
            self.slowed = False
        self.x -= self.speed

    def apply_slow(self):
        self.speed = 1
        self.slowed = True
        self.slow_timer = pygame.time.get_ticks() + 10000 
    

    def create_monster(monsters):
        monster_x = WIDTH
        monster_y = random.randint(0, HEIGHT - MONSTER_SIZE)
        monsters.append(Bug(monster_x, monster_y, 2, 100, 100))  # Tốc độ ban đầu của quái vật là 2, máu của quái vật là 100

    # Khởi tạo bộ đếm thời gian để tạo quái vật mới
    spawn_monster_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_monster_event, 1000)  # Tạo quái vật mới mỗi giây
    

    def draw_monster(x, y):
        pygame.draw.rect(screen, RED, (x, y, MONSTER_SIZE, MONSTER_SIZE))


    def apply_slow_effect(monsters):
        for monster in monsters:
            monster.apply_slow()


    def draw_health_bar(x, y, health, max_health):
        # Calculate health bar
        health_bar_length = MONSTER_SIZE
        health_bar_height = 5
        fill = (health / max_health) * health_bar_length
        outline_rect = pygame.Rect(x, y - 10, health_bar_length, health_bar_height)
        fill_rect = pygame.Rect(x, y - 10, fill, health_bar_height)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, BLACK, outline_rect, 1)
