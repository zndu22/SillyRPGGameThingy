#Handles the world and all the Entities in it.
from constants import *
import random

from WorldMap import WorldMap
from Entity import Entity
from CharacterStats import CharacterStats
from Character import Character


class World():

	def __init__(self):
		self.worldMap = WorldMap()
		self.worldMap.generateTilemap()

		self.ticks = 0

		self.entities: list[Entity] = []
		self.entityPosMap = {}

	def Update(self):
		# self.spawnBadGuy()
		# self.spawnGuy()
		
		for i in self.entities:
			i.Update(self)
		
		self.ticks += 1

	def addEntity(self, sprite, position, name=None):
		if position in self.entityPosMap:
			print(f"Cannot create Entity, Tile Occupied.  Position: {position}  tick: {self.ticks}")
			return
		self.entities.append(Entity(sprite, position, name, self))
		self.UpdateArrays(self.entities[-1])

	def addCharacter(self, sprite, position, stats, name=None):
		if position in self.entityPosMap:
			print("Cannot create Entity, Tile Occupied")
			return
		self.entities.append(Character(sprite, position, name, stats, self))
		self.UpdateArrays(self.entities[-1])
		

	def UpdateArrays(self, entity):
		if entity.name == None: entity.name = f"entity{len(self.entities)}"
		if entity.id   == None: entity.id   = len(self.entities)

		self.entityPosMap[(entity.positionX, entity.positionY)] = entity

	def spawnBadGuy(self):
		tgtPos = (random.randint(0, self.worldMap.columns-1), random.randint(0, self.worldMap.rows-1))
		if self.worldMap.getPixel(tgtPos[0], tgtPos[1]) == mountianColor: self.addCharacter(assets['evilGuy'], tgtPos, CharacterStats(10))
	
	def spawnGuy(self):
		tgtPos = (random.randint(0, self.worldMap.columns-1), random.randint(0, self.worldMap.rows-1))
		if self.worldMap.getPixel(tgtPos[0], tgtPos[1]) == grassColor: self.addCharacter(assets['guy'], tgtPos, CharacterStats(10))