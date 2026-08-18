from __future__ import annotations
from constants import *

from Actions.Wander import Wander
from States import States

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from typing import Dict
	from typing import List
	from Entities.Character import Character
	from Actions.Action import Action

class Brain():

	def __init__(self):
		self.character: Character
		self.state = States.Wander

	def setup(self, character: Character):
		self.character = character
		self.actionsPerState: Dict[str, List[Action]] = {
			States.Wander : [],
			States.Combat : [],
			States.Idle : []
		}

	def think(self):
		if not self.character.hasAction(): # if the character has no action,
			# Set the characters current action to the best action (highest utility score) for the current state.
			self.character.currentAction = max(self.actionsPerState[self.state], key=lambda i: i.getUtility)