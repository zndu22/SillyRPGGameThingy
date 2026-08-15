from __future__ import annotations
from constants import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from Entities.Character import Character

class Brain():

	def __init__(self, character: Character):
		self.character = character
	
	def think(self):
		pass