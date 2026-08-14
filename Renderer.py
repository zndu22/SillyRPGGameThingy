import pygame
from constants import *
import math

from World import World
from Camera import Camera
from Character import Character
from Input import Input

class Renderer():

	def __init__(self, inputs: Input):
		self.screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.RESIZABLE)
		self.icon = pygame.image.load("assets/icon.png")
		pygame.display.set_icon(self.icon)
		self.inputs = inputs

		convertTextures()
	
	def RenderFrame(self, world: World, camera: Camera):
		self.screen.fill((0, 0, 0))
		self.blit(world.worldMap.tilemap, camera.getPosition())

		self.blit(assets["cursor"], self.toScreenSpace(world, camera, self.inputs.mouseWorldPos))

		for i in world.entities:
			tile = world.getEntitiesAtPos(i.getPosition())
			if len(tile) == 1: 
				self.blit(i.sprite, self.toScreenSpace(world, camera, i.getPosition()))
			else: # brace yourself, this next part isn't pretty
				lvl = math.ceil(math.sqrt(len(tile))) # find the closest square all the guys can fit in
				scale = int(tileWidth/lvl) # find the scale those guys need to be to fit
				sp = self.toScreenSpace(world, camera, i.getPosition()) # find the offset each guy needs to be at
				sp = addTuples(sp, ((tile.index(i)%lvl) * scale, math.floor(tile.index(i)/lvl) * scale)) # add the guy's location
				self.blit(pygame.transform.scale(i.sprite, (scale, scale)), sp) # and finally, draw the guy.
				# I apoligize to anyone who had to read that.
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