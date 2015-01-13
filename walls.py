import pygame, math, random

class Wall():
	def __init__(self, side, height, speedy=1):
		# Bottom Right
		self.image = "Art/Wall/wall"+str(random.randint(1,2))+".png"
		if self.side == "right":
			self.image = pygame.transform.flip(self.image, 0, 1) #or 1,0 if it is wrong
		self.rect = self.image.get_rect()
		self.speedx = 0
		self.speedy = speedy
		self.speed = [self.speedx, self.speedy]
		self.place(pos)#left off here
		self.didBounceX = False
		self.didBounceY = False
		self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
		self.living = True
		
	def place(self, pos):
		self.rect.center = pos
