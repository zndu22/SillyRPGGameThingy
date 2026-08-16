from __future__ import annotations
from constants import *
import random

from WorldMap import WorldMap
from Entities.Entity import Entity
from CharacterStats import CharacterStats
from Entities.Character import Character

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
		self.entities.append(Character(sprite, position, name, stats, self))
		self.UpdateArrays(self.entities[-1])
		return self.entities[-1]

	def getEntitiesAtPos(self, pos):
		return self.entityPosMap[pos[0]][pos[1]]

	def getEntitiesInRadius(self, pos, radius=1):
		arr = []
		for i in range(pos[0] - radius, pos[0] + radius + 1):
			for j in range(pos[1] - radius, pos[1] + radius + 1):
				for k in self.getEntitiesAtPos((i, j)): arr.append(k)
		return arr 

	def UpdateArrays(self, entity):
		if entity.name == None: entity.name = f"entity{len(self.entities)}"
		if entity.id   == None: entity.id   = len(self.entities)

		self.getEntitiesAtPos(entity.getPosition()).append(entity)
		#self.entityPosMap[entity.positionX][entity.positionY].append(entity)