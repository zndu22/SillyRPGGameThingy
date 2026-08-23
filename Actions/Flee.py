from __future__ import annotations
from constants import *
from typing import TYPE_CHECKING
from random import randint

from Actions.Action import Action

if TYPE_CHECKING:
    from Entities.Character import Character

class Flee(Action):

    def __init__(self, character: Character):
        super().__init__(character)
        self.ticksPerMove = 4
        self.ticksPerSprinting = 2
        self.tickCounter = 0

    def start(self):
        # Pathfind away
        self.character.pathfindTo((randint(-20, 20), randint(-20, 20)))
    
    def update(self):
        if self.tickCounter >= self.ticksPerSprinting if self.character.state["stamina"] > 0 else self.ticksPerMove: # sprint when possible
            if self.character.state["stamina"] > 0:
                 self.character.state["stamina"] -= 1
            self.character.Move(self.character.pathfinder.nextMove(self.character.getPosition()))
        else:
            self.tickCounter += 1
        if self.character.pathfinder.finishedPath():
                    self.isFinished = True # Trigger finished if the path is finished

    def end(self):
        pass # halt path and clean up

    def getUtility(self):
        return (-1 * math.sqrt(self.character.state["health"]/self.character.characterStats.getMaxHealth)) + 1 # Same as rest, just for now.