from constants import *
import random

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from typing import List

class Entity():

	def __init__(self, sprite, position, name, world):
		self.positionX = position[0]
		self.positionY = position[1]
		self.name = name
		self.id = None
		self.tags: List[str] = [] # Used to identify what type of entity it is.
		# For example, Heroes will have a 'hero' tag, while structures will have a 'structure'.
		# Some structures might have an 'impassiable' tag. This info would be checked by the pathfinder in this example.
		
		self.sprite = sprite

		self.world = world

	def __str__(self):
		return f"{self.name} at position: {self.getPosition()}."
	
	def Update(self):
		pass
	
	def getPosition(self):
		return (self.positionX, self.positionY)

	def setPosition(self, position):
		self.world.getEntitiesAtPos(self.getPosition()).remove(self)
		
		self.positionX = position[0]
		self.positionY = position[1]

		self.positionX = max(0, min(self.positionX, self.world.worldMap.rows   ))
		self.positionY = max(0, min(self.positionY, self.world.worldMap.columns))

		self.world.getEntitiesAtPos(self.getPosition()).append(self)