# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:06:18 2022

@author: angel
"""

import pygame
import random

#trees = ["tree.png",5,30,400]
#walls = ["wall.png",5,30,100]

# 이미지0, 속도1, 데미지2, 개수3, 위치4

#stage1 = [trees ]

class wallc:
    def __init__(self,hp):
        #self.img = pygame.image.load(img)
        self.hp = hp
        self.walls = []
        self.start = 850
        self.p = 0
        self.trees =  ["tree.png",5,30,1,300]
        
        self.bird = ["bird.png",7,10,1,0]
        self.bird1 = ["bird.png",7,10,1,100]
        self.bird2 = ["bird.png",7,10,1,200]
        self.bird3 = ["bird.png",7,10,1,300]
        self.bird4 = ["bird.png",7,10,1,400]
        self.bird134 = ["bird.png",7,10,3,100,300,400]
        self.bird124 = ["bird.png",7,10,3,100,200,400]
        
        
        self.stage = [self.bird,self.bird1,self.bird3,self.trees,self.bird2,self.trees,self.trees]
        self.stage2 = [self.trees,self.trees,self.trees]
        self.stage3 = [self.bird134,self.bird124]
        
        self.i = 0
        self.stage_choice = 0
    
        self.stages = [self.stage,self.stage2,self.stage3]
        self.stage = self.stages[self.stage_choice]
        #self.gap = 100
        self.wall_time = True
        
    def create(self):
        
        self.img =  pygame.image.load(self.stage[self.i][0])
        self.speed = self.stage[self.i][1] 
        self.damge = self.stage[self.i][2]
        self.number = self.stage[self.i][3]
    
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        
        # 스테이지의 리스트가 없을 때 스테이지 멈추기
        if not (self.stage_choice >= len(self.stages)-1):
            for a in range(0,self.number):
                self.walls.append([self.start,self.stage[self.i][4+a]])
            self.i += 1
            self.p += 1
            if self.i >= len(self.stage):
                self.i = 0
                self.stage_choice += 1
                self.stage = self.stages[self.stage_choice] 
                
    #def check2(self):
     #   if self.stage_choice >= len(self.stages)-1:
      #      return False
        
    def move(self):
        self.walls = [ [w[0] - self.speed, w[1]] for w in self.walls if w[0] > 0] # 벽을 왼쪽으로 
            
        
        
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
                self.hp -= self.damge
                
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
def main0(hp):
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
    point = font.render("점수 : " + str(wall.p),True,(255,255,255))
    stage_point = font.render("스테이지 : " + str(wall.stage_choice),True,(255,255,255))
    
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
            #wall =  wallc(hp)
            wall.create()
            #if wall.check2() == False:
             #   running = False
        
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
        point = font.render("점수 : " + str(wall.p),True,(255,255,255))
        heart_point = font.render(str(wall.hp),True,(255,255,255))
        stage_point = font.render("스테이지 : " + str(wall.stage_choice),True,(255,255,255))
        
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
        #if wall.create() == 1:
         #   running = False
        # 이미지 그리기
        screen.blit(background,(0,0))
            
        wall.display(screen) 
        screen.blit(point,(850,10)) 
        screen.blit(heart,(15,10))
        screen.blit(heart_point,(heart_x,24))
        screen.blit(stage_point,(650,10))
        
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
    
    pygame.time.delay(2000)        
    pygame.quit()
    return wall.p, wall.stage_choice 

def main1(h):
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

def main2():
  pygame.init()
  screen_width = 480
  screen_height = 640
  screen = pygame.display.set_mode((screen_width,screen_height))

  clock = pygame.time.Clock()

  background = pygame.image.load('ojuu.png') # 배경화면
  character = pygame.image.load('oju.png') # 캐릭터
  box = pygame.image.load('box_.png') # 적
  speed_box = pygame.image.load('speed_box.png')
  big_box =  pygame.image.load('big_box.png')
  end = pygame.image.load('eend.png') # 글자

  # 글자
  end_size = end.get_rect().size
  end_width = end_size[0]
  end_height = end_size[1]

  # 캐릭터
  character_size = character.get_rect().size
  character_width = character_size[0]
  character_height = character_size[1]
  character_x_pos = (screen_width/2) - (character_width/2) 
  character_y_pos = screen_height - character_height  - 150
  to_x = 0
  to_y = 0

  # 행성 박스
  box_size = box.get_rect().size
  box_widht = box_size[0]
  box_height = box_size[1]
  box_x_pos = random.randint(0,(screen_width - box_widht))
  box_y_pos = 0

  # speed 행성 박스
  speed_box_size = speed_box.get_rect().size
  speed_box_widht = speed_box_size[0]
  speed_box_height = speed_box_size[1]
  speed_box_x_pos = random.randint(0,(screen_width - box_widht))
  speed_box_y_pos = 0 

  # big 행성 박스 
  big_box_size = big_box.get_rect().size
  big_box_widht = big_box_size[0]
  big_box_height = big_box_size[1]
  big_box_x_pos = random.randint(0,(screen_width - box_widht))
  big_box_y_pos = 0 
  
  
  character_speed = 6
  box_speed = 3
  d = 0
  jumsu = 0
  a = 1
  aa = 0
  b = 1
  bb = 0
  c = 1
  cc = 0
  # 시간 
  game_font = pygame.font.Font(None, 40)
  total_time = 0
  start_ticks = pygame.time.get_ticks()
  
  # 루프 and 키 입력에 따른 움직임
  running = True
  while running :
    dt = clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
          to_x += character_speed
        if event.key == pygame.K_UP:
          to_y -= character_speed
        elif event.key == pygame.K_DOWN:
          to_y += character_speed
        if event.key == pygame.K_SPACE:
          running = False
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
          to_x = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          to_y = 0

    # 캐릭터 이동 and 제한
    character_x_pos += to_x 
    character_y_pos += to_y
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
      character_x_pos = screen_width - character_width
    if character_y_pos < 0:
      character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
      character_y_pos = screen_height - character_height
    
    # 박스 이동 and 제한
    if a == 1 :
      box_y_pos += box_speed
      if box_y_pos >= screen_height :
        box_x_pos = random.randint(0,(screen_width - box_widht))
        box_y_pos = 0
        jumsu += 1
        aa = random.randint(1,4) 
        if aa == 1:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = 0
          a = 1
        if aa == 2:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = screen_height - box_height
          a = 2
        if aa == 3:
          box_x_pos = 0
          box_y_pos =  random.randint(0,(screen_height - box_height))
          a = 3
        if aa == 4 :
          box_x_pos = screen_width - box_widht
          box_y_pos = random.randint(0,(screen_height - box_height))
          a = 4
    if a == 2 :
      box_y_pos -= box_speed
      if box_y_pos <= 0 :
        box_x_pos = random.randint(0,(screen_width - box_widht))
        box_y_pos = screen_height - box_height
        jumsu += 1
        aa = random.randint(1,4)
        if aa == 1:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = 0
          a = 1
        if aa == 2:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = screen_height - box_height
          a = 2
        if aa == 3:
          box_x_pos = 0
          box_y_pos =  random.randint(0,(screen_height - box_height))
          a = 3
        if aa == 4 :
          box_x_pos = screen_width - box_widht
          box_y_pos = random.randint(0,(screen_height - box_height))
          a = 4
    if a == 3 :
      box_x_pos += box_speed
      if box_x_pos >= screen_width :
        box_x_pos = 0
        box_y_pos =  random.randint(0,(screen_height - box_height))
        jumsu += 1
        aa = random.randint(1,4)
        if aa == 1:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = 0
          a = 1
        if aa == 2:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = screen_height - box_height
          a = 2
        if aa == 3:
          box_x_pos = 0
          box_y_pos =  random.randint(0,(screen_height - box_height))
          a = 3
        if aa == 4 :
          box_x_pos = screen_width - box_widht
          box_y_pos = random.randint(0,(screen_height - box_height))
          a = 4
    if a == 4 :
      box_x_pos -= box_speed
      if box_x_pos <= 0 :
        box_x_pos = screen_width - box_widht
        box_y_pos = random.randint(0,(screen_height - box_height))
        jumsu += 1
        aa = random.randint(1,4)
        if aa == 1:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = 0
          a = 1
        if aa == 2:
          box_x_pos = random.randint(0,(screen_width - box_widht))
          box_y_pos = screen_height - box_height
          a = 2
        if aa == 3:
          box_x_pos = 0
          box_y_pos =  random.randint(0,(screen_height - box_height))
          a = 3
        if aa == 4 :
          box_x_pos = screen_width - box_widht
          box_y_pos = random.randint(0,(screen_height - box_height))
          a = 4

    # speed 박스 이동 and 제한
    if b == 1 :
      speed_box_y_pos += random.randint(4,6)
      if speed_box_y_pos >= screen_height :
        speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
        speed_box_y_pos = 0
        jumsu += 1
        bb = random.randint(1,4) 
        if bb == 1:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = 0
          b = 1
        if bb == 2:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = screen_height - box_height
          b = 2
        if bb == 3:
          speed_box_x_pos = 0
          speed_box_y_pos =  random.randint(0,(screen_height - speed_box_height))
          b = 3
        if bb == 4 :
          speed_box_x_pos = screen_width - box_widht
          speed_box_y_pos = random.randint(0,(screen_height - speed_box_height))
          b = 4
    if b == 2 :
      speed_box_y_pos -= random.randint(4,6)
      if speed_box_y_pos <= 0 :
        speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
        speed_box_y_pos = screen_height - box_height
        jumsu += 1
        bb = random.randint(1,4)
        if bb == 1:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = 0
          b = 1
        if bb == 2:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = screen_height - box_height
          b = 2
        if bb == 3:
          speed_box_x_pos = 0
          speed_box_y_pos =  random.randint(0,(screen_height - speed_box_height))
          b = 3
        if bb == 4 :
          speed_box_x_pos = screen_width - box_widht
          speed_box_y_pos = random.randint(0,(screen_height - speed_box_height))
          b = 4
    if b == 3 :
      speed_box_x_pos += random.randint(4,6)
      if speed_box_x_pos >= screen_width :
        speed_box_x_pos = 0
        speed_box_y_pos =  random.randint(0,(screen_height - speed_box_height))
        jumsu += 1
        bb = random.randint(1,4)
        if bb == 1:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = 0
          b = 1
        if bb == 2:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = screen_height - box_height
          b = 2
        if bb == 3:
          speed_box_x_pos = 0
          speed_box_y_pos =  random.randint(0,(screen_height - speed_box_height))
          b = 3
        if bb == 4 :
          speed_box_x_pos = screen_width - box_widht
          speed_box_y_pos = random.randint(0,(screen_height - box_height))
          b = 4
    if b == 4 :
      speed_box_x_pos -= random.randint(4,6)
      if speed_box_x_pos <= 0 :
        speed_box_x_pos = screen_width - box_widht
        speed_box_y_pos = random.randint(0,(screen_height - speed_box_height))
        jumsu += 1
        bb = random.randint(1,4)
        if bb == 1:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = 0
          b = 1
        if bb == 2:
          speed_box_x_pos = random.randint(0,(screen_width - speed_box_widht))
          speed_box_y_pos = screen_height - box_height
          b = 2
        if bb == 3:
          speed_box_x_pos = 0
          speed_box_y_pos =  random.randint(0,(screen_height - speed_box_height))
          b = 3
        if bb == 4 :
          speed_box_x_pos = screen_width - box_widht
          speed_box_y_pos = random.randint(0,(screen_height - speed_box_height))
          b = 4

    # big 박스 이동 and 제한
    if c == 1 :
      big_box_y_pos += 2
      if big_box_y_pos >= screen_height :
        big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
        big_box_y_pos = 0
        jumsu += 1
        cc = random.randint(1,4) 
        if cc == 1:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = 0
          c = 1
        if cc == 2:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = screen_height - big_box_height
          c = 2
        if cc == 3:
          big_box_x_pos = 0
          big_box_y_pos =  random.randint(0,(screen_height - big_box_height))
          c = 3
        if cc == 4 :
          big_box_x_pos = screen_width - big_box_widht
          big_box_y_pos = random.randint(0,(screen_height - big_box_height))
          c = 4
    if c == 2 :
      big_box_y_pos -= 2
      if big_box_y_pos <= 0 :
        big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
        big_box_y_pos = screen_height - big_box_height
        jumsu += 1
        cc = random.randint(1,4)
        if cc == 1:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = 0
          c = 1
        if cc == 2:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = screen_height - big_box_height
          c = 2
        if cc == 3:
          big_box_x_pos = 0
          big_box_y_pos =  random.randint(0,(screen_height - big_box_height))
          c = 3
        if cc == 4 :
          big_box_x_pos = screen_width - big_box_widht
          big_box_y_pos = random.randint(0,(screen_height - big_box_height))
          c = 4
    if c == 3 :
      big_box_x_pos += 2
      if big_box_x_pos >= screen_width :
        big_box_x_pos = 0
        big_box_y_pos =  random.randint(0,(screen_height - big_box_height))
        jumsu += 1
        cc = random.randint(1,4)
        if cc == 1:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = 0
          c = 1
        if cc == 2:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = screen_height - big_box_height
          c = 2
        if cc == 3:
          big_box_x_pos = 0
          big_box_y_pos =  random.randint(0,(screen_height - big_box_height))
          c = 3
        if cc == 4 :
          big_box_x_pos = screen_width - big_box_widht
          big_box_y_pos = random.randint(0,(screen_height - big_box_height))
          c = 4
    if c == 4 :
      big_box_x_pos -= 2
      if big_box_x_pos <= 0 :
        big_box_x_pos = screen_width - big_box_widht
        big_box_y_pos = random.randint(0,(screen_height - big_box_height))
        jumsu += 1
        cc = random.randint(1,4)
        if cc == 1:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = 0
          c = 1
        if cc == 2:
          big_box_x_pos = random.randint(0,(screen_width - big_box_widht))
          big_box_y_pos = screen_height - big_box_height
          c = 2
        if cc == 3:
          big_box_x_pos = 0
          big_box_y_pos =  random.randint(0,(screen_height - big_box_height))
          c = 3
        if cc == 4 :
          big_box_x_pos = screen_width - big_box_widht
          big_box_y_pos = random.randint(0,(screen_height - big_box_height))
          c = 4

    # 캐릭터 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    # 박스 
    box_rect = box.get_rect()
    box_rect.left = box_x_pos
    box_rect.top = box_y_pos
    
    # speed 박스
    speed_box_rect = speed_box.get_rect()
    speed_box_rect.left = speed_box_x_pos
    speed_box_rect.top = speed_box_y_pos

    # big 박스
    big_box_rect = big_box.get_rect()
    big_box_rect.left = big_box_x_pos
    big_box_rect.top = big_box_y_pos
    
    # 충돌 처리
    if character_rect.colliderect(box_rect):
        d = 1
    if character_rect.colliderect(speed_box_rect):
        d = 1
    if character_rect.colliderect(big_box_rect):
        d = 1
    
    # 화면 그리기 
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(speed_box,(speed_box_x_pos,speed_box_y_pos))
    screen.blit(box,(box_x_pos,box_y_pos))
    screen.blit(big_box,(big_box_x_pos,big_box_y_pos))
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과 시간을 1000으로 나누어서 초 단위로 표시
    timer = game_font.render(str(int(total_time + elapsed_time)), True, (255,255,255))
    
    screen.blit(timer, (10, 10))
    if d == 1:
      screen.blit(end,(screen_width/2 - end_width/2 ,screen_height/2 - end_height/2 ))
      running = False
    pygame.display.update()
  print("당신의 피한 운석 수는", ":",jumsu,"입니다")
  pygame.time.delay(4000)
  pygame.quit()
  
  
def main3():
    #'O'와 'X'를 좀더 이해하기 쉽게 PLAYER_STONE과 COMPUTER_STONE 변수에 넣어 사용함
    PLAYER_STONE = 'O'
    COMPUTER_STONE = 'X'
    
    #게임에 관해 안내한다.
    def printInfo():
    	print("[Player-Computer Version]")
    	print("틱택토(tic-tac-toe) 두 명이 번갈아가며 'O'와 'X'를 3×3 판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하는 놀이입니다.")
    	print("플레이어는 'O', 컴퓨터는 'X'를 사용합니다.")
    	print("위치 선택은 아래와 같이 키보드의 숫자 키패드를 이용하세요.")
    	print("---------")
    	print("| 7 8 9 |")
    	print("| 4 5 6 |")
    	print("| 1 2 3 |")
    	print("---------")
    
    
    #보드의 내용을 화면에 출력한다.
    def drawBoard(board):
    	print("---------")
    	print("|", board[7], board[8], board[9], "|")
    	print("|", board[4], board[5], board[6], "|")
    	print("|", board[1], board[2], board[3], "|")
    	print("---------")  
    
    
    #누가 먼저 시작할지 랜덤하게 정하고, 정해진 순서('O' 또는 'X')를 리턴한다.
    def whoIsFirst():
    	first = random.choice(['O', 'X'])
    
    	if first == PLAYER_STONE:
    		print("플레이어부터 시작합니다.")
    	else:
    		print("컴퓨터부터 시작합니다.")
    
    	return first
    
    
    #플레이어로부터 위치를 입력받는다.
    def getPlayerMove(board, stone):
    	while True:
    		inData = input('위치를 선택하세요. ')
    		if len(inData) == 1 and '1' <= inData <= '9':
    			pos = int(inData)  
    			if board[pos] == '-':
    				board[pos] = stone
    				break
    		print('잘못 선택하셨습니다. 비어있는 칸을 숫자로 입력하세요.')
    
    
    #컴퓨터가 위치를 선택하게 한다.
    def getComputerMove(board, stone):
    	print('컴퓨터가 둡니다.')
    	
    	#컴퓨터가 두면 이길 위치를 찾아둔다.
    	for i in range(1, 10):
    		if board[i] == '-':
    			copyBoard = board[:]
    			copyBoard[i] = COMPUTER_STONE
    			if isWinner(copyBoard, COMPUTER_STONE):
    				board[i] = COMPUTER_STONE
    				return
    			
    	#플레이어가 두면 이길 위치를 찾아둔다.
    	for i in range(1, 10):
    		if board[i] == '-':
    			copyBoard = board[:]
    			copyBoard[i] = PLAYER_STONE
    			if isWinner(copyBoard, PLAYER_STONE):
    				board[i] = COMPUTER_STONE
    				return
    				
    	#앞에서부터 빈자리를 찾아 둡니다.
    	for i in range(1, 10):
    		if board[i] == '-':
    			board[i] = stone
    			break
    
    
    #보드에 놓여진 돌의 개수를 리턴한다.
    def numberOfStone(board):
    	n = 0
    	for c in board:
    		if c != '-':
    			n = n + 1
    	return n
    
    
    #보드에서 stone('O' 또는 'X')가 연속해서 3개 놓여졌는지 여부(True 또는 False)를 리턴한다.
    def isWinner(board, stone):
    	
    	#가로 세 행 확인
    	for i in [1, 4, 7]:
    		if board[i] == stone and board[i + 1] == stone and board[i + 2] == stone:
    			return True
    
    	#세로 세 열 확인
    	for i in [1, 2, 3]:
    		if board[i] == stone and board[i + 3] == stone and board[i + 6] == stone:
    			return True
    
    	#대각선(오른쪽 위에서 왼쪽 아래)
    	if board[1] == stone and board[5] == stone and board[9] == stone:
    		return True
    
    	#대각선(왼쪽 위에서 오른쪽 아래)
    	if board[7] == stone and board[5] == stone and board[3] == stone:
    		return True
    	
    	return False
    
    
    #틱택토 1게임을 진행합니다.
    def ticTacToe():
    	
    	#빈 틱택토 보드를 표현하기 위해서 '-'로 10개의 요소를 채운 리스트를 만듭니다.
    	#위치 정보와 리스트의 인덱스를 일치시키기 위해 10개의 요소를 채우고, 이후에 맨 앞(인덱스 0) 요소는 사용하지 않습니다.
    	tttBoard = ['-'] * 10
    
    	drawBoard(tttBoard)
    	
    	currentStone = whoIsFirst()
    	
    	while True:
    		if currentStone == PLAYER_STONE:
    			getPlayerMove(tttBoard, PLAYER_STONE)  
    			drawBoard(tttBoard)
    		
    			if isWinner(tttBoard, PLAYER_STONE):
    				print("축하합니다. 당신이 이겼어요!")
    				return PLAYER_STONE
    			
    			currentStone = COMPUTER_STONE
    		
    		else:
    			getComputerMove(tttBoard, COMPUTER_STONE)  
    			drawBoard(tttBoard)
    		
    			if isWinner(tttBoard, COMPUTER_STONE):
    				print("아쉽군요. 컴퓨터가 이겼습니다.")
    				return COMPUTER_STONE
    			
    			currentStone = PLAYER_STONE
    		
    		if numberOfStone(tttBoard) >= 9:
    			print("비겼습니다.")
    			return '-'
    			
    			
    
    printInfo()
    			
    resultList = []
    
    while True:
    	result = ticTacToe()
    	resultList.append(result)
    	
    	isContinued = input("한 게임 더 진행할까요?(y/n) ")
    	if isContinued == 'n':
    		break
    
    print('\n[게임 전적]')
    print(resultList.count(PLAYER_STONE), '승 ', resultList.count('-'), '무 ', resultList.count(COMPUTER_STONE), '패', sep = '')

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
      
def menu(p,stage):
    pygame.init()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("menu")
    background = pygame.image.load("background_r.png")
    a =  pygame.image.load("a.png")
    d =  pygame.image.load("d.png")
    xs = [0,1,2,3,4]
    x = 0
    font = pygame.font.SysFont("malgungothic",30)
    point = font.render("점수:" + str(p),True,(255,255,255))
    stage_point = font.render("스테이지:" + str(stage),True,(255,255,255))
    
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
                if event.key == pygame.K_a:
                    x -= 1
                    x = xs[x]
                if event.key == pygame.K_d:
                    x += 1
                    if x >= 5:
                        x = 0
                    x = xs[x]
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x_p, y_p = pygame.mouse.get_pos()    
                    if x_p > 50 and x_p < 120 and y_p > 290 and y_p < 350:
                        x -= 1
                        x = xs[x]
                    if x_p > 330 and x_p < 400 and y_p > 290 and y_p < 350:
                        x += 1
                        if x >= 5: 
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
            
        point = font.render("점수:" + str(p),True,(255,255,255))
        stage_point = font.render("스테이지:" + str(stage),True,(255,255,255))
        
        if x == 0:
            card = pygame.image.load("card_t.png")
        if x == 1:
            card = pygame.image.load("card_s.png")
        if x == 2:
            card = pygame.image.load("card_r.png")
        if x == 3:
            card = pygame.image.load("card_tic.png")
        if x == 4:
            card = pygame.image.load("card_e.png")
        screen.blit(background,(0,0))
        screen.blit(card,(50,40))
        screen.blit(point,(800,10))
        screen.blit(stage_point,(800,40))
        screen.blit(a,(50,290))
        screen.blit(d,(330,290))
        pygame.display.update()
         
    pygame.quit()

# 시작점
if __name__ == "__main__":
    running = window()
    h = 100
    p = 0
    stage = 0
    while running:
        running ,x = menu(p,stage)
        if running == False:
            break
        if x == 0:
            p,stage = main0(h)
        if x == 1:
            p = main1(h)
        if x == 2:
            main2()
        if x == 3:
            main3()
        if x == 4:
            englishs()


        
        