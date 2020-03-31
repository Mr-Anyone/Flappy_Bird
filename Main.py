import pygame
import os
from Variables import *
from Sprite import *

# There are group of sprite
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
birds = pygame.sprite.Group()

# Putting things inside the group
def start():
    bird = Bird()
    all_sprites.add(bird)
    birds.add(bird)
    for x in range(3):
        down_pipe = Down_Pipe(x)

        all_sprites.add(down_pipe)
        pipes.add(down_pipe)

    for x in range(3):
        up_pipe = Up_Pipe(x)
        all_sprites.add(up_pipe)
        pipes.add(up_pipe)

font = pygame.font.Font('freesansbold.ttf', 40)
def write(texts, x, y):
    written = font.render(texts, True, white)
    written_rect = written.get_rect()
    written_rect.center = (x, y)
    windows.blit(written, written_rect)

start()
while run:
    key = pygame.key.get_pressed()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    windows.blit(background, background_rect)

    # This is the collision
    hit = pygame.sprite.groupcollide(birds, pipes ,False, False)

    # This will update the sprites
    all_sprites.draw(windows)
    all_sprites.update()

    write(("Score: " + str(score[0])), 90 , 40)
    if hit:
        windows.blit(gover_pic, gover_pic_rect)
        write("Restart to play ", WIDTH/2, HEIGHT -40)
        restart[0] = 1

    if lmao[0] == 1:
        windows.blit(gover_pic, gover_pic_rect)
        write("Restart to play ", WIDTH/2, HEIGHT -40)
        restart[0] = 1

    # This would update the console windows
    pygame.display.update()
    pygame.display.flip()


pygame.quit()

