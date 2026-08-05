from dataclasses import dataclass
from typing import Tuple

# nessecary for the pathfinder, also graciously provided by Chet Gepeiti
@dataclass
class Node:
	position: Tuple[int, int]

	gCost: float = 0.0
	hCost: float = 0.0

	parent = None

	@property
	def fCost(self):
		return self.gCost + self.hCost