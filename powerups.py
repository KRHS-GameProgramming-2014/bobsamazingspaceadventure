import pygame, math

class PowerUp():
	def __init__(self, kind, speed = [0,0], pos = [0,0]):
		if kind == "burst shot":
			self.image = pygame.image.load("Art/Powerups/Burst Shot.png")
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
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = -self.speedx
				self.didBounceX = True
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = -self.speedy
				self.didBounceY = True
				
				
	def collidePlayer(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False

