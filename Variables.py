from os import path
import pygame

run = True

# Display settings
WIDTH = 640
HEIGHT = 980
windows = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird!")


image_folder = path.join(path.dirname(__file__), 'Images')
pygame.init()

# Colors
white = (255,255,255)
black = (0,0,0)

# Other Settings
clock = pygame.time.Clock()
FPS = 60

lmao = [0]
# BG Images
background = pygame.image.load(path.join(image_folder, 'FP_BG.jpg')).convert()
background_rect = background.get_rect()

score = [0]

gover_pic = pygame.image.load(path.join(image_folder, 'gameover.png')).convert()
gover_pic_rect = gover_pic.get_rect()
gover_pic_rect.center = (WIDTH/2, HEIGHT/2)

restart = [0, 0]
