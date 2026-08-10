import pygame
from constants import *

from World import World

class Input():

	def __init__(self):
		self.keys = None

		# some flags or something, IDK how else to do it.
		self.QuitProgram = False
		self.isDragging = False
		self.mouseMotion = (0, 0)

	def updateInputs(self, world: World):
		self.keys = pygame.key.get_pressed()
		self.mouseMotion = pygame.mouse.get_rel() 

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.QuitProgram = True

			# Drag middle mouse to move camera
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 2:  # 2 is Middle Click
					self.isDragging = True
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 2:
					self.isDragging = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					world.spawnGuy()
				if event.key == pygame.K_SPACE:
					world.Update()
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

		if self.isDragging:
			camera.moveCamera(self.mouseMotion)