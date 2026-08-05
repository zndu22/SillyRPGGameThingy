import pygame
from constants import *

from World import World
from Camera import Camera

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
			self.blit(i.sprite, 
							tuple(
								(v * (tileWidth, tileHeight)[i]) + camera.getPosition()[i]
								for i, v in enumerate(i.getPosition()))) #sorry future me


		pygame.display.flip()
	
	def blit(self, surface, position):
		self.screen.blit(surface, position)