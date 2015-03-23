import pygame, sys, random
from Player import PlayerShip
from walls import Wall
from walls import Walls

#test

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0
screen = pygame.display.set_mode(size)

player = PlayerShip([width/2, height/2])
powerups = []

theWalls =  Walls(5, size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
                 
                 
                 
                 
                 
                 
                 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
                
                

    #if random.randint(0,10*60) == 0:
    #    powerups+=[PowerUp("burst shot", [0, 5], [random.randint(0, width),0])]
    
    theWalls.update()

    player.update(width, height)
    for powerup in powerups:
        powerup.update(width, height)
		

    bgColor = r,g,b
    screen.fill(bgColor)
    
    screen.blit(player.image, player.rect)
    for powerup in powerups:
        screen.blit(powerup.image, powerup.rect)
    for wall in theWalls.walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(45)
