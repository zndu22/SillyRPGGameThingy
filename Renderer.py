import pygame
from constants import *
import math

from World import World
from Camera import Camera
from Character import Character

class Renderer():

	def __init__(self):
		self.screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.RESIZABLE)
		self.icon = pygame.image.load("assets/icon.png")
		pygame.display.set_icon(self.icon)

		convertTextures()
	
	def RenderFrame(self, world: World, camera: Camera):
		self.screen.fill((0, 0, 0))
		self.blit(world.worldMap.tilemap, camera.getPosition())

		for i in world.entities:
			tile = world.getEntitiesAtPos(i.getPosition())
			if 1 < len(tile) <= 4:
				scale = int(tileWidth/2)
				sp = self.toScreenSpace(world, camera, i.getPosition())
				sp = addTuples(sp, ((tile.index(i)%2) * scale, math.floor(tile.index(i)/2) * scale))
				self.blit(pygame.transform.scale(i.sprite, (scale, scale)), sp)
			elif 4 < len(tile):
				scale = int(tileWidth/3)
				sp = self.toScreenSpace(world, camera, i.getPosition())
				sp = addTuples(sp, ((tile.index(i)%3) * scale, math.floor(tile.index(i)/3) * scale))
				self.blit(pygame.transform.scale(i.sprite, (scale, scale)), sp)
			else: 
				self.blit(i.sprite, self.toScreenSpace(world, camera, i.getPosition()))
			if isinstance(i, Character):
				if i.pathfinder.hasPath():
					for a, v in enumerate(i.pathfinder.path):
						try:
							pygame.draw.line(self.screen, (255, 0, 0), self.toScreenSpace(world, camera, v), self.toScreenSpace(world, camera, i.pathfinder.path[a+1]), 8)
						# except: pygame.draw.line(self.screen, (255, 0, 0), self.toScreenSpace(world, camera, v), self.toScreenSpace(world, camera, i.getPosition()), 8)
						except: pass

		pygame.display.flip()
	
	def blit(self, surface, position):
		self.screen.blit(surface, position)

	def toScreenSpace(self, world: World, camera:Camera, pos):
		return tuple(v * (tileWidth, tileHeight)[i] + camera.getPosition()[i] for i, v in enumerate(pos))