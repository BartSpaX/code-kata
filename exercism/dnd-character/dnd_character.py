import random
import math

    
def modifier(ability):
    return math.floor((ability - 10)/2)

class Character:
    def __init__(self):
        self.rolled_abilities = self.__generate_abilities()
        self.strength = self.rolled_abilities[0]
        self.dexterity = self.rolled_abilities[1]
        self.constitution = self.rolled_abilities[2]
        self.intelligence = self.rolled_abilities[3]
        self.wisdom = self.rolled_abilities[4]
        self.charisma = self.rolled_abilities[5]
        self.hitpoints = 10 + modifier(self.constitution)
        

    def __generate_abilities(self):
        rolled_points = []
        for _ in range(6):
            dice_rolls = []
            for _ in range(4):
                dice_rolls.append(random.randint(1,6))
            dice_rolls.remove(min(dice_rolls))
            rolled_points.append(sum(dice_rolls))
        return rolled_points
    
    def ability(self):
        return random.choice(self.rolled_abilities)