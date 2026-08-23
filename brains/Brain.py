from __future__ import annotations
from constants import *

from Brains.States import States
from Actions.Wander import Wander
from Actions.Rest import Rest
from Actions.Attack import Attack
from Actions.Flee import Flee

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
		self.actionsPerState: Dict[str, List[type[Action]]] = {
			States.Wander : [Wander, Rest], # Wander action, Rest action
			States.Combat : [Attack, Flee] 	# Attack action, Flee action
		}

	def think(self):
		if not self.character.hasAction(): # if the character has no action,
			# Set the characters current action to the best action (highest utility score) for the current state.
			actions = [actionType(self.character) for actionType in self.actionsPerState[self.state]]
			self.character.currentAction = max(actions, key=lambda i: i.getUtility())
			self.character.currentAction.start()

	def updateState():
		# manages the FSM. Really just used to determine what situation the character is currently in.
		# It only uses the state to narrow down the avalable actions for the utility part of the AI.
		# For example, you wouldn't want to attack while just wandering around.
		
		# For testing, I'd do:

		# if character.inCombat():
		#	state = States.Combat
		# else:
		# 	state = States.Wander

		# But I need to impliment more actions and combat before I tackle all of that.

		return
	