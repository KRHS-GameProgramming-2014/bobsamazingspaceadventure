import pygame, sys, random
from enemys import EnemyEasy
from Player import PlayerShip
from powerups import PowerUp
from walls import Wall
#from HUD import Text
#from HUD import Score

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height
bg = pygame.image.load("Resources/Object/Background/Sure.png")

bgColor = r,g,b = 200, 0, 200
screen = pygame.display.set_mode(size)
fullscreen = False 
bgImage = pygame.image.load("Resources/Object/Background/Sure.png").convert()
bgImage = pygame.transform.scale (bgImage, (800, 600))
bgRect = bgImage.get_rect()
player = Player([width/20, height/20])

balls = []
balls += [Ball("Resources/Object/Zombie/zombie.png", [4,5], [250, 275])]
