from __future__ import annotations
from constants import *
from typing import TYPE_CHECKING
from random import randint

from Actions.Action import Action

if TYPE_CHECKING:
    from Entities.Character import Character

class Rest(Action):

    def __init__(self, character: Character):
        super().__init__(character)
        self.ticksPerHeal = 5
        self.tickCounter = 0

    def start(self):
        self.character.pathfinder.haltPath()
    
    def update(self):
        if self.tickCounter >= self.ticksPerHeal: 
            self.character.Heal(1)
            self.character.state["stamina"] += 1
            self.tickCounter = 0
        else:
            self.tickCounter += 1
        if self.character.state["health"] >= self.character.characterStats.getMaxHealth():
            self.isFinished = True # Trigger finished if the character is fully healed is finished

    def end(self):
        pass

    def getUtility(self):
        return (-1 * math.sqrt(self.character.state["health"]/self.character.characterStats.getMaxHealth)) + 1