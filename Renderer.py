import pygame
from constants import *

from World import World
from Camera import Camera
from Character import Character

class Renderer():

	def __init__(self):
		self.screen = pygame.display.set_mode((windowWidth, windowHeight))
		self.icon = pygame.image.load("assets/icon.png")
		pygame.display.set_icon(self.icon)

		convertTextures()
	
	def RenderFrame(self, world: World, camera: Camera):
		self.screen.fill((0, 0, 0))
		self.blit(world.worldMap.tilemap, camera.getPosition())

		for i in world.entities:
			self.blit(i.sprite, self.toScreenSpace(world, camera, i.getPosition())) # sorry future me
			if isinstance(i, Character):
				for a, v in enumerate(i.pathfinder.path):
					try:
						pygame.draw.line(self.screen, (255, 0, 0), self.toScreenSpace(world, camera, v), self.toScreenSpace(world, camera, i.pathfinder.path[a+1]), 8)
					except: pass

		pygame.display.flip()
	
	def blit(self, surface, position):
		self.screen.blit(surface, position)

	def toScreenSpace(self, world: World, camera:Camera, pos):
		return tuple(v * (tileWidth, tileHeight)[i] + camera.getPosition()[i] for i, v in enumerate(pos))