from __future__ import annotations
from constants import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entities.Character import Character

class Action():

    def __init__(self, character: Character):
        self.isFinished = False
        self.character: Character = character

    def start(self):
        pass

    def update(self):
        pass

    def finish(self):
        if not self.isFinished:
            self.isFinished = True
        self.end()

    def end(self):
        pass

    def getUtility(self):
        return 0.0