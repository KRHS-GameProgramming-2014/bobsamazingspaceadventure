import pygame, math, random

class Wall():
	def __init__(self, image, side, height, screenSize, speedy=1):
		# Bottom Right
		self.image = image
		self.screenSize = screenSize
		if self.side == "right":
			self.image = pygame.transform.flip(self.image, 0, 1) #or 1,0 if it is wrong
			self.placeRight(height)
		else:
			self.placeLeft(height)
			
		self.rect = self.image.get_rect()
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
		pos[0] = self.screenSize[0]
		pos[1] = height * 100
		self.rect.bottomright = pos
	
	def placeLeft(self, height):
		pos[0] = s0
		pos[1] = height * 100
		self.rect.bottomleft = pos


class Walls():
	def __init__(speed, screenSize)
		rightImages = [pygame.image.load("Art/Bg/" + str(random.randint(1,20))+" WALL.PNG")]
		rightRects = [rightImages[0].get_rect()]
		rightWidths = [rightRects[0].width]
		leftRects = []
		leftWidths = [screenSize[0]]
		while (rightWidths[0] + leftWidths[0] + 68 + 4*2 > screenSize[0]): #68 is player width 4 pixels is buffer
			leftImages = [pygame.image.load("Art/Bg/" + str(random.randint(1,20))+" WALL.PNG")]
			leftRects = [leftImages[0].get_rect()]
			leftWidths = [leftRects[0].width]
		self.walls = []
		self.walls += [Wall(rigthImages[0], "right", 0, screenSize, speedy), Wall(leftImages[0], "left", 0, screenSize, speedy)]
		
	def __init	
		
		
		
