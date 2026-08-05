from constants import *
import random

from Entity import Entity
from CharacterStats import CharacterStats
from Pathfinder import Pathfinder

class Character(Entity):
	
	def __init__(self, sprite, position, name, stats:CharacterStats, world):
		super().__init__(sprite, position, name, world)

		self.characterStats:CharacterStats = stats
		self.HP = self.characterStats.maxHP
		self.validTiles = [grassColor, mountianColor]

		self.pathfinder = Pathfinder(self.world, self.validTiles)
		
	def Damage(self, health):
		self.HP -= health

	def Heal(self, health):
		self.HP += health

	def Move(self, dp):
		targetPos = addTuples(self.getPosition(), dp)
		if self.world.worldMap.getPixel(targetPos[0], targetPos[1]) in self.validTiles:
			self.setPosition(targetPos)

	def pathfindTo(self, target):
		if not self.pathfinder.path:
			self.pathfinder.findPath(
				self.getPosition(),
				target
			)
		dp = self.pathfinder.nextMove()
		if dp is not None:
			self.Move(dp)
	
	def Update(self, world):
		# self.move((random.randint(-1, 1), random.randint(-1, 1)))
		if self.pathfinder.hasPath(): return
		targetPos = addTuples(self.getPosition(), (random.randint(-10, 10), random.randint(-10, 10)))
		if self.world.worldMap.isOutOfBounds(targetPos): return
		if self.world.worldMap.getPixel(targetPos[0], targetPos[1]) in self.validTiles:
			self.pathfindTo(targetPos)