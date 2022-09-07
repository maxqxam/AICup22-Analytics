import random
from main import Action
from main import GameState

class MyClass:

    def __init__(self):
        self.dummy = 0

    @staticmethod
    def getAction(view:GameState) -> Action:

        return random.choice(range(0,12))
