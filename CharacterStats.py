from constants import *

class CharacterStats():
	
	def __init__(self, Health=0, Stamina=0, Mana=0, Strength=0, Intelligence=0, Finesse=0, Concentration=0, Precision=0, Agility=0, Defence=0):
		self.stats = {
			"health" : Health, # affects max HP
			"stamina" : Stamina, # affects max Stamina
			"mana" : Mana, # affects max mana

			"strength" : Strength, # affects melee damage calculations
			"intelligence" : Intelligence, # affects magic damage calculations

			"finesse" : Finesse, # affects melee hit chance
			"concentration" : Concentration, # affects magic hit chance
			"precision" : Precision, # affects ranged hit chance. Damage is determined by ammo type and weapon

			"agility" : Agility, # affects speed and encumberence
			"defence" : Defence # affects damage taken
		}
		# I'm thinking of only tracking xp, and determining level solely based on that.
		# I only have 10 skills, and the max skill level would be 10. The character's level is the sum of all their skills, meaning the max character level is 100.

		# only xp is tracked here. Level number is derived from xp, using a formula like: f(x) = 10x^2,
		# This gives an exponential curve, that still doesn't feel like too much of a chore. No "92 is half of 99" shenanigans.
	def getLevel(self, skill):
		return 10 * self.stats[skill] ^ 2

	def addExperience(self, skill, experience):
		self.stats[skill] += experience

	def getMaxHealth(self):
		return 10 + (4 * self.stats["health"])

