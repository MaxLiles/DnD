from random import randint

    ### Determines character stats using 5th Edition method ###

class Stats:
    def __init__(self, ability):
        self.ability = ability
   ### Rolls 4 d6, removes lowest value and prints out total. ###
    def getStat(self):
        value = []
        for i in range(4):
            roll = [randint(1,6)]
            value.append(roll.pop())
        value.remove(min(value))
        print(value)
        print(f"Your {self.ability} is {sum(value)}")


            
    
