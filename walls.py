import pygame, math, random

class Wall():
    def __init__(self, image, side, height, screenSize, speedy=1):
        # Bottom Right
        self.image = image
        self.rect = self.image.get_rect()
        self.screenSize = screenSize
        if side == "right":
            self.image = pygame.transform.flip(self.image, 1, 0) #or 1,0 if it is wrong
            self.placeRight(height)
        else:
            self.placeLeft(height)
        self.speedx = 0
        self.speedy = speedy
        self.speed = [self.speedx, self.speedy]
        self.living = True
    
    def collideEdge(self):
        if self.rect.bottom > self.screenSize[1]:
            self.living = False
        
    def place(self, pos):
        self.rect.center = pos
        
    def placeRight(self, height):
        pos = [0,0]
        pos[0] = self.screenSize[0]
        pos[1] = height * 100
        self.rect.bottomright = pos
    
    def placeLeft(self, height):
        pos = [0,0]
        pos[0] = 0
        pos[1] = height * 100
        self.rect.bottomleft = pos
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def update(self):
        self.speed = [self.speedx, self.speedy]
        self.move()


class Walls():
    def __init__(self, speed, screenSize):
        self.screenSize = screenSize
        self.speed = speed
        self.walls = []
        self.makeWalls()
        
    def makeWalls(self):
        aWallR = "Art/Bg/" + str(random.randint(2,20))+" WALL.PNG"
        print aWallR
        rightImages = [pygame.image.load(aWallR)]
        rightRects = [rightImages[0].get_rect()]
        rightWidths = [rightRects[0].width]
        leftRects = []
        leftWidths = [self.screenSize[0]]
        count = 0
        while (rightWidths[0] + leftWidths[0] + 68 + 4*2 > self.screenSize[0]): #68 is player width 4 pixels is buffer
            aWallL = "Art/Bg/" + str(random.randint(2,20))+" WALL.PNG"
            count += 1
            if count >= 10:
				sys.exit()
            print "trying", aWallL
            leftImages = [pygame.image.load(aWallL)]
            leftRects = [leftImages[0].get_rect()]
            leftWidths = [leftRects[0].width]
        self.walls += [Wall(rightImages[0], "right", 0, self.screenSize, self.speed), 
                       Wall(leftImages[0], "left", 0, self.screenSize, self.speed)]
        
    def update(self):
        if self.walls[-1].rect.top > 100:
            self.makeWalls()
        for wall in self.walls:
            wall.update()
        
