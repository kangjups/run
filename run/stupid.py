# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:06:18 2022

@author: angel
"""

import pygame
import random

#trees = ["tree.png",5,30,400]
#walls = ["wall.png",5,30,100]

# 이미지, 속도, 데미지, 위치

#stage1 = [trees ]

class wallc:
    def __init__(self,hp):
        #self.img = pygame.image.load(img)
        self.hp = hp
        self.walls = []
        self.trees =  ["tree.png",5,30,300]
        self.bird = ["bird.png",7,10,0]
        self.bird1 = ["bird.png",7,10,100]
        self.bird2 = ["bird.png",7,10,200]
        self.bird3 = ["bird.png",7,10,300]
        self.stage = [self.bird,self.bird1,self.bird3,self.trees,self.bird2,self.trees,self.trees]
        self.start = 800
        self.gap = 100
        self.wall_time = True
        self.i = 0
        
    def create(self):
        
        self.i += 1
        if self.i >= len(self.stage):
            self.i = 0
            self.wall_time = False
        self.img =  pygame.image.load(self.stage[self.i][0])
        self.speed = self.stage[self.i][1]
        
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        
        self.walls.append([self.start,self.stage[self.i][3]])

    
    def move(self):
        self.walls = [ [w[0] - self.speed, w[1]] for w in self.walls if w[0] > 0] # 벽을 왼쪽으로 이동
                
        
    def collision(self, arrow_rect):
        for self.img_idx, self.img_val in enumerate(self.walls):
            self.img_pos_x = self.img_val[0]
            self.img_pos_y = self.img_val[1]

            self.img_rect = self.img.get_rect()
            self.img_rect.left = self.img_pos_x
            self.img_rect.top = self.img_pos_y
            
            # 벽과 플레이어의 충돌
            if self.img_rect.colliderect(arrow_rect):
                self.walls.pop(self.img_idx)
                self.hp -= self.stage[self.i][2]
                
    def check(self):
        return len(self.walls)
           
    def display(self, screen):
            
        for self.img_x_pos, self.img_y_pos in self.walls:
            screen.blit(self.img, (self.img_x_pos, self.img_y_pos))
def window():
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("school")
    background = pygame.image.load("school.png")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    return True
                    
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x_p, y_p = pygame.mouse.get_pos()    
                    if x_p > 400 and x_p < 600 and y_p > 200 and y_p < 250:
                        running = False
                    if x_p > 400 and x_p < 600 and y_p > 300 and y_p < 350:
                        print("setting")
                    if x_p > 400 and x_p < 600 and y_p > 400 and y_p < 450:
                        running = False
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
        screen.blit(background,(0,0))
        pygame.display.update()
         
    pygame.quit()
    if x_p > 400 and x_p < 600 and y_p > 200 and y_p < 250:
        return True  
    if x_p > 400 and x_p < 600 and y_p > 400 and y_p < 450:
        return False         
# 메인 함수
def main_0(hp):
    # 파이게임 기본 정의
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("run")
    
    # 바탕하면
    background = pygame.image.load("background_t.png")
    background_sound = pygame.mixer.Sound("rpg.mp3")
    background_sound.play(-1)
    
    #arrow
    arrow = pygame.image.load("arrow.png")
    arrow_size = arrow.get_rect().size
    arrow_width = arrow_size[0]
    arrow_height = arrow_size[1]
    arrow_y_pos = 290 
    to_y = 0
    
    # 사냥꾼
    player = pygame.image.load("player_main.png")
    
    # 박스
    box = pygame.image.load("box.png")
    
    # 화살 세기 정하기
    rulet = pygame.image.load("rulet.png")
    rulet_ = pygame.image.load("rulet_.png")
    rulet_x = 40
    rul = True    
    rulet_x_to = 5 
    
    # 점프
    space = True
    space_sound = pygame.mixer.Sound("jump.wav")
    space_sound.set_volume(0.4)
     
    # 벽
    wall =  wallc(hp)
    wall_list = []
    
    # 점수
    font = pygame.font.SysFont("malgungothic",30)
    p = 0
    point = font.render("점수:" + str(p),True,(255,255,255))
    
    # 하트
    heart = pygame.image.load("heart.png")
    heart_x = 17
    heart_point = font.render(str(hp),True,(255,255,255))
    heart_time = 0
    
    clock = pygame.time.Clock() 
    running = True
    
    while running:
        clock.tick(60)
        #wall.wall_time += 1 
        heart_time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE and rul == True:
                    rul = False
                    if rulet_x >= 112 and rulet_x <= 120:
                        wall.hp += 10
                    if rulet_x >= 58 and rulet_x <= 75 or rulet_x >= 135 and rulet_x <= 150:
                        wall.hp -= 10
                if event.key == pygame.K_SPACE and rul == False:
                    space_sound.play()
                    to_y = - 5
                    space = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    to_y = 0
                    space = False
            
        # 플레이어 충돌 정의
        arrow_rect = arrow.get_rect()
        arrow_rect.left = 160
        arrow_rect.top = arrow_y_pos
            
        # 점프         
        if space == True:
            arrow_y_pos += to_y
        else :
            arrow_y_pos += 3
            
        # 플레이어 높이 제한    
        if arrow_y_pos <= 0:
            arrow_y_pos = 0
        
        if arrow_y_pos >= 470:
            arrow_y_pos = 470
            running = False             
    
        if rul == True :
            rulet_x += rulet_x_to
            if rulet_x >= 190 :
                rulet_x_to = -5
            if rulet_x <= 50:
                rulet_x_to = 5

                
        # 벽 위치 정의 ------------------- 벽 위치 정의
        
        if wall.wall_time == True and rul == False:
            p += 1
            #wall =  wallc(hp)
            wall.create()
            wall_list.append(wall)
            wall.wall_time = False
            
         #벽 움직임 , 벽 충돌 
        for w in wall_list :
            w.move()
            w.collision(arrow_rect)
            if w.check() == 0 :
                wall_list.remove(w)
                wall.wall_time = True
               
        # 점수 그리고 hp
        point = font.render("점수 :" + str(p),True,(255,255,255))
        heart_point = font.render(str(wall.hp),True,(255,255,255))
        
        # hp 값에 따른 위치 변화
        if heart_time >= 50 and rul == False:
            wall.hp -= 1
            hp = wall.hp
            if wall.hp <= 99:
                heart_x = 30
            if wall.hp  <= 9:
                heart_x = 38
            heart_time = 0
            
        if wall.hp <= 0:
            running = False  

        # 이미지 그리기
        screen.blit(background,(0,0))
            
        wall.display(screen) 
        screen.blit(point,(750,10)) 
        screen.blit(heart,(15,10))
        screen.blit(heart_point,(heart_x,24))
        
        if rul == True:
            for i in range(3):
                for a in range(3-i):
                    screen.blit(box,(a*50+50*i, 450 - i*50))
        
            screen.blit(rulet,(50,240))
            screen.blit(rulet_,(rulet_x,256))
            screen.blit(player,(110,280))
        if rul == False:    
            screen.blit(arrow,(160,arrow_y_pos))
        pygame.display.update()
            
    pygame.quit()
    return p 

def main_1(h):
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("s")
    background = pygame.image.load("background_s.png")
    bird = pygame.image.load("bird.png")
    p = 13
    x = 100
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        #x += 1
        screen.blit(background,(0,0))
        screen.blit(bird,(x,100))
        pygame.display.update()
         
    pygame.quit()
    return p 

def englishs():
  korea = ["이의를 제기하다","소중한","채택하다","평가","경영진","분리된","결속되어 있는","관점","사고방식","위태롭게 하다","결정하다","특성","발전시키다"]
  english = ["challenge","valuable","adopt","assessment","management","disassociated","bonded","perspective","mentality","risk","determine","characteristic","advance"]
      
  while True:
      x = random.randint(0,len(korea)-1)
      y = input(korea[x])
      if y == english[x]:
          del korea[x]
          del english[x]
      else :
          print(korea[x],":",english[x])
          
      if len(korea) == 0:
          break
      if y == 'break':
          break
      
def menu(p):
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("menu")
    background = pygame.image.load("background_menu.png")
    xs = [0,1,2]
    x = 0
    font = pygame.font.SysFont("malgungothic",50)
    point = font.render("점수:" + str(p),True,(255,255,255))
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False ,x
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    return True ,x
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x_p, y_p = pygame.mouse.get_pos()    
                    if x_p > 50 and x_p < 120 and y_p > 290 and y_p < 390:
                        x -= 1
                        x = xs[x]
                    if x_p > 330 and x_p < 400 and y_p > 290 and y_p < 390:
                        x += 1
                        if x >= 3:
                            x = 0
                        x = xs[x]
                    if x_p > 190 and x_p < 260 and y_p > 290 and y_p < 390:
                        pygame.quit()
                        return True ,x
                    #if x_p > 850 and x_p < 950 and y_p > 400 and y_p < 500:
                     #   pygame.quit()
                      #  return False ,x
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if x == 0:
            card = pygame.image.load("card_t.png")
        if x == 1:
            card = pygame.image.load("card_s.png")
        if x == 2:
            card = pygame.image.load("card_e.png")
            
        screen.blit(background,(0,0))
        screen.blit(card,(50,40))
        screen.blit(point,(800,10))
        pygame.display.update()
         
    pygame.quit()
    
running = window()
h = 100
p = 0
while running:
    running ,x = menu(p)
    print(x)
    if running == False:
        break
    if x == 0:
        p = main_0(h)
    if x == 1:
        p = main_1(h)
    if x == 2:
        englishs()
        
        
        