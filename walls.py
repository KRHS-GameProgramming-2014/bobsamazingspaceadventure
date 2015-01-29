import pygame, math, random

class Wall():
	def __init__(self, side, height, screenSize, speedy=1):
		# Bottom Right
		self.image = "Art/Bg/" + str(random.randint(1,20))+" WALL.PNG"
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


#class Walls():
	#def __init__(speed, screenSize)
