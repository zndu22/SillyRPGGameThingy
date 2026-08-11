import pygame
from constants import *
import math

from World import World
from Camera import Camera
from CharacterStats import CharacterStats

class Input():

	def __init__(self, world: World, camera: Camera):
		self.keys = None

		# some flags or something, IDK how else to do it.
		self.QuitProgram = False
		self.isDragging = False
		self.mouseMotion = (0, 0)

		self.world = world
		self.camera = camera

	def updateInputs(self):
		self.keys = pygame.key.get_pressed()
		self.mouse = pygame.mouse.get_pressed()
		self.mousePos = pygame.mouse.get_pos()
		self.mouseMotion = pygame.mouse.get_rel() 

		if self.keys[pygame.K_g]:
			self.world.spawnGuy()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.QuitProgram = True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					tgtPos = ( math.floor((self.mousePos[0] - self.camera.positionX)/tileWidth) , math.floor((self.mousePos[1] - self.camera.positionY)/tileHeight) )
					self.world.addCharacter(assets['guy'], tgtPos, CharacterStats(10))
				if event.button == 2:  # 2 is Middle Click
					self.isDragging = True
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 2:
					self.isDragging = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					self.world.spawnGuy()
				if event.key == pygame.K_SPACE:
					self.world.Update()
				if event.key == pygame.K_ESCAPE:
					self.QuitProgram = True

	def MoveCamera(self, speed, dt):
		dp = [0, 0]
		if self.keys[pygame.K_UP]:
			dp[1] += 1
		if self.keys[pygame.K_DOWN]:
			dp[1] -= 1
		if self.keys[pygame.K_LEFT]:
			dp[0] += 1
		if self.keys[pygame.K_RIGHT]:
			dp[0] -= 1

		self.camera.moveCamera(tuple(i * speed * dt for i in dp))

		if self.isDragging:
			self.camera.moveCamera(self.mouseMotion)