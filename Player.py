import pygame
 

class PlayerShip():
	def __init__(self, pos):
		#Ship.__init__(self, "images/Player/pballbu.png", [0,0], pos)
		self.image = pygame.image.load("Art/Player/basic spaceship.png")
		#self.facing = "up"
		#self.changed = False
		#self.images = self.upImages
		#self.frame = 0
		#self.maxFrame = len(self.images) - 1
		#self.waitCount = 0
		#self.maxWait = 60*.25
		#self.image = self.images[self.frame]
		self.rect = self.image.get_rect()
		self.maxSpeed = 10
		self.speed = [0,0]
		self.speedx =0
		self.speedy =0
			
	def update(self, width, height):
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
	
	def move(self):
		self.rect = self.rect.move(self.speed)
		
	def collideWall(self, width, height):
		if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				#print "hit xWall"
		if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				#print "hit xWall"
		print self.speedx, self.speedy
	
	
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0
