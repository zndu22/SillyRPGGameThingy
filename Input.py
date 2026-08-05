import pygame
from constants import *

from World import World

class Input():

	def __init__(self):
		self.keys = None

		self.QuitProgram = False

	def updateInputs(self, world: World):
		self.keys = pygame.key.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.QuitProgram = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.QuitProgram = True

	def MoveCamera(self, camera, speed, dt):
		dp = [0, 0]
		if self.keys[pygame.K_UP]:
			dp[1] += 1
		if self.keys[pygame.K_DOWN]:
			dp[1] -= 1
		if self.keys[pygame.K_LEFT]:
			dp[0] += 1
		if self.keys[pygame.K_RIGHT]:
			dp[0] -= 1
		camera.moveCamera(tuple(i * speed * dt for i in dp))