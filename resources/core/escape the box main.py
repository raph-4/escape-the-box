import pygame
from sys import exit
import time
from pygame.sprite import Group
import random
import json 
import bcrypt
import os

class volume(pygame.sprite.Sprite):
    def __init__(self,bar):
        super().__init__()
        self.clicked = False
        if bar == 'layout':
            self.image = pygame.image.load('escape the box\graphics/volume/border.png').convert_alpha()
            self.image = pygame.transform.scale(self.image , (500,100))
            self.rect = self.image.get_rect(center= (640,200))
            self.bar = 'layout'
        if bar == 'volume up':
            self.image = pygame.image.load('escape the box\graphics/volume/volume up.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (905,170))
            self.image = pygame.transform.scale(self.image , (70,60))
            self.bar = 'volume up' 
        if bar == 'volume down':
            self.image = pygame.image.load('escape the box\graphics/volume/volume down.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (300,170))
            self.image = pygame.transform.scale(self.image , (80,60))
            self.bar = 'volume down' 
        if bar == '1':
            self.image = pygame.image.load('escape the box\graphics/volume/1.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (402,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '1'
        if bar == '2':
            self.image = pygame.image.load('escape the box\graphics/volume/3.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (449,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '2'
        if bar == '3':
            self.image = pygame.image.load('escape the box\graphics/volume/2.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (497,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '3'
        if bar == '4':
            self.image = pygame.image.load('escape the box\graphics/volume/4.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (545,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '4'
        if bar == '5':
            self.image = pygame.image.load('escape the box\graphics/volume/5.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (593,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '5'
        if bar == '6':
            self.image = pygame.image.load('escape the box\graphics/volume/6.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (641,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '6'
        if bar == '7':
            self.image = pygame.image.load('escape the box\graphics/volume/7.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (689,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '7'
        if bar == '8':
            self.image = pygame.image.load('escape the box\graphics/volume/8.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (737,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '8'
        if bar == '9':
            self.image = pygame.image.load('escape the box\graphics/volume/9.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (785,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '9'
        if bar == '10':
            self.image = pygame.image.load('escape the box\graphics/volume/10.png').convert_alpha()
            self.rect = self.image.get_rect(topleft= (833,volume_y_pos ))
            self.image = pygame.transform.scale(self.image , (43,80))
            self.bar = '10'              
    
    def update(self,event):
        global master_vol

        previous_vol = master_vol        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.clicked:
                # Prevents multiple triggers while hovering
                self.clicked = True  
                if self.bar == 'volume up' and master_vol < 1:
                    master_vol = round(master_vol + 0.1, 1)

                elif self.bar == 'volume down' and master_vol > 0:
                    master_vol = round(master_vol - 0.1, 1)
            # loops music
            if previous_vol == 0 and master_vol > 0:
                bg_music.play(loops=-1)

            bg_music.set_volume(master_vol) 

        if event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

class Player(pygame.sprite.Sprite):
    def __init__(self,speed):
        super().__init__()
        self.base_image = pygame.image.load('escape the box\graphics\SPRITES\player.png').convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image , (50,40))
        self.image = self.base_image
        self.rect = self.image.get_rect(center= (211,161))
        
        self.use_wasd = True 
        self.angle = 0
        self.hit_time = None 
        self.speed = speed
    
    def toggle_controls(self):
        self.use_wasd  = not self.use_wasd

    def player_input(self):
        keys = pygame.key.get_pressed()
        direction = None
        if self.use_wasd:
            up, down, left, right = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
        else:
            up, down, left, right = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT

        #normal movement
        if keys[up]:  # Up
            self.rect.y -= 5 * self.speed
            direction = 0
        if keys[down]:  # Down
            self.rect.y += 5 * self.speed
            direction = 180
        if keys[left]:  # Left
            self.rect.x -= 5 * self.speed
            direction = 90
        if keys[right]:  # Right
            self.rect.x += 5 * self.speed
            direction = -90
        
        # Diagonal directions
        if keys[up] and keys[right]: 
            self.rect.y -= round(0.001 * self.speed)
            self.rect.x += round(0.001 * self.speed)
            direction = -45
        if keys[up] and keys[left]:  
            self.rect.y -= round(0.001 * self.speed)
            self.rect.x -= round(0.001 * self.speed)
            direction = 45
        if keys[down] and keys[right]:  
            self.rect.y += round(0.001 * self.speed)
            self.rect.x += round(0.001 * self.speed)
            direction = -135
        if keys[down] and keys[left]:  
            self.rect.y += round(0.001 * self.speed)
            self.rect.x -= round(0.001 * self.speed)
            direction = 135
        
        #stops the player from pressing opposing buttons
        if keys[left] and keys[right]:
            self.rect.x += 0
        if keys[up] and keys[down]:
            self.rect.y += 0            
            
        # sets the players image to face the correct direction depending on how its moving
        if direction is not None and direction != self.angle:
            self.angle = direction
            self.image = pygame.transform.rotate(self.base_image, self.angle)
            self.rect = self.image.get_rect(center = self.rect.center)

    def collision(self,group,target):
        #checks colliions with specific targets
        collided = pygame.sprite.spritecollide(self, group, False)
        for object in collided:
            if hasattr(object, 'name') and object.name == target:
                return True
        return False

    def position_change(self,position):
        self.rect.center = position

    def hit_door(self,group):     
        for object in group:
             if self.rect.colliderect(object.rect):
                object.start_animation()
                return object        
        return None        

    def collision_enemy(self, group, position):
        global deaths
        collided = pygame.sprite.spritecollide(self, group, False)

        # ensures collision only triggers on first contact
        if collided and not self.was_colliding:  
            self.hit_time = time.time()
            self.respawn_position = position
            deaths += 1
            # prevents multiple deaths
            self.was_colliding = True  

        elif not collided:
            # Resets when not colliding
            self.was_colliding = False  

        return collided

    def collide_with_colour(self, surface, colour, position):
        collision_points =[
            self.rect.topleft,
            self.rect.topright,
            self.rect.bottomleft,
            self.rect.bottomright,
            self.rect.midtop,
            self.rect.midbottom,
            self.rect.midleft,
            self.rect.midright,
            self.rect.center
        ]
        # check if any of the players points are touching the specified colour
        for point in collision_points:
            if 0 <= point[0] < surface.get_width() and 0 <= point[1] < surface.get_height():
                if surface.get_at(point)[:3] == colour:
                    self.rect.center = position
                    return True
        return False

    def update(self):
        self.player_input()

        # delay when colliding with the saws
        if self.hit_time and time.time() - self.hit_time >= 0.00002:
            self.rect.center = self.respawn_position
            self.hit_time = None 
                 
class level_1(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'box1':
            self.image = pygame.image.load('escape the box\levels\level 1/box1.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (80, 50))
            self.image = pygame.transform.scale(self.image , (280,224))
            self.name = 'box1'
        if type == 'box2':
            self.image = pygame.image.load('escape the box\levels\level 1/box2.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (446, 100))
            self.image = pygame.transform.scale(self.image , (626,183))
            self.name = 'box2'
        if type == 'box3':
            self.image = pygame.image.load('escape the box\levels\level 1/box3.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (186, 433))
            self.image = pygame.transform.scale(self.image , (264,200))
            self.name = 'box3'
        if type == 'box4':
            self.image = pygame.image.load('escape the box\levels\level 1/box4.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (793, 458))
            self.image = pygame.transform.scale(self.image , (382,250))
            self.name = 'box4'
        if type == 'box5':
            self.image = pygame.image.load('escape the box\levels\level 1\connection.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (445, 467))
            self.image = pygame.transform.scale(self.image , (355,80))
            self.name = 'box5'
        if type == 'background':
            self.image = pygame.image.load('escape the box\levels\level 1/background 1.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (0,0))
            self.image = pygame.transform.scale(self.image , (1280,720))
            self.name = 'background'

class Game_Buttons(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if  type == 'button_1':
            self.image = pygame.image.load('escape the box\graphics\game buttons/button.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (1003,219))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'button_1'
        if  type == 'button_2':
            self.image = pygame.image.load('escape the box\graphics\game buttons/button 2.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (1100,472))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'button_2'
        if  type == 'button_3':
            self.image = pygame.image.load('escape the box\graphics\game buttons/button 3.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (1010, 625))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'button_3'

class Portals(pygame.sprite.Sprite):
    def __init__(self,portal_type):
        super().__init__()
        if portal_type == 'purp_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal1.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (277,198))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'purp_portal'
        if portal_type == 'purp_con_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal1.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (461,173))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'purp_con_portal'

        if portal_type == 'red_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal2.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (461,173))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'red_portal'
        if portal_type == 'red_con_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal2.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (195,570))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'red_con_portal'

        if portal_type == 'yel_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal3.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (255, 225))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'yel_portal'
        if portal_type == 'yel_con_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal3.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (108, 630))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'yel_con_portal'

        if portal_type == 'pink_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal4.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (832, 73))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'pink_portal'
        if portal_type == 'pink_con_portal':
            self.image = pygame.image.load('escape the box\graphics\portals\portal5.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (680, 340))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'pink_con_portal'

        if portal_type == 'win_1':
            self.image = pygame.image.load('escape the box\graphics\portals\end_portal.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (962, 560))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'win_1'
        if portal_type == 'win_2':
            self.image = pygame.image.load('escape the box\graphics\portals\end_portal2.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (832, 460))
            self.image = pygame.transform.scale(self.image , (50,50))
            self.name = 'win_2'

def collision(target):
    collided = pygame.sprite.spritecollide(player_group.sprite,level2_group,False)
    if collided:
        for box in collided:
            if box.name == target:
                #print(f'hit: {box.name}')
                return True

class level_2(pygame.sprite.Sprite):
        def __init__(self,type):
            super().__init__()
            if type == 'box6':
                self.image = pygame.image.load('escape the box\levels\level 2/box6.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (80, 50))
                self.image = pygame.transform.scale(self.image , (400,400))
                self.name = 'box6'
            if type == 'box7':
                self.image = pygame.image.load('escape the box\levels\level 2/box7.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (600, 50))
                self.image = pygame.transform.scale(self.image , (500,500))
                self.name = 'box7'
            if type == 'box8':
                self.image = pygame.image.load('escape the box\levels\level 2/box5.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (80, 590))
                self.image = pygame.transform.scale(self.image , (1020,120))
                self.name = 'box8'
            if type == 'box9':
                self.image = pygame.image.load('escape the box\levels\level 2/box8.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (58, 31))
                self.image = pygame.transform.scale(self.image , (1200,650))
                self.name = 'box9'

class Enemy(pygame.sprite.Sprite):
    def __init__(self,type,bounds,speed,start_pos):
        super().__init__()
        self.image = pygame.image.load('escape the box\graphics\SPRITES\enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image , (90,60))
        self.rect = self.image.get_rect(center= start_pos)

        self.start_pos = start_pos
        self.enemy_type = type
        self.bounds = bounds
        self.speed = speed
        self.direction = -1

    def reset_pos(self):
        self.rect.center = self.start_pos

    def horizontal_movement(self):
        self.rect.x += self.direction * self.speed

        if self.rect.x <= self.bounds[0] or self.rect.x >= self.bounds[1]:
            self.direction *= -1

    def horizontal_movement_rev(self):
            self.rect.x -= self.direction * self.speed

            if self.rect.x <= self.bounds[0] or self.rect.x >= self.bounds[1]:
                self.direction *= -1
    
    def vertical_movement(self):
        self.rect.y += self.direction * self.speed

        if self.rect.y <= self.bounds[2] or self.rect.y >= self.bounds[3]:
            self.direction *= -1

    def diagonal_movement(self):
        self.rect.x -= self.direction * self.speed
        self.rect.y += self.direction * self.speed 

        if self.rect.y <= self.bounds[2] or self.rect.y >= self.bounds[3]:
            self.direction *= -2
        if self.rect.x <= self.bounds[0] or self.rect.x >= self.bounds[1]:
            self.direction *= -1

    def update(self):
        
        if self.enemy_type == 'horizontal':
            self.horizontal_movement()
        if self.enemy_type == 'horizontal_rev':
            self.horizontal_movement_rev()
        if self.enemy_type == 'vertical':
            self.vertical_movement()
        if self.enemy_type == 'diagonal':
            self.diagonal_movement()

class Saws(pygame.sprite.Sprite):
    def __init__(self,type,bounds,speed,start_pos):
        super().__init__()
        saw1 = pygame.image.load('escape the box\graphics\saws\Saw1.png').convert_alpha()
        saw2 = pygame.image.load('escape the box\graphics\saws\Saw2.png').convert_alpha()
        saw3 = pygame.image.load('escape the box\graphics\saws\Saw3.png').convert_alpha()
        saw4 = pygame.image.load('escape the box\graphics\saws\Saw4.png').convert_alpha()
        saw5 = pygame.image.load('escape the box\graphics\saws\Saw5.png').convert_alpha()
        saw6 = pygame.image.load('escape the box\graphics\saws\Saw6.png').convert_alpha()
        saw7 = pygame.image.load('escape the box\graphics\saws\Saw7.png').convert_alpha()
        saw8 = pygame.image.load('escape the box\graphics\saws\Saw8.png').convert_alpha()
        saw9 = pygame.image.load('escape the box\graphics\saws\Saw9.png').convert_alpha()
        saw10 = pygame.image.load('escape the box\graphics\saws\Saw10.png').convert_alpha()

        #creates the animation for spinning saws
        self.saw_spin = [
            pygame.transform.scale(img, (50,50))

            for img in [saw1,saw2,saw3,saw4,saw5,saw6,saw7,saw8,saw9,saw10]
            ]


        self.saw_index = 0

        self.image = self.saw_spin[self.saw_index]
        self.rect = self.image.get_rect(midbottom = (start_pos))

        self.random_direction_x = random.choice([1, -1, 2, -2])
        self.random_direction_y = random.choice([1, -1, 2, -2])

        self.saw_type = type
        self.speed = speed
        self.bounds = bounds
        self.direction = 1

    def animation_state(self):
        self.saw_index += 0.5
        if self.saw_index >= len(self.saw_spin):
            self.saw_index = 0
        self.image = self.saw_spin[int(self.saw_index)] 

    def horizontal_saw(self):
        self.rect.x += self.direction * self.speed

        if self.rect.x <= self.bounds[0] or self.rect.x >= self.bounds[1]:
            self.direction *= -1
    
    def horizontal_saw_rev(self):
        self.rect.x -= self.direction * self.speed

        if self.rect.x <= self.bounds[0] or self.rect.x >= self.bounds[1]:
            self.direction *= -1

    def vertical_saw(self):
        self.rect.y += self.direction * self.speed

        if self.rect.y <= self.bounds[2] or self.rect.y >= self.bounds[3]:
            self.direction *= -1

    #this saw moves in a random direction
    def random_saw(self):
        self.rect.x += self.random_direction_x * self.speed
        self.rect.y += self.random_direction_y * self.speed

        if self.rect.x <= self.bounds[0] or self.rect.x >= self.bounds[1]:
            self.random_direction_x*= -1
        if self.rect.y <= self.bounds[2] or self.rect.y >= self.bounds[3]:
            self.random_direction_y*= -1


    def update(self):
        self.animation_state()
        
        if self.saw_type == 'horzontal':
            self.horizontal_saw()
        if self.saw_type == 'horizontal_rev':
            self.horizontal_saw_rev()
        if self.saw_type == 'vertical':
            self.vertical_saw()
        if self.saw_type == 'random':
            self.random_saw()

class button(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.last_click_time = 0 
        self.click_delay = 0.5

        if type == 'start':
            self.image = pygame.image.load('escape the box\graphics\start screen\start.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,300))
            self.button = 'start'
        elif type == 'settings':
            self.image =  pygame.image.load('escape the box\graphics\start screen\settings.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,500))
            self.button = 'settings'
        elif type == 'back':
            self.image =  pygame.image.load('escape the box\graphics\start screen/back.png').convert_alpha()
            self.rect = self.image.get_rect(center = (90,50))
            self.button = 'back'
        elif type == 'leaderboard':
            self.image =  pygame.image.load('escape the box\graphics\start screen/leaderboard.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,400))
            self.button = 'leaderboard'
        elif type == 'next':
            self.image =  pygame.image.load('escape the box\graphics\start screen/next.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,400))
            self.button = 'next'
        elif type == 'next2':
            self.image =  pygame.image.load('escape the box\graphics\start screen/next.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (1110,635))
            self.button = 'next2'
        elif type == 'continue':
            self.image =  pygame.image.load('escape the box\graphics\start screen\continue.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,400))
            self.button = 'continue'     
        elif type == 'continue2':
            self.image =  pygame.image.load('escape the box\graphics\start screen\continue.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,600))
            self.button = 'continue2'            
        elif type == 'save game':
            self.image =  pygame.image.load('escape the box\graphics\start screen\save game.png').convert_alpha()
            self.rect = self.image.get_rect(center = (600,400))
            self.button = 'save game'                    
        elif type == 'wasd':
            self.image =  pygame.image.load('escape the box\graphics\start screen\wasd.png').convert_alpha()
            self.rect = self.image.get_rect(center = (500,400))
            self.button = 'wasd'        
        elif type == 'arrow':
            self.image =  pygame.image.load('escape the box\graphics\start screen/arrow keys.png').convert_alpha()
            self.rect = self.image.get_rect(center = (900,400))
            self.button = 'arrow' 
        elif type == 'wasd2':
            self.image =  pygame.image.load('escape the box\graphics\start screen\wasd.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (280,82))
            self.rect = self.image.get_rect(center = (461,400))
            self.button = 'wasd2'        
        elif type == 'arrow2':
            self.image =  pygame.image.load('escape the box\graphics\start screen/arrow keys.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (340,82))
            self.rect = self.image.get_rect(center = (808,400))
            self.button = 'arrow2'               
        elif type == 'help on':
            self.image =  pygame.image.load('escape the box\graphics\start screen\help on.png').convert_alpha()
            self.rect = self.image.get_rect(center = (500,600))
            self.button = 'help on'        
        elif type == 'help off':
            self.image =  pygame.image.load('escape the box\graphics\start screen\help off.png').convert_alpha()
            self.rect = self.image.get_rect(center = (750,600))
            self.button = 'help off'             

    def clicked(self,event):
        current_time = time.time() 
        if event.type == pygame.MOUSEBUTTONDOWN and (current_time - self.last_click_time) > self.click_delay:
                if self.rect.collidepoint(event.pos):
                    global level,control_state,control_state2,help_activated,temp_active,Next_2_clicked
                    self.last_click_time = current_time          
                    if self.button == 'start':  
                        level = 1
                        return level
                    if self.button == 'leaderboard':
                        level = 0.1
                        return level
                    if self.button == 'back':
                        level = 0
                        return level
                    if self.button == 'settings':
                        level = 0.2
                        return level
                    if self.button == 'next':
                        level += 0.5
                        level = round(level)
                        return level
                    if self.button == 'next2':
                        temp_active = False
                        Next_2_clicked = True
                        return temp_active, Next_2_clicked 

                    if self.button == 'continue':
                       level = 4
                       return level
                    if self.button == 'continue2':
                       level = 0
                       return level                    
                    if self.button == 'save game':
                        stop_timer()
                        save_game(logged_in_user)

                    if self.button == 'wasd':
                        control_state = 1
                        player.toggle_controls()   
                        return control_state                
                    if self.button == 'arrow':
                        control_state = 0 
                        player.toggle_controls() 
                        return control_state
                                                             
                    if self.button == 'wasd2':
                        control_state = 1
                        player.toggle_controls()   
                        return control_state                
                    if self.button == 'arrow2':
                        control_state = 0 
                        player.toggle_controls() 
                        return control_state
                       
                    if self.button == 'help on':
                        control_state2 = 0  
                        help_activated = True
                        temp_active = True
                        return control_state2,help_activated,temp_active                
                    if self.button == 'help off':
                        control_state2 = 1  
                        help_activated = False
                        return control_state2,help_activated
    
    def update(self,event):
        self.clicked(event)

class pause(pygame.sprite.Sprite):
    def  __init__(self,font,font2):
        super().__init__()        
        self.base_image = pygame.image.load('escape the box/levels/level 4/pause.png').convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image , (700,700))
        self.image = self.base_image
        self.rect = self.image.get_rect(topleft = (300, 10))
        
        self.font = font
        self.other_font = font2

        self.title = self.font.render('Pause',False, (255,255,255))
        self.title_rect = self.title.get_rect(center = (650,80))

        self.message = self.other_font.render('press escape to continue',False, (255,255,255))
        self.message_rect = self.message.get_rect(center = (650,160))

    def draw_text(self,screen):
        screen.blit(self.title, self.title_rect)
        screen.blit(self.message, self.message_rect)

class Help(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'help1':
            self.image = pygame.image.load('escape the box\levels\help\help level 1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image , (1280,720))
            self.rect = self.image.get_rect(topleft = (0,0))
            self.button = 'help1'
        elif type == 'help2':
            self.image =  pygame.image.load('escape the box\levels\help\help level 2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image , (1280,720))
            self.rect = self.image.get_rect(topleft = (0,0))
            self.button = 'help2'
        elif type == 'help3':
            self.image =  pygame.image.load('escape the box\levels\help\help level 3.png').convert_alpha()
            self.image = pygame.transform.scale(self.image , (1280,720))
            self.rect = self.image.get_rect(topleft = (0,0))
            self.button = 'help3'

class Door(pygame.sprite.Sprite):
    def __init__(self,type,start_pos,change_level,completed_level):
        super().__init__()
        if  type == 'sub_level_1':
            door1 = pygame.image.load('escape the box\graphics\door\door1.png').convert_alpha()
            door2 = pygame.image.load('escape the box\graphics\door\door1.1.png').convert_alpha()
            door3 = pygame.image.load('escape the box\graphics\door\door1.2.png').convert_alpha()
            door4 = pygame.image.load('escape the box\graphics\door\door1.3.png').convert_alpha()
            door5 = pygame.image.load('escape the box\graphics\door\door1.4.png').convert_alpha() 
            door6 = pygame.image.load('escape the box\graphics\door\door1.5.png').convert_alpha()     
            door7 = pygame.image.load('escape the box\graphics\door\door1.6.png').convert_alpha()  

            self.door_frames = [
            pygame.transform.scale(img, (150,160))
            for img in [door1,door2,door3,door4,door5,door6,door7]
        ]          
            self.name = 'sub_level_1'

        if  type == 'sub_level_2':
            if completed_level == 0:
                door1 = pygame.image.load('escape the box\graphics\door\door 1.png').convert_alpha()
                door2 = pygame.image.load('escape the box\graphics\door\door 2.png').convert_alpha()
                door3 = pygame.image.load('escape the box\graphics\door\door 3.png').convert_alpha()
                door4 = pygame.image.load('escape the box\graphics\door\door 4.png').convert_alpha()
                door5 = pygame.image.load('escape the box\graphics\door\door 5.png').convert_alpha()        
                self.name = 'sub_level_2'        

        self.door_frames = [
            pygame.transform.scale(img, (150,160))
            for img in [door1,door2,door3,door4,door5,door6,door7]
        ]

        self.animating = False
        self.change_level = change_level
        self.door_index = 0
        self.image = self.door_frames[self.door_index]
        self.rect = self.image.get_rect(topleft = (start_pos))
        self.animation_done = False

    def start_animation(self):
        if not self.animating:
            self.animating = True
            self.door_index = 0
            self.animation_done = False

    def animation_state(self):
        if self.animating:
            self.door_index += 0.1
            if self.door_index >= len(self.door_frames):
                self.door_index = len(self.door_frames) - 1
                self.animating = False
                self.animation_done = True
                #self.door_index = 0
            self.image = self.door_frames[int(self.door_index)] 

    def update(self):
        self.animation_state()

class level_3(pygame.sprite.Sprite):
        def __init__(self,type):
            super().__init__()
            if type == 'box10':
                self.image = pygame.image.load('escape the box\levels\level 3/1.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (0, 0))
                self.image = pygame.transform.scale(self.image , (1280,720))
                self.name = 'box10'
            if type == 'box11':
                self.image = pygame.image.load('escape the box\levels\level 3/2.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (0, 0))
                self.image = pygame.transform.scale(self.image , (1280,720))
                self.name = 'box11'
            if type == 'box12':
                self.image = pygame.image.load('escape the box\levels\level 3/3.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (0, 0))
                self.image = pygame.transform.scale(self.image , (1280,720))
                self.name = 'box12'
            if type == 'box13':
                self.image = pygame.image.load('escape the box\levels\level 3/4.png').convert_alpha()
                self.rect = self.image.get_rect(topleft = (0, 0))
                self.image = pygame.transform.scale(self.image , (1280,720))
                self.name = 'box13'

def update_volume_bar():
    # clears the group before updating the bar
    volume_increment.empty()
    # converts the volume into a count (1 to 10)
    num_bars = int(master_vol * 10)  

    # Add the correct number of bars to the group
    for i in range(num_bars):
        volume_increment.add(bars[i]) 
    
def reset_enemies():
    for enemy in enemies:
        enemy.reset_pos()

#hashes the password when saved into the file
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

#verifies the password to allow the user to sign in 
def verify_password(stored_password, entered_password):
    return bcrypt.checkpw(entered_password.encode(), stored_password.encode())

#checks whether the file exists
def load_users():
    if os.path.exists(File_name):
        with open(File_name, "r") as f:
            return json.load(f)
    return {}

#saves new users into the file 
def save_users(users):
    with open(File_name, "w") as f:
        json.dump(users, f, indent=4)

#signs up new users 
def register_user(username, password):
    global condition
    users = load_users()
    if username in users:
        condition = 3
        return False
    
    users[username] = {
        "password": hash_password(password),
        "clear_time": 0,
        "deaths": 0,
        "score": 0
    }
    save_users(users)
    condition = 2
    return True
#allows users to login to their accounts
def login_user(username, password):
    global condition, logged_in,logged_in_user
    users = load_users()
    if username in users and verify_password(users[username]["password"], password):
        condition = 1
        logged_in = 1
        logged_in_user = username
        return True
    condition = 4
    return False

#converts players information into a dictionary
def load_leaderboard(filename = "escape the box/resources\players.json"):
    with open(filename, 'r') as file:
        users = json.load(file)
        leaders = [{"username": user, **data} for user, data in users.items()]
    return leaders

def draw_leaderboard(screen, leaders):
    screen.fill(swamp_green)
    headers = ['Username','Clear Time', 'Deaths', 'Score']
    x_positions = [300, 500, 700, 850]
    y_start = 200

    # create leaderboad headers and space them out
    for i, header in enumerate(headers):
        text_surface = base_font2.render(header, True, white)
        screen.blit(text_surface, (x_positions[i], y_start))

    # draws a line differentiating the titles and the scores 
    pygame.draw.line(screen, black, (250,y_start +30), (950, y_start + 30), 2 )

    # writes out the users information in a line across the screen giving it a nice presentation
    for index, entry in enumerate(leaders):
        y_position = y_start + 50 + (index * 40)

        if y_position < 670:
            values = [
                entry["username"], 
                str(entry["clear_time"]), 
                str(entry["deaths"]), 
                str(entry['score'])
            ]
            for i, value in enumerate(values):
                text_surface = base_font2.render(value, True, white)
                screen.blit(text_surface, (x_positions[i], y_position))

def save_game(username):
    users = load_users()

    users[username]["clear_time"] = formatted_time  
    users[username]["deaths"] = deaths 
    users[username]["score"] = score

    save_users(users)

def stop_timer():
    global elapsed_time, timer_running, formatted_time
    if timer_running:
        elapsed_time = int(pygame.time.get_ticks() / 1000) - start_time
        timer_running = False

        minutes, seconds = divmod(elapsed_time, 60)
        formatted_time = f"{minutes:02}:{seconds:02}"

def restart_timer():
    global timer_running
    if timer_running == False:
        timer_running = True

pygame.init()
screen =  pygame.display.set_mode((1280,720))
pygame.display.set_caption('Escape the Box')
clock = pygame.time.Clock()
font = pygame.font.Font(None,200)
font2 = pygame.font.Font(None,120)
base_font = pygame.font.Font(None, 60) 
base_font2 = pygame.font.Font(None, 40)

# titles and header
game_name = font.render('Escape The Box',False,(255,243,243))
game_name_rect = game_name.get_rect(center = (600,100))

leaderboard_title = font2.render('Leaderboard',False, (255,255,255))
leaderboard_rect = leaderboard_title.get_rect(center = (630,100))

settings_title = font2.render('Settings',False,(255,255,255))
settings_rect = settings_title.get_rect(center = (640,100))

help_title = base_font.render('Help on/off',False,(255,255,255))
help_rect = help_title.get_rect(center = (640,500))

controlls_title = base_font.render('Control change',False,(255,255,255))
controlls_rect = controlls_title.get_rect(center = (640,300))

level_complete_1 = font2.render('You have completed level 1',False,(255,243,243))
level_complete_1_rect = game_name.get_rect(topleft = (100,50))
level_complete_2 = font2.render('You have completed level 2',False,(255,243,243))
level_complete_2_rect = game_name.get_rect(topleft = (100,50))

game_complete = font2.render('You have completed the game',False, (255,255,255))
game_complete_rect = game_complete.get_rect(center = (630,100))

#initialized value
level = -1
master_vol = 0
deaths = 0
bg_music = pygame.mixer.Sound('escape the box/resources/audio')
looped = False
#bg_music.play(loops = -1)
#bg_music.set_volume(master_vol)
volume_y_pos = 159
game_active = True
door_triggered = None
completed_level = 0
condition = 0
start_time = None
increased = False
control_state = 1
control_state2 = 1
cooldown = 1
help_activated = False
prev_control_state = -1
prev_control_state2 = -1
# temp active ensure that if help is on the help screen show up first
temp_active = False
paused = False 
original_speeds = {}
score = 0
elapsed_time = 0
timer_running = False 
logged_in_user = None

#file for player data
File_name = "escape the box/resources\players.json"

#text and information
user_txt = ''
pass_txt = ''
message_1 = 'Enter your username:'
message_2 = 'Enter your password:'
check1 = 'You have successfully logged in'
check2 = 'You have successfully signed in'
check3 = 'Username already exists'
check4 = 'Incorrect username or password '
logged_in = 0
box_1_filled = False
box_2_filled = False

#rectangles
input_rect = pygame.Rect(500, 150, 300, 60)
input_rect2 = pygame.Rect(500, 300, 300, 60)
login_rect = pygame.Rect(500, 400, 200, 60)
signup_rect = pygame.Rect(410, 500, 200, 60)
continue_rect = pygame.Rect(410, 600, 200, 60)

#colour and colour states
colour_active = pygame.Color('lightskyblue3')
colour_passive= pygame.Color('gray15')
colour = colour_passive
colour2 = colour_passive

active = False
active2 = False

#group objects
start =button('start')
leaderboard =button('leaderboard')
settings =button('settings')
Next = button('next')
Next2 = button('next2')
Continue = button('continue')
Continue2 = button('continue2')
save = button('save game')
back = button('back')
wasd = button('wasd')
wasd2 = button('wasd2')
arrow = button('arrow')
arrow2 = button('arrow2')
help_on = button('help on')
help_off = button('help off')

vol_layout = volume('layout')
vol_up = volume('volume up')
vol_down = volume('volume down')
# volume bar desplay
bars = [volume(str(i)) for i in range(1, 11)]

help1 = Help('help1')
help2 = Help('help2')
help3 = Help('help3')

box1 = level_1('box2')
box2 = level_1('box3')
box3 = level_1('box4')
box4 = level_1('box1')
box5 = level_1('box5')
box6 = level_2('box6')
box7 = level_2('box7')
box8 = level_2('box8')
box9 = level_2('box9')
box10 = level_3('box10')
box11 = level_3('box11')
box12 = level_3('box12')
box13 = level_3('box13')
pause_screen = pause(font2,base_font)

portal1 = Portals('purp_portal')
portal2 = Portals('purp_con_portal')
portal3 = Portals('red_portal')
portal4 = Portals('red_con_portal')
portal5 = Portals('yel_portal')
portal6 = Portals('yel_con_portal')
portal7 = Portals('pink_portal')
portal8 = Portals('pink_con_portal')
win_1 = Portals('win_1')
win_2 = Portals('win_2')

# Define boundaries (x_min, x_max, y_min, y_max)
box_bounds = (0, 800, 0, 600)
saw1 = Saws('vertical', box_bounds, 3, (200,200))


box_bounds2 = (620, 1040, 141, 345)
side_saw1 = Saws('horzontal', box_bounds2, 3, (647, 193))
side_saw2 = Saws('horizontal_rev', box_bounds2, 3, (1050, 313))
side_saw3 = Saws('horzontal', box_bounds2, 3, (647, 423))

box_bounds3 = (105, 420, 75, 380)
rand_saw1 = Saws('random', box_bounds3, 1, (280,190))
rand_saw2 = Saws('random', box_bounds3, 1, (310,230))
rand_saw3 = Saws('random', box_bounds3, 1, (380,250))

enemy_bounds = (70,1150,45,610)
enemy_bounds2 = (70,357,269,661)
side_enemy = Enemy('horizontal',enemy_bounds,3,(1180,130))
side_enemy2 = Enemy('horizontal_rev',enemy_bounds,3,(130,590))
vert_enemy = Enemy('vertical',enemy_bounds,4,(1130,400))
diag_enemy = Enemy('diagonal',enemy_bounds2,3,(130,580))

door1 = Door('sub_level_1', (565,10),3.3,completed_level)

player= Player(1)

switch_button_1 = Game_Buttons('button_1')
switch_button_2 = Game_Buttons('button_2')
switch_button_3 = Game_Buttons('button_3')

#Groups
buttons = pygame.sprite.Group(start,leaderboard,settings)
level_group = pygame.sprite.Group(box1,box2,box3,box4)
game_buttons = pygame.sprite.Group(switch_button_1)
level2_group = pygame.sprite.Group(box6,box7,box8)
level3_group = pygame.sprite.Group(box10)
volume_bar = pygame.sprite.Group(vol_layout,vol_up,vol_down)
volume_increment = pygame.sprite.Group()
for bar in bars:
    volume_increment.add(bar)
player_group = pygame.sprite.GroupSingle(player)
pause_group =  pygame.sprite.GroupSingle(pause_screen)
portals_lvl1 = pygame.sprite.Group(portal1,portal2,win_1)
portals_lvl2 = pygame.sprite.Group(portal5,portal6,portal7,win_2)
saws = pygame.sprite.Group(rand_saw1, rand_saw2, rand_saw3, side_saw1,side_saw2,side_saw3)
enemies = pygame.sprite.Group(side_enemy,side_enemy2,vert_enemy,diag_enemy)
doors = pygame.sprite.Group(door1)
help_group = pygame.sprite.Group(help1)

#colours
swamp_green = (47,59,56)
blue = (0,0,255)
purple = (122,45,204)
green_win = (35,177,76)
red = (255,0,0)
maroon = (128,0,0)
dark_purp = (153,104,225)
yellow = (255,242,0)
teal = (44,237,170)
pink = (204,15,214)
dark_blue = (79,123,196)
black = (0,0,0)
white = (255,255,255)
happened = 0
Next_2_clicked = False

while game_active:
    pos  = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            #skip to level 2 and skip login
            if event.key == pygame.K_2:
                level = 2
            if event.key == pygame.K_0:
                level = 0
            #pausing
            elif event.key == pygame.K_ESCAPE:
                paused = not paused  

                if paused:
                    stop_timer()
                    # Store original speeds, when the game is paused all speeds are set to 0
                    for enemy in enemies:
                        original_speeds[enemy] = enemy.speed 
                        enemy.speed = 0  
                    
                    for saw in saws:
                        original_speeds[saw] = saw.speed
                        saw.speed = 0
                    
                    original_speeds[player] = player.speed
                    print(original_speeds)
                    player.speed = 0

                else:
                    # Restore original speeds when unpausing
                    restart_timer()
                    for obj, speed in original_speeds.items():
                        obj.speed = speed

                    original_speeds.clear()  

        #text input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

            if input_rect2.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False
        
        # creates the buttons 
            if login_rect.collidepoint(event.pos) and user_txt and pass_txt:
                login_user(user_txt, pass_txt)

            if signup_rect.collidepoint(event.pos) and user_txt and pass_txt:
                register_user(user_txt, pass_txt)
        # cannot start the game unless logged in  
            if continue_rect.collidepoint(event.pos) and user_txt and pass_txt and logged_in == 1:
                level = 0  

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_txt = user_txt[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                else:
                    user_txt += event.unicode

            if active2 == True:
                if event.key == pygame.K_BACKSPACE:
                    pass_txt = pass_txt[:-1]
                elif event.key == pygame.K_RETURN:
                    active2 = False
                else:
                    pass_txt += event.unicode        

    if level == -1:
    #colours screen
        screen.fill(black)
    
    #centers all of the assets
        input_rect.x = (screen.get_width() - input_rect.width) // 2
        input_rect2.x = (screen.get_width() - input_rect2.width) // 2
        login_rect.x = (screen.get_width() - login_rect.width) // 2 
        signup_rect.x = (screen.get_width() - signup_rect.width) // 2 
        continue_rect.x = (screen.get_width() - signup_rect.width) // 2 

    #renders all of the assets on screen
        pygame.draw.rect(screen,colour,input_rect,2)
        pygame.draw.rect(screen,colour2,input_rect2,2)

        pygame.draw.rect(screen, pygame.Color("slategray2"), login_rect)
        pygame.draw.rect(screen, pygame.Color("slategray3"), signup_rect)
        pygame.draw.rect(screen, pygame.Color("teal"), continue_rect)

    #render text
        screen.blit(base_font.render(message_1, True, (255, 255, 255)), (430, 90))
        screen.blit(base_font.render(message_2, True, (255, 255, 255)), (430, 240))
        if condition == 1:
            screen.blit(base_font2.render(check1, True, (255, 255, 255)), (800, 620))
        if condition == 2:
            screen.blit(base_font2.render(check2, True, (255, 255, 255)), (800, 620))    
        if condition == 3:
            screen.blit(base_font2.render(check3, True, (255, 255, 255)), (800, 620))  
        if condition == 4:
            screen.blit(base_font2.render(check4, True, (255, 255, 255)), (800, 620)) 

        username_surf = base_font.render(user_txt, True, (255, 255, 255))
        password_surf = base_font.render("*" * len(pass_txt), True, (255, 255, 255))
        screen.blit(username_surf, (input_rect.x + 5, input_rect.y + 5))
        screen.blit(password_surf, (input_rect2.x + 5, input_rect2.y + 5))

        screen.blit(base_font.render("Login", True, (255, 255, 255)), (login_rect.x + 45, login_rect.y + 10))
        screen.blit(base_font.render("Sign Up", True, (255, 255, 255)), (signup_rect.x + 25, signup_rect.y + 10))
        screen.blit(base_font.render("Continue", True, (255, 255, 255)), (continue_rect.x + 7, continue_rect.y + 10))

    #text box active and unactive state
        if active:
            colour = colour_active
        else:
            colour = colour_passive
        if active2:
            colour2 = colour_active
        else:
            colour2 = colour_passive

    #widens textbox when writing
        input_rect.w = max(300,username_surf.get_width()+10)
        input_rect2.w = max(300,password_surf.get_width()+10)

    if level == 0:
        screen.fill(swamp_green)
        screen.blit(game_name,game_name_rect)
        buttons.draw(screen)
        buttons.update(event)
        if buttons.has(Continue2):
            buttons.remove(Continue2)

        if buttons.has(back):
            buttons.empty()

        if buttons.has(start) == False:
            buttons.add(start,leaderboard,settings)

    if level == 0.1:
        buttons.empty()
        if buttons.has(back) == False:
            buttons.add(back)
            
        screen.fill(swamp_green)
        leaderboard_vals = load_leaderboard()
        draw_leaderboard(screen, leaderboard_vals)
        screen.blit(leaderboard_title,leaderboard_rect)
        buttons.draw(screen)
        buttons.update(event)

    if level == 0.2:
        buttons.empty()
        if buttons.has(back) == False:
            buttons.add(back)

        update_volume_bar()
        screen.fill(swamp_green)
        screen.blit(settings_title,settings_rect)
        screen.blit(help_title, help_rect)
        screen.blit(controlls_title, controlls_rect)        
        increased = True        

        volume_bar.draw(screen)
        buttons.update(event)

        # if you click the wasd button it will disappear and the arrow keys button will appear and vice versa
        if control_state == 1:
            if buttons.has(arrow) == False:
                buttons.add(arrow)
            if buttons.has(wasd):
                buttons.remove(wasd)
        else:  
            if buttons.has(wasd) == False:
                buttons.add(wasd)
            if buttons.has(arrow):
                buttons.remove(arrow)   

        # if you click the help_on button it will disappear and the help_off button will appear and vice versa
        if control_state2 == 1:
            if buttons.has(help_on) == False:
                buttons.add(help_on)
            if buttons.has(help_off):
                buttons.remove(help_off)
        else:  
            if buttons.has(help_off) == False:
                buttons.add(help_off)
            if buttons.has(help_on):
                buttons.remove(help_on)

        buttons.draw(screen)                         

        for button in buttons:
            button.update(event)

        volume_bar.update(event)
        volume_increment.draw(screen)

    if level == 1:

        if temp_active == True:
            buttons.empty()
            help_group.draw(screen)  
            if buttons.has(Next2) == False:
                buttons.add(Next2)
            buttons.draw(screen)
            buttons.update(event)
        else:  
            screen.fill('blue')
            if level_group.has(box1) == False:
                level_group.add(box1,box2,box3,box4)
            if portals_lvl1.has(portal1):
                portals_lvl1.add(portal1,portal2,win_1)
            level_group.draw(screen)
            game_buttons.draw(screen)
            portals_lvl1.draw(screen)
            player_group.draw(screen)

            # draws a pause screen onto the screen
            if paused:
                buttons.empty()
                pause_group.draw(screen)
                pause_screen.draw_text(screen)

                if control_state == 1:
                    if buttons.has(arrow2) == False:
                        buttons.add(arrow2)
                    if buttons.has(wasd2):
                        buttons.remove(wasd2)
                else:  
                    if buttons.has(wasd2) == False:
                        buttons.add(wasd2)
                    if buttons.has(arrow2):
                        buttons.remove(arrow2) 
                buttons.draw(screen)
                for button in buttons:
                    button.update(event)

            player_group.update()

            # if the player collides with the backround they die, so deaths is incremented 
            # and it adds the portals and button back onto the screen if they are gone
            if player.collide_with_colour(screen, blue, (211, 161)):
                deaths += 1
                if portals_lvl1.has(portal1,portal2) == False:
                    portals_lvl1.add(portal1,portal2)
                if game_buttons.has(switch_button_1) == False:
                    game_buttons.add(switch_button_1)    

            #checks if the player collides with the portal and then teleports them
            if player.collide_with_colour(screen, purple, (490,193)):
                portals_lvl1.remove(portal1,portal2)

            if player.collide_with_colour(screen, green_win, (122, 100)):
                level = 1.5
                player_group.remove(player)
                level_group.empty()
                portals_lvl1.empty()
                game_buttons.empty()

            if player.collision(game_buttons, 'button_1'):
                portals_lvl1.remove(win_1)
                portals_lvl1.add(portal3,portal4)
                level = 1.1

    if level ==1.1:
        screen.fill('red')
        game_buttons.remove(switch_button_1)
        level_group.add(box5)
        game_buttons.add(switch_button_2)

        level_group.draw(screen)
        game_buttons.draw(screen)
        portals_lvl1.draw(screen)
        player_group.draw(screen)
        if paused:
                buttons.empty()
                pause_group.draw(screen)
                pause_screen.draw_text(screen)

                if control_state == 1:
                    if buttons.has(arrow2) == False:
                        buttons.add(arrow2)
                    if buttons.has(wasd2):
                        buttons.remove(wasd2)
                else:  
                    if buttons.has(wasd2) == False:
                        buttons.add(wasd2)
                    if buttons.has(arrow2):
                        buttons.remove(arrow2) 
                buttons.draw(screen)
                for button in buttons:
                    button.update(event)

        if player.collide_with_colour(screen, maroon, (265,590)):
            portals_lvl1.remove(portal3,portal4)
            
        player_group.update()

        if player.collide_with_colour(screen, red, (211, 161)):
            deaths += 1
            level = 1
            portals_lvl1.remove(portal3,portal4)
            game_buttons.remove(switch_button_2)
            portals_lvl1.add(portal1,portal2,win_1)
            game_buttons.add(switch_button_1)
        
        if player.collision(game_buttons, 'button_2'):
            level_group.remove(box5)
            game_buttons.remove(switch_button_2)
            portals_lvl1.add(win_1)
            level = 1

    if level == 1.5:
        screen.fill((47,59,56))
        screen.blit(level_complete_1,level_complete_1_rect)
        buttons.empty()
        buttons.add(Next)
        buttons.draw(screen)
        buttons.update(event)
        Next_2_clicked = False

    if level == 2:
        if help_activated == True and Next_2_clicked == False:
            buttons.empty()
            help_group.empty()
            if help_group.has(help2) == False:
                help_group.add(help2)
            if buttons.has(Next2) == False:
                buttons.add(Next2)

            help_group.draw(screen)  
            buttons.draw(screen)
            buttons.update(event)
        else:    
            buttons.empty()
            help_group.empty()
            screen.fill(dark_purp)
            if game_buttons.has(switch_button_1):
                game_buttons.remove(switch_button_1)
            if game_buttons.has(switch_button_3) == False and happened == 0:
                game_buttons.add(switch_button_3)

            level2_group.draw(screen)
            portals_lvl2.draw(screen)
            saws.draw(screen)
            game_buttons.draw(screen)
        
            if player_group.has(player) == False:
                player_group.add(player)

            if portals_lvl2.has(portal5,portal6) == False and happened == 0:
                portals_lvl2.add(portal5,portal6)        

            if portals_lvl2.has(win_2) == False:
                portals_lvl2.add(win_2)      

            if player.collide_with_colour(screen, dark_purp, (137, 108)):
                deaths += 1
                if portals_lvl2.has(portal5,portal6) == False:
                    portals_lvl2.add(portal5,portal6)

            if collision('box8'):
                portals_lvl2.remove(portal5,portal6)            
            if player.collide_with_colour(screen, (217,206,0), (183, 641)) and collision('box8'):
                portals_lvl2.remove(portal5,portal6)

            if player.collision_enemy(saws,(137, 108)):
                happened = 0
                if portals_lvl2.has(portal5,portal6,portal7) == False:
                    portals_lvl2.add(portal5,portal6,portal7)      

            if player.collision(game_buttons, 'button_3'):
                player.position_change((100, 140))
                portals_lvl2.empty()
                level2_group.empty()
                Next_2_clicked = False
                level = 2.1
            
            if player.collide_with_colour(screen, green_win, (122, 100)):
                level = 2.5
                player_group.remove(player)
                level2_group.empty()
                portals_lvl2.empty()
                game_buttons.empty()

            player_group.draw(screen)
            player_group.update()
            saws.update()
            if paused:
                buttons.empty()
                pause_group.draw(screen)
                pause_screen.draw_text(screen)

                if control_state == 1:
                    if buttons.has(arrow2) == False:
                        buttons.add(arrow2)
                    if buttons.has(wasd2):
                        buttons.remove(wasd2)
                else:  
                    if buttons.has(wasd2) == False:
                        buttons.add(wasd2)
                    if buttons.has(arrow2):
                        buttons.remove(arrow2) 
                buttons.draw(screen)
                for button in buttons:
                    button.update(event)

    if level == 2.1:
        if help_activated == True and Next_2_clicked == False:
            buttons.empty()
            help_group.empty()
            if help_group.has(help3) == False:
                help_group.add(help3)
            if buttons.has(Next2) == False:
                buttons.add(Next2)

            help_group.draw(screen)  
            buttons.draw(screen)
            buttons.update(event)
        else:  
            screen.fill(teal)  

            if level2_group.has(box9) == False:
                level2_group.add(box9)
                reset_enemies()
            if portals_lvl2.has(portal8) == False:
                portals_lvl2.add(portal8)

            level2_group.draw(screen)
            enemies.draw(screen)
            portals_lvl2.draw(screen)

            if player.collide_with_colour(screen, teal, (100, 140)):
                deaths += 1
                level = 2
                portals_lvl2.remove(portal8)
                level2_group.remove(box9)
                portals_lvl2.add(portal5,portal6,portal7)
                game_buttons.add(switch_button_3)
                level2_group.add(box6,box7,box8)

            if player.collision_enemy(enemies,(110, 140)):
                level = 2
                portals_lvl2.remove(portal8)
                level2_group.remove(box9)
                portals_lvl2.add(portal5,portal6,portal7)
                game_buttons.add(switch_button_3)
                level2_group.add(box6,box7,box8)

            if player.collide_with_colour(screen, pink, (851, 93)):
                level = 2
                check1 = 1
                portals_lvl2.remove(portal8)
                level2_group.remove(box9)
                game_buttons.remove(switch_button_3)
                level2_group.add(box6,box7,box8)

            player_group.draw(screen)

            player_group.update()
            enemies.update()
            if paused:
                buttons.empty()
                pause_group.draw(screen)
                pause_screen.draw_text(screen)

                if control_state == 1:
                    if buttons.has(arrow2) == False:
                        buttons.add(arrow2)
                    if buttons.has(wasd2):
                        buttons.remove(wasd2)
                else:  
                    if buttons.has(wasd2) == False:
                        buttons.add(wasd2)
                    if buttons.has(arrow2):
                        buttons.remove(arrow2) 
                buttons.draw(screen)
                for button in buttons:
                    button.update(event)      

    if level == 2.5:
        screen.fill((47,59,56))
        screen.blit(level_complete_2,level_complete_2_rect)
        buttons.empty()
        if buttons.has(Continue) == False:
            buttons.add(Continue)
        buttons.draw(screen)
        buttons.update(event)

    if level == 3:
        if player_group.has(player) == False:
            player_group.add(player)
        
        if level3_group.has(box10) == False:
            level3_group.add(box10)

        buttons.empty()
        screen.fill((dark_blue))
        level3_group.draw(screen)
        doors.draw(screen)

        if player.hit_door(doors, 'sub_level_1'):
            #player.position_change((100, 140))
            doors.update()
 
        if door_triggered is None:
            hit_door = player.hit_door(doors)
            if hit_door:
                door_triggered = hit_door
        
        if door_triggered  and door_triggered.animation_done:
            level = door_triggered.change_level
            level3_group.empty()
            door_triggered = None

        doors.update()
        player_group.draw(screen)
        player_group.update()

    if level ==3.1:
        screen.fill((dark_blue))
        if level3_group.has(box11) == False:
            player.position_change((449, 96))
            level3_group.add(box11)

        level3_group.draw(screen)
        player.collide_with_colour(screen, black, (449, 96))

        player_group.draw(screen)
        player_group.update()

    if level ==3.2:
        screen.fill((dark_blue))
        if level3_group.has(box12) == False:
            player.position_change((722, 638))
            level3_group.add(box12)

        level3_group.draw(screen)
        player.collide_with_colour(screen, black, (722, 638))

        player_group.draw(screen)
        player_group.update()

    if level ==3.3:
        screen.fill((dark_blue))
        if level3_group.has(box13) == False:
            player.position_change((91,200))
            level3_group.add(box13)            

        level3_group.draw(screen)
        player.collide_with_colour(screen, black, (91,200))

        player_group.draw(screen)
        player_group.update()

    if level == 4:
        screen.fill(swamp_green)
        screen.blit(game_complete,game_complete_rect)

        buttons.empty()
        if buttons.has(save) == False:
            elapsed_time = max(1, elapsed_time)
            base_score = (200 - elapsed_time) * 100 
            penalty = deaths * 250 
            score = max(0, base_score - penalty)  

            buttons.add(save, Continue2)

        buttons.draw(screen)
        buttons.update(event)

    if level >= 1 and start_time is None:
        start_time = int(pygame.time.get_ticks() / 1000)
        timer_running = True

    if level >= 1 and timer_running:
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
    else:
        current_time = elapsed_time

    if level >= 1 and increased == False:
        master_vol = 0.5
        bg_music.set_volume(master_vol)
        if looped == False:
            bg_music.play(loops = -1)
            looped = True
        #bg_music.set_volume(master_vol)

    # renders onto the screen the players coordinates
    font = pygame.font.Font(None, 36)  
    position_text = font.render(f"X: {player.rect.x}, Y: {player.rect.y}", True, (255, 255, 255))
    screen.blit(position_text, (1110, 10))



    pygame.display.update()
    clock.tick(60)
