from constants import *
import random

class Entity():

	def __init__(self, sprite, position, name, world):
		self.positionX = position[0]
		self.positionY = position[1]
		self.name = name
		self.sprite = sprite
		self.id = None

		self.world = world
	
	def Update(self, world):
		pass
	
	def getPosition(self):
		return (self.positionX, self.positionY)

	def setPosition(self, position):
		if position in self.world.entityPosMap:
			print("Invalid position, Tile Occupied")
			return

		del self.world.entityPosMap[self.getPosition()]
		
		self.positionX = position[0]
		self.positionY = position[1]

		self.positionX = max(0, min(self.positionX, self.world.worldMap.rows   ))
		self.positionY = max(0, min(self.positionY, self.world.worldMap.columns))

		self.world.entityPosMap[self.getPosition()] = self