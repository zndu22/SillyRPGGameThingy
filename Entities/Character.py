from __future__ import annotations
from constants import *
import random

from Entities.Entity import Entity
from Pathfinder import Pathfinder

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from CharacterStats import CharacterStats
	from World import World 


class Character(Entity):
	
	def __init__(self, sprite, position, name, stats: CharacterStats, world: World):
		super().__init__(sprite, position, name, world)

		self.characterStats: CharacterStats = stats
		self.HP = self.characterStats.maxHealth
		self.validTiles = [grassColor, mountianColor]

		self.pathfinder = Pathfinder(self.world, self.validTiles)
		self.targetTile = position
		
	def Damage(self, health):
		self.HP -= health

	def Heal(self, health):
		self.HP += health

	def Move(self, dp):
		targetPos = addTuples(self.getPosition(), dp)
		if self.world.worldMap.getPixel(targetPos[0], targetPos[1]) in self.validTiles:
			self.setPosition(targetPos)

	def pathfindTo(self, target):
		self.targetTile = target

		if not self.pathfinder.path:
			self.pathfinder.findPath(
				self.getPosition(),
				target
			)
		dp = self.pathfinder.nextMove()
		if dp is not None:
			self.Move(dp)
	
	def Update(self):
		pass # re-write all your garbagre code please... it sucked.
		# No, I'm gonna put it in the monster and hero classes when I write them.
		# okay, how're those gonna look?
		
		# Okay so, I'll have three Character types. NPCs, Monsters, and Heroes.
		# NPCs will just wander around the town, I'll add them last.
		# Monsters will spawn at a monster hideout or something and wander around the world, attacking heroes and NPCs.
		# And Heroes will be adventuring, hunting monsters, and leveling up their skills and gear, ect.

		# Each will have their own 'brain', that will determine how they behave. They will also have their own Stats, which will determine how the brain thinks.
		# I'll use a utility based AI that uses specific skills and attributes to determine what to do next.
		# For example: Two different heroes are both low on HP and in combat. One has a higher strength and Attack stat, so they'll continue fighting,
		# While the other with lower stats will flee.

		# Monsters and NPCs will also have their own stats, but will not think as much on what to do. NPCs will just wander and flee combat.
		# While Monsters will wander and look for combat.

		# ---| What needs to be done in the future? |---
		# -> Create a 'brain' class for Monsters and Heroes, just for testing.
		# -> Impliment combat between two characters.
		# -> Impliment inventories and equietment.
		# -> Impliment skills and xp
		# -> Potentially, re-write the A* code so I understand it better.