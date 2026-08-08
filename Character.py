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
	
	def Update(self, world):
		# self.move((random.randint(-1, 1), random.randint(-1, 1)))
		if self.pathfinder.hasPath():
			try: self.world.entityPosMap[self.pathfinder.nextPosition()] # if that tile is empty
			except: self.Move(self.pathfinder.nextMove(self.getPosition())) # then move
			return # Then don't try to find a new path
		# If there isn't a path, then...
		targetPos = addTuples(self.getPosition(), (random.randint(-10, 10), random.randint(-10, 10))) # select a random target position
		if self.world.worldMap.isOutOfBounds(targetPos): return # Throw it away if it's not in the world bounds
		if self.world.worldMap.getPixel(targetPos[0], targetPos[1]) in self.validTiles: # and only if it's a valid tile,
			self.pathfindTo(targetPos) # pathfind to that tile
		#! I need to desperately re-write this logic. It sucks lwky (Highkey)

		#? Instead I should:
		# If hasPath(): 
		# 	If nextPos is not empty:
		#		Move(path.nextMove(don't pop)[::-1]) # off to the right
		#		Move(path.nextMove(still don't pop)) # now make the move
		#		Move(-x for x in path.nextMove(Now pop)) # now move back on track
		# 	else: Move(Path.nextMove())

		#! But I can see how this all could still result in some bugs. I need to come up with a better Entity avoidance system.
		#? or I could just allow multiple entities to occupy the same tile? That'd be much easier.
		#! But Then I'd have to do a bunch or refactoring and stuff... I don't wanna
		#? Shut up, you're stupid, and I'm right, just do it.
		#! fine...