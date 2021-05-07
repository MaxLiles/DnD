from random import randint

    ### Determines character stats using 5th Edition method ###

class Stats:
    def __init__(self, character):
        self.character = character
   ### Rolls 4 d6, removes lowest value and prints out total. ###
    def getStat(self):
      
        score = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                   'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0,}
        for k in score.keys():
            print(k)
            value = []
            for i in range(4):
                roll = [randint(1,6)]
                value.append(roll.pop())
# This is not looping correctly, keeps adding results to value,
            value.remove(min(value))
            print(value)
            print(sum(value))
            score[k] = sum(value)
            
            
               
               
        print(f"{self.character}'s stats are: \n{score}")

            

john = Stats('John')

john.getStat()
