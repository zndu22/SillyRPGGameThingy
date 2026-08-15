from __future__ import annotations
import sys
from pathlib import Path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
# Idk what type of bs this is, but apparently I need it, so whatever I guess.

from constants import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from Character import Character

class Brain():

	def __init__(self, character: Character):
		self.character = character
	
	def think(self):
		pass