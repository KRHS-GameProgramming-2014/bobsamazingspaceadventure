import pygame, math

class EnemyEasy():
    def __init__(self, speed = [0,0], pos = [0,0]):
        #Art from C-Toy: http://opengameart.org/content/spaceships-drakir
        self.image = pygame.image.load("Art/Enemy/Spaceship-Drakir4.png")
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"
