from __future__ import annotations
from constants import *
import random

from Entities.Entity import Entity
from Pathfinder import Pathfinder
from Brains.Brain import Brain

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from CharacterStats import CharacterStats
	from World import World 
	from Actions.Action import Action


class Character(Entity):
	
	def __init__(self, sprite, position, name, stats: CharacterStats, brain: Brain, world: World):
		super().__init__(sprite, position, name, world)

		self.characterStats: CharacterStats = stats
		self.state = {
			"health" : self.characterStats.getMaxHealth()
		}

		self.brain = brain
		self.brain.character = self
		self.currentAction: Action = None

		
		self.validTiles = [grassColor, mountianColor]

		self.pathfinder = Pathfinder(self.world, self.validTiles)
		self.targetTile = position
		
	def Damage(self, health):
		self.state["health"] -= health

	def Heal(self, health):
		self.state["health"] += health

	def Move(self, dp):
		targetPos = addTuples(self.getPosition(), dp)
		if self.world.worldMap.getPixel(targetPos[0], targetPos[1]) in self.validTiles:
			self.setPosition(targetPos)

	def pathfindTo(self, target):
		self.targetTile = target

		if not self.pathfinder.hasPath():
			self.pathfinder.findPath(self.getPosition(), target)
		dp = self.pathfinder.nextMove()
		if dp is not None:
			self.Move(dp)

	def hasAction(self):
		return not self.currentAction == None
	
	def Update(self):

		self.brain.think()