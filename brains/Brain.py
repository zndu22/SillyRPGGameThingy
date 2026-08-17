from __future__ import annotations
from constants import *

from Actions.Wander import Wander

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from typing import List
	from Entities.Character import Character
	from Actions.Action import Action

class Brain():

	def __init__(self):
		self.character: Character
		self.avalableActions: List[Action] = []
	
	def think(self):
		if not self.character.hasAction():
			self.character.currentAction = Wander(self.character)
			self.character.currentAction.start()

		if self.character.currentAction.isFinished:
			self.character.currentAction = None