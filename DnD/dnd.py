
from random import randint
import operator
from race import Race

    ### Determines character stats using 5th Edition method ###

class Character:
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
        'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    
    


    def __init__(self, name):
        self.name = name
        self.class_name = self.chooseClass()
        self.race = Race()
        self.rolls = []
        self.scores = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                   'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0,}
        
        self.rollStats()
        self.assignScores()
        
        
        
        
        self.modifiers = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                   'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0,}
        self.getMods()
        self.printStats()
    
    def chooseClass(self):
        
        classes = self.classes
        
        while True:
            classChoice = input('Please select a class: ')
            if classChoice.capitalize() in classes:
                return classChoice
            else:
                print('Please select a valid class.')
    
    
                     
            
                
                

    def assignScores(self):
        
        scores = self.scores
        rolls = self.rolls
        
        for k,v in list(scores.items()):
            print(f"Assign a score for {k}: ")
            print(rolls)
            while True:

                choice = int(input())
                if choice in rolls:
                    rolls.remove(choice)
                    break
                else:
                    print('Please select a valid score.')
                    print(rolls)

            scores[k] = choice 
        

    def rollStats(self):
        value = []
        for i in range(6):
            for i in range(4):
                roll = [randint(1,6)]
                value.append(roll.pop())
            value.remove(min(value))
            self.rolls.append(sum(value))
            value.clear()
            self.rolls.sort()
            
        

    # Adds race modifiers to Ability Scores if applicable
    def getAbilityScore(self, ability):
        return self.scores[ability] + self.race.getRaceAdjustments(ability)


    ### prints Race, Class, ability scores, and modifiers
    def printStats(self):
        
        #for k, v in self.scores.items():
        #print(f'{k} is {v}')
        print(f'Your race is {self.race}')
        print(f"You're class is {self.class_name.capitalize()}")
        print(self.modifiers)
        for k, v in self.scores.items():
            print(f'{k} is {v + Race.getRaceAdjustments(k)}')

        
    ### determines modifiers            
    def getMods(self):
        for k, v in self.scores.items():
            mod = -4
            score = 3
            while score < 20:
                if v <= score:
                    self.modifiers[k] = mod
                    score = 21
                else:
                    mod += 1
                    score += 2


### call this subclass to generate ability scores, determine race and class
class RandomCharacter(Character):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.race = Race()
        self.scores = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                   'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0,}
        self.scores['Strength'] = self.getRoll()
        self.scores['Dexterity'] = self.getRoll()
        self.scores['Constitution'] = self.getRoll()
        self.scores['Intelligence'] = self.getRoll()
        self.scores['Wisdom'] = self.getRoll()
        self.scores['Charisma'] = self.getRoll()
        self.getClass()
        self.modifiers = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0,
                   'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0,}
        self.getMods()

### Rolls 4 d6, removes lowest value and prints out total. ###
    def getRoll(self):
            value = []
            for i in range(4):
                roll = [randint(1,6)]
                value.append(roll.pop())
            value.remove(min(value))
            return sum(value)


### uses results of getRoll() to determine best class based on ability score           
    def getClass(self):
        s = sorted(self.scores.items(), key = lambda x:x[1])
        
        primary = s[-1][0]
        secondary = s[-2][0]

        if primary == 'Constitution':
            if secondary == 'Strength':
                self.class_name = 'Barbarian'
            elif secondary == "Intelligence":
                self.class_name = 'Sorcerer'
            else:
                self.class_name = 'Barbarian'
        
        
        elif primary == 'Charisma':
            if secondary == 'Intelligence':
                self.class_name = 'Bard'
            elif secondary == 'Strength':
                self.class_name = 'Paladin'
            else:
                self.class_name = 'Bard'
        
        
        elif primary == 'Wisdom':
            if secondary == 'Charisma':
                self.class_name = 'Cleric'
            elif secondary == 'Dexterity':
                self.class_name = 'Druid'
            else: 
                self.class_name = 'Cleric'
        
        elif primary == 'Strength':
            if secondary == 'Constitution':
                self.class_name = 'Fighter'
            elif secondary == 'Dexterity':
                self.class_name = 'Ranger'
            else:
                self.class_name = 'Fighter'
        
        elif primary == 'Dexterity':
            if secondary == 'Wisdom':
                self.class_name = 'Monk'
            elif secondary == 'Charisma':
                self.class_name = 'Rogue'
            else:
                self.class_name = 'Monk'

       
        elif primary == 'Intelligence':
            if secondary == 'Constitution':
                self.class_name = 'Warlock'
            elif secondary == 'Wisdom':
                self.class_name = 'Wizard'
            else:
                self.class_name = 'Warlock'


    ### Chooses a random race
    def randomRace(self):
        self.race = randint(0,len(Race.races)- 1)
        return Race.races[self.race]

