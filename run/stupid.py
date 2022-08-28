# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:06:18 2022

@author: angel
"""
import pygame
import random

class wallc:
    def __init__(self,img,walls):
        self.img =  pygame.image.load(img)
        self.walls = walls
    def wall_make(self):
        self.walls.append([0,0])
def wallss(wal,walls):
    #벽 4
    if wal == 1:
        
        walls.append([800,100])
        walls.append([800,200])
        walls.append([800,300])
        walls.append([800,400])
    
    if wal == 2:
        walls.append([800,0])
        
        walls.append([800,200])
        walls.append([800,300])
        walls.append([800,400])

    if wal == 3:
        walls.append([800,0])
        walls.append([800,100])
   
        walls.append([800,300])
        walls.append([800,400])
    
    if wal == 4:
        walls.append([800,0])
        walls.append([800,100])
        walls.append([800,200])
   
        walls.append([800,400])
    
    if wal == 5:
        walls.append([800,0])
        walls.append([800,100])
        walls.append([800,200])
        walls.append([800,300])
 
    # 벽 3 
    if wal == 6:
        walls.append([800,0])
        walls.append([800,100])
        walls.append([800,200])
        
    
    if wal == 7:
        walls.append([800,0])
        walls.append([800,100])
        
        
        walls.append([800,400])

    if wal == 8:
        walls.append([800,0])
        
        
        walls.append([800,300])
        walls.append([800,400])
    
    if wal == 9:
        
        
        walls.append([800,200])
        walls.append([800,300])
        walls.append([800,400])
# 메인 함수
def main():
    # 파이게임 기본 정의
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("run")
    
    # 바탕하면
    background = pygame.image.load("background.png")
    
    # 플레이어 
    player = pygame.image.load("player.png")
    player_size = player.get_rect().size
    player_width = player_size[0]
    player_height = player_size[1]
    player_x_pos = 150
    player_y_pos = 300
    to_y = 0
     
    space = False
    
    # 벽
    wall =  pygame.image.load("wall.png")
    wall_size = wall.get_rect().size
    wall_width = wall_size[0]
    wall_height = wall_size[1]
    walls = []
    wall_time = 0
    x = random.randint(1,6)
    wallss(x,walls)
    
    # 점수
    font = pygame.font.SysFont("malgungothic",50)
    p = 0
    point = font.render("점수:" + str(p),True,(255,255,255))
    
    clock = pygame.time.Clock() 
    running = True
    while running:
        clock.tick(60)
        wall_time += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
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
            player_y_pos += to_y
        else :
            player_y_pos += 3 
            
        # 플레이어 높이 제한    
        if player_y_pos <= 0:
            player_y_pos = 0
        
        if player_y_pos >= 500:
            print("게임오버")
            running = False             
            
        # 벽 위치 정의
        if wall_time > 150:
            x = random.randint(1,9)
            wallss(x,walls)
            p += 1
            point = font.render("점수 :" + str(p),True,(255,255,255))
            wall_time = 0
            
        walls = [ [w[0] - 5, w[1]] for w in walls if w[0] > 0] # 벽을 왼쪽으로 이동
        
        # 벽의 충돌 정의 
        for wall_idx, wall_val in enumerate(walls):
            wall_pos_x = wall_val[0]
            wall_pos_y = wall_val[1]

            wall_rect = wall.get_rect()
            wall_rect.left = wall_pos_x
            wall_rect.top = wall_pos_y
            
            # 벽과 플레이어의 충돌
            if wall_rect.colliderect(player_rect):
                walls.pop(wall_idx)
                print("게임 오버23")
                
        for i in range(2):
            screen.blit(background,(0+(i*500),0))
            
        for wall_x_pos, wall_y_pos in walls:
            screen.blit(wall, (wall_x_pos, wall_y_pos))
        
        screen.blit(point,(800,10))
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
    background = pygame.image.load("background.png")
    
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
    
r_running = True
while r_running:
    p = main()
    r_running = run_menu(p)    
    
    
    
    
    
    
    