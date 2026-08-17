from __future__ import annotations
import pygame
from constants import *
import math

from CharacterStats import CharacterStats

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from World import World
	from Camera import Camera

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
		self.mouseWorldPos = ( math.floor((self.mousePos[0] - self.camera.positionX)/tileWidth) , math.floor((self.mousePos[1] - self.camera.positionY)/tileHeight) )

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.QuitProgram = True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.world.addCharacter(assets['guy'], self.mouseWorldPos, CharacterStats())
				if event.button == 2:  # 2 is Middle Click
					self.isDragging = True
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 2:
					self.isDragging = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					for i in self.world.getEntitiesInRadius(self.mouseWorldPos, 10): print(f"{i},")
					print("")
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