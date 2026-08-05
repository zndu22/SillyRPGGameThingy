from constants import *
import random

from Entity import Entity
from CharacterStats import CharacterStats

class Character(Entity):
	
	def __init__(self, sprite, position, name, stats:CharacterStats, world):
		super().__init__(sprite, position, name, world)

		self.characterStats:CharacterStats = stats
		self.HP = self.characterStats.maxHP
	
	def Damage(self, health):
		self.HP -= health

	def Heal(self, health):
		self.HP += health

	def move(self, dp):
		self.setPosition(addTuples(self.getPosition(), dp))
	
	def Update(self, world):
		self.move((random.randint(-1, 1), random.randint(-1, 1)))