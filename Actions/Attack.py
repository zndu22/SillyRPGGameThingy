from __future__ import annotations
from constants import *
from typing import TYPE_CHECKING
from random import randint

from Actions.Action import Action

if TYPE_CHECKING:
    from Entities.Character import Character

class Attack(Action):

    def __init__(self, character: Character):
        super().__init__(character)
        self.ticksPerAttack = 5
        self.tickCounter = 0
        self.target: Character

    def start(self):
        # It have to remove itself from the list so it doesn't try attacking itself
        entitiesInRange = self.character.world.getEntitiesInRadius(self.character.getPosition(), 10).remove(self.character)
        self.target = entitiesInRange[0] # Just select the closest one (I think)
    
    def update(self):
        if self.tickCounter >= self.ticksPerAttack: 
            if self.character.canAttack(self.target.getPosition()):
                self.target.Damage(randint(1, 3))
            else:
                self.character.pathfindTo(self.target.getPosition())
            self.tickCounter = 0
        else:
            self.tickCounter += 1
        if self.target.state["Health"] <= 0:
            self.isFinished = True # Trigger finished if the target is dead.
            #? Maybe add a dead state to the FSM? or something like that.

    def end(self):
        pass

    def getUtility(self):
        return 0.5