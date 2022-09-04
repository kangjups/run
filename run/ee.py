# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:06:18 2022

@author: angel
"""

import pygame
import random

class wallc:
    def __init__(self,img,img2,hp):
        self.wall =  pygame.image.load(img)
        self.star = pygame.image.load(img2)
        self.ab = self.wall
        self.hp = hp
        self.walls = []
        self.speed = 5
        self.start = 800
        self.gap = 100
        self.size = self.wall.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.wall_time = 0
        self.stage_choice = 1
        
    def create(self):
        if self.stage_choice == 1:
            self.wall = self.ab 
            wal = random.randint(1,4)
            if wal == 1:
                self.walls.append([self.start,0])
                self.walls.append([self.start,100])
                self.walls.append([self.start,200])
            if wal == 2:
                self.walls.append([self.start,0])
                self.walls.append([self.start,100])
                self.walls.append([self.start,400])
            if wal == 3:
                self.walls.append([self.start,0])
                self.walls.append([self.start,300])
                self.walls.append([self.start,400])
            if wal == 4:
                self.walls.append([self.start,200])
                self.walls.append([self.start,300])
                self.walls.append([self.start,400])
                
        if self.stage_choice == 2:
            wal = random.randint(1,5)
            if wal == 1:
                self.walls.append([self.start,100])
                self.walls.append([self.start,200])
                self.walls.append([self.start,300])
                self.walls.append([self.start,400])
            if wal == 2:
                self.walls.append([self.start,0])
                self.walls.append([self.start,200])
                self.walls.append([self.start,300])
                self.walls.append([self.start,400])
            if wal == 3:
                self.walls.append([self.start,0])
                self.walls.append([self.start,100])
                self.walls.append([self.start,300])
                self.walls.append([self.start,400])
            if wal == 4:
                self.walls.append([self.start,0])
                self.walls.append([self.start,100])
                self.walls.append([self.start,200])
                self.walls.append([self.start,400])
            if wal == 5:
                self.walls.append([self.start,0])
                self.walls.append([self.start,100])
                self.walls.append([self.start,200])
                self.walls.append([self.start,300])
                
        if self.stage_choice == 3:
            self.wal = self.star
            wal = random.randint(1,2)
            if wal == 1:
                self.walls.append([self.start,0])
                self.walls.append([self.start,100]) 
                self.walls.append([self.start,400])
            if wal == 2:
                self.walls.append([self.start,0])
                self.walls.append([self.start,300])
                self.walls.append([self.start,400])
        
    def move(self, speed):
        self.speed = speed
        self.walls = [ [w[0] - self.speed, w[1]] for w in self.walls if w[0] > 0] # 벽을 왼쪽으로 이동
    def move(self):
        self.walls = [ [w[0] - self.speed, w[1]] for w in self.walls if w[0] > 0] # 벽을 왼쪽으로 이동
        
    def collision(self, player_rect):
        for wall_idx, wall_val in enumerate(self.walls):
            wall_pos_x = wall_val[0]
            wall_pos_y = wall_val[1]

            wall_rect = self.wall.get_rect()
            wall_rect.left = wall_pos_x
            wall_rect.top = wall_pos_y
            
            # 벽과 플레이어의 충돌
            if wall_rect.colliderect(player_rect):
                self.walls.pop(wall_idx)
                self.hp -= random.randint(18,28)
            
    def set_speed(self,s):
        self.speed = s
                
    def display(self, screen):
        if self.stage_choice == 3:
            self.wall = self.star
        else :
            self.wall = self.ab
        for wall_x_pos, wall_y_pos in self.walls:
            screen.blit(self.wall, (wall_x_pos, wall_y_pos))
            
# 메인 함수
 
def main(hp):
    # 파이게임 기본 정의
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("run")
    
    # 바탕하면
    background = pygame.image.load("wall_red.png")
    background_sound = pygame.mixer.Sound("rpg.mp3")
    background_sound.play(-1)
    
    # 플레이어 
    player = pygame.image.load("player.png")
    player_size = player.get_rect().size
    player_width = player_size[0]
    player_height = player_size[1]
    player_x_pos = 150
    player_y_pos = 100
    to_y = 0
    
    # 점프
    space = False
    space_sound = pygame.mixer.Sound("jump.wav")
    space_sound.set_volume(0.4)
    
    # 문
    door = pygame.image.load("door.png")
    door_x = 150
    
    # 벽
    wall =  wallc("wall.png","wall_star.png",hp)
    
    # 점수
    font = pygame.font.SysFont("malgungothic",30)
    p = 0
    point = font.render("점수:" + str(p),True,(255,255,255))
    
    # 하트
    heart = pygame.image.load("heart.png")
    heart_x = 17
    heart_point = font.render(str(hp),True,(255,255,255))
    heart_time = 0
    
    # 스테이지
    stage = 0
    stage_choice = 1
    
    clock = pygame.time.Clock() 
    running = True
    while running:
        clock.tick(60)
        wall.wall_time += 1 
        heart_time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_sound.play()
                    to_y = - 5
                    space = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    to_y = 0
                    space = False
            
        # 플레이어 충돌 정의
        player_rect = player.get_rect()
        player_rect.left = player_x_pos
        player_rect.top = player_y_pos
            
        # 점프         
        if space == True:
            player = pygame.image.load("player_up.png")
            player_y_pos += to_y
        else :
            player = pygame.image.load("player.png")
            player_y_pos += 3
            
        # 플레이어 높이 제한    
        if player_y_pos <= 0:
            player_y_pos = 0
        
        if player_y_pos >= 500:
            running = False             
            
        # 벽 위치 정의
        if wall.wall_time > 150:
            p += 1
            stage += 1
            if stage == 3:
                wall.stage_choice += 1
                stage = 0
                if wall.stage_choice >= 4:
                    wall.stage_choice = 1
            wall.create()
            wall.wall_time = 0
        
        # 벽 움직임 , 벽 충돌 
        wall.move()
        wall.collision(player_rect)
        
        # 문 위치 변화
        door_x -= 2
                
        # 점수 그리고 hp
        point = font.render("점수 :" + str(p),True,(255,255,255))
        heart_point = font.render(str(wall.hp),True,(255,255,255))
        
        # hp 값에 따른 위치 변화
        if heart_time >= 50:
            wall.hp -= 1
            if wall.hp <= 99:
                heart_x = 30
            if wall.hp  <= 9:
                heart_x = 38
            heart_time = 0
        if wall.hp <= 0:
            running = False  
        
        # 이미지 그리기
        for i in range(2):
            screen.blit(background,(0+(i*500),0))
            
        wall.display(screen)
        
        if door_x >= -30:
            screen.blit(door,(door_x,100)) 
            
        screen.blit(point,(750,10)) 
        screen.blit(heart,(15,10))
        screen.blit(heart_point,(heart_x,24))
        screen.blit(player,(player_x_pos,player_y_pos))
        
        pygame.display.update()
            
    pygame.quit()
    return p 

def run_menu(p):
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("run_menu")
    background = pygame.image.load("wall_red.png")
    
    font = pygame.font.SysFont("malgungothic",50)
    point = font.render("점수:" + str(p),True,(255,255,255))
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    return False
            
        for i in range(2):
            screen.blit(background,(0+(i*500),0))
        screen.blit(point,(800,10))
        pygame.display.update()
         
    pygame.quit()
    
h = 100
r_running = True
while r_running:
    p = main(h)
    r_running = run_menu(p)
