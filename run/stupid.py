# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:06:18 2022

@author: angel
"""
import pygame
import random

def wallss(wal,walls):
    if wal == 1:
        
        walls.append([800,100])
        walls.append([800,200])
        walls.append([800,300])
        walls.append([800,400])
        return walls
    
    if wal == 2:
        walls.append([800,0])
        
        walls.append([800,200])
        walls.append([800,300])
        walls.append([800,400])
        return walls
    
    if wal == 3:
        walls.append([800,0])
        walls.append([800,100])
   
        walls.append([800,300])
        walls.append([800,400])
        return walls
    
    if wal == 4:
        walls.append([800,0])
        walls.append([800,100])
        walls.append([800,200])
   
        walls.append([800,400])
        return walls
    
    if wal == 5:
        walls.append([800,0])
        walls.append([800,100])
        walls.append([800,200])
        walls.append([800,300])
        return walls
     
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
    player_x_pos = 250
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
                    to_y = -10
                    space = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    to_y = 0
                    space = False
            # 점프         
            if space == True:
                player_y_pos += to_y
            else :
                player_y_pos += 5
            
            # 플레이어 높이 제한    
            if player_y_pos <= 0:
                player_y_pos = 0
            
            # 벽 위치 정의
            if wall_time > 150:
                x = random.randint(1,6)
                wallss(x,walls)
                wall_time = 0
            
            walls = [ [w[0] - 5, w[1]] for w in walls if w[0] > 0]
            
            player_rect = player.get_rect()
            player_rect.left = player_x_pos
            player_rect.top = player_y_pos
            
            for wall_idx, wall_val in enumerate(walls):
                wall_pos_x = wall_val[0]
                wall_pos_y = wall_val[1]

                wall_rect = wall.get_rect()
                wall_rect.left = wall_pos_x
                wall_rect.top = wall_pos_y
                
                if wall_rect.colliderect(player_rect):
                    walls.pop(wall_idx)
                    
            for i in range(2):
                screen.blit(background,(0+(i*500),0))
                
            for wall_x_pos, wall_y_pos in walls:
                screen.blit(wall, (wall_x_pos, wall_y_pos))
                
            screen.blit(player,(250,player_y_pos))
            
            pygame.display.update()
            
    pygame.quit()
    
main()