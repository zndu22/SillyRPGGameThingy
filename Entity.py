from constants import *
import random

class Entity():

	def __init__(self, sprite, position, name, world):
		self.positionX = position[0]
		self.positionY = position[1]
		self.name = name
		self.id = None
		
		self.sprite = sprite

		self.world = world
	
	def Update(self, world):
		pass
	
	def getPosition(self):
		return (self.positionX, self.positionY)

	def setPosition(self, position):
		if position in self.world.entityPosMap:
			print(f"Invalid position, Tile Occupied.  Position: {position}  Entity: {self.name}  tick: {self.world.ticks}") #? potentially messes up pathfinding in the characters
			return -1
		
		del self.world.entityPosMap[self.getPosition()]
		
		self.positionX = position[0]
		self.positionY = position[1]

		self.positionX = max(0, min(self.positionX, self.world.worldMap.rows   ))
		self.positionY = max(0, min(self.positionY, self.world.worldMap.columns))

		self.world.entityPosMap[self.getPosition()] = self