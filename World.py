from __future__ import annotations
from constants import *
import random

from WorldMap import WorldMap
from Entities.Entity import Entity
from CharacterStats import CharacterStats
from Entities.Character import Character
from Brains.Brain import Brain

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from typing import List

#Handles the world and all the Entities in it.
class World():

	def __init__(self):
		self.worldMap = WorldMap()
		self.worldMap.generateTilemap()

		self.ticks = 0

		self.entities: list[Entity] = []
		self.entityPosMap = [[[] for _ in range(self.worldMap.rows)] for _ in range(self.worldMap.columns)]

	def Update(self):
		# self.spawnBadGuy()
		# self.spawnGuy()
		
		for i in self.entities:
			i.Update()
		
		self.ticks += 1

	def addEntity(self, sprite, position, name=None):
		if position in self.entityPosMap:
			print(f"Cannot create Entity, Tile Occupied.  Position: {position}  tick: {self.ticks}")
			return
		self.entities.append(Entity(sprite, position, name, self))
		self.UpdateArrays(self.entities[-1])
		return self.entities[-1]

	def addCharacter(self, sprite, position, stats, name=None):
		if position in self.entityPosMap:
			print("Cannot create Entity, Tile Occupied")
			return
		self.entities.append(Character(sprite, position, name, stats, Brain(), self))
		self.UpdateArrays(self.entities[-1])
		return self.entities[-1]

	def getEntitiesAtPos(self, pos):
		return self.entityPosMap[pos[0]][pos[1]]

	def getEntitiesInRadius(self, pos, radius=1, tagMask: List[str]=[], inclusive=False):
		arr: List[Entity] = []
		for i in range(pos[0] - radius, pos[0] + radius + 1):
			for j in range(pos[1] - radius, pos[1] + radius + 1):
				for k in self.getEntitiesAtPos((i, j)): arr.append(k)
		arr.sort(key=lambda x: distance(self.getPosition(), x.getPosition())) # I think this should sort entites by distance
		# set(x).isdisjoint(y) returns true if x and y have no elements in common
		if inclusive: # if the mask is inclusive, meaning it only returns entities with those tags,
			arr = [i for i in arr if not set(i.tags).isdisjoint(tagMask)] # Then return all entities with any of those tags
		else:
			arr = [i for i in arr if set(i.tags).isdisjoint(tagMask)] # Otherwhise, return all the entities without those tags
		return arr 

	def UpdateArrays(self, entity):
		if entity.name == None: entity.name = f"entity{len(self.entities)}"
		if entity.id   == None: entity.id   = len(self.entities)

		self.getEntitiesAtPos(entity.getPosition()).append(entity)
		#self.entityPosMap[entity.positionX][entity.positionY].append(entity)