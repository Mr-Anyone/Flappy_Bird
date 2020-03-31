from Variables import *
import pygame
from os import path
import random
import time


WIDTH = 640
HEIGHT = 980
image_folder = path.join(path.dirname(__file__), 'Images')
bird_images = [path.join(image_folder, 'DP.png'), path.join(image_folder, 'MD.png'), path.join(image_folder, 'UP.png')]
posx = []
posy = []
for x in range(100):
    posx.append(x)
    posy.append(x)


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # All the variable
        self.original = pygame.image.load(bird_images[0])
        self.image = self.original
        self.rect = self.image.get_rect()

        #The init pos
        self.rect.center = (90, HEIGHT/2)

        self.fall = True
        self.flap = False

        #Random variable
        self.draw_count = 0
        self.stime = 0
        self.etime = 0
        self.angle = 0

        # This is for the jumping settings
        self.vel = 9
        self.fvel = 0
        self.tvel = self.vel - self.fvel

    def draw(self):
        self.draw_count += 1
        if self.draw_count == 0:
            self.image = pygame.image.load(bird_images[0]).convert()
            self.original = pygame.image.load(bird_images[0]).convert()

        if self.draw_count == 1:
            self.image = pygame.image.load(bird_images[1]).convert()
            self.original =pygame.image.load(bird_images[1]).convert()

        if self.draw_count == 2:
            self.image = pygame.image.load(bird_images[2]).convert()
            self.original =  pygame.image.load(bird_images[2]).convert()
            self.draw_count = 0

    def move(self):
        self.tvel = self.vel - self.fvel

        if self.fvel >0:
            self.fvel -= 0.1
        else:
            self.fvel = 0
        self.rect.y += self.tvel


    def rotate(self, angle, x, y):
        self.x, self.y = x,y
        self.angle = angle
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if restart[0] == 0:
            self.draw() # This would draw the bird animation

            key = pygame.key.get_pressed()
            if self.etime - self.stime >= 0.3:
                if key[pygame.K_SPACE]:
                    self.stime = time.time()
                    self.fvel += 5

            self.move()


            # Border of the bird
            if self.rect.bottom < -5:
                lmao[0] = 1
            if self.rect.top > HEIGHT +5:
                lmao[0] = 1

            # This is the rotation
            if self.tvel <0 :
                self.angle += 2
                self.rotate(self.angle, self.rect.centerx, self.rect.centery)

            elif self.tvel >0:
                self.angle -= 2
                self.rotate(self.angle, self.rect.centerx, self.rect.centery)

            # This is the max angle
            if self.angle < - 30:
                self.angle = -30
            if self.angle > 30:
                self.angle = 30

            if restart[1] == 1:
                self.kill()

            # Time pause for brid flap
            self.etime = time.time()








class Up_Pipe(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(image_folder, 'Down_Pipe.png')).convert()

        self.rect = self.image.get_rect()
        self.top = 0
        self.right = 0

        self.rect.center = (WIDTH + 600,10)
        self.x = x


    def information(self, top, right):
        self.top = top
        self.right = right
        return self.top, self.right

    def update(self):
        self.rect.right = posx[self.x]
        self.rect.bottom = posy[self.x]
        if restart[1] == 1:
            self.kill()


class Down_Pipe(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(image_folder, 'up_pipe.png')).convert()
        self.rect = self.image.get_rect()

        self.vel = 3
        self.x = x
        self.once = True
    def update(self):
        global score, restart
        if restart[0] == 0:
            if self.once:
                self.rect.y = random.randint(400,800)
                self.rect.x = WIDTH + self.x * 300
                posy[self.x] = self.rect.top - 200
                posx[self.x] = self.rect.right
                self.once = False

            if self.rect.left < -70:
                self.rect.x = WIDTH + 300
                self.rect.y = random.randint(400, 800)
                scores = score[0]
                score[0] = scores + 1

            self.rect.right -= self.vel
            posy[self.x] = self.rect.top - 200
            posx[self.x] = self.rect.right
        if restart[0] == 1:
            self.vel = 0
        if restart[1] == 1:
            self.kill()
