from __future__ import annotations
from constants import *
from typing import TYPE_CHECKING
from random import randint

from Actions.Action import Action

if TYPE_CHECKING:
    from Entities.Character import Character

class Wander(Action):

    def __init__(self, character: Character):
        super().__init__(character)

    def start(self):
        if not self.character.pathfinder.hasPath():
            self.character.pathfindTo((self.character.positionX + randint(-10, 10), self.character.positionY + randint(-10, 10)))
    
    def update(self):
        
        self.character.Move(self.character.pathfinder.nextMove(self.character.getPosition())) # Move along the path
        self.isFinished = self.character.pathfinder.finishedPath() # Trigger finished if the path is finished

        super().update()

    def end(self):
        self.character.pathfinder.haltPath()