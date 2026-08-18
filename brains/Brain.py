from __future__ import annotations
from constants import *

from Actions.Wander import Wander
from enum import Enum

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from typing import Dict
	from typing import List
	from Entities.Character import Character
	from Actions.Action import Action

class States(str, Enum):
	Wander = "wander"
	Combat = "combat"
	Idle   = "idle"

class Brain():

	def __init__(self):
		self.character: Character
		self.state = States.Wander
		self.actionsPerState: Dict[str, List[Action]] = {
			States.Wander : [Wander(self.character)],
			States.Combat : [],
			States.Idle : []
		}
	
	def think(self):
		if not self.character.hasAction():
			self.character.currentAction = Wander(self.character)
			self.character.currentAction.start()