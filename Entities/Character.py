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

		self.tags.append("Character")

		self.characterStats: CharacterStats = stats
		self.state = { # this is the current physical state of the character,
			"health" : self.characterStats.getMaxHealth()
			# Things like Current Health, Mana, Stamina, ect. will be stored here
		}
		# The state in the brain class is the state of the FSM/utility thingy.
		#! To future me: Don't mix up the two

		self.brain = brain
		self.brain.setup(self)
		self.currentAction: Action = None

		
		self.validTiles = [grassColor, mountianColor] # Tiles the Character can walk on.

		self.pathfinder = Pathfinder(self.world, self.validTiles)
		self.targetTile = position # I don't think this is actually used anywhere yet. Just useful to have I guess.
		
	def Damage(self, health):
		self.state["health"] -= health

	def Heal(self, health):
		self.state["health"] += health

	def Move(self, dp): # offset the Character's current position by dp (delta position)
		targetPos = addTuples(self.getPosition(), dp)
		if self.world.worldMap.getPixel(targetPos[0], targetPos[1]) in self.validTiles:
			self.setPosition(targetPos)

	def canAttack(self, target):
		atkRange = cornerDist # this is a placeholder. Reaplce with main weapon range
		return distance(self.getPosition(), target) < atkRange

	def pathfindTo(self, target): # Tells the pathfinder to create a path to target
		self.targetTile = target

		if not self.pathfinder.hasPath():
			self.pathfinder.findPath(self.getPosition(), target)
		dp = self.pathfinder.nextMove()
		if dp is not None:
			self.Move(dp)

	def hasAction(self):
		return not self.currentAction == None
	
	def Update(self):
		if self.hasAction(): # If we have an action,
			self.currentAction.update() # Do that action

			if self.currentAction.isFinished: # If that action is finished
				self.currentAction.finish() # trigger the cleanup code
				self.currentAction = None # and remove that action
				
		self.brain.think()