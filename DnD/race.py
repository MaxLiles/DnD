from random import randint

### Randomly picks a race for your character
class Race:
    races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
    def __init__(self):
        self.race = randint(0,len(self.races)- 1)

### Has user select character's race
    #def chooseRace(self):
        #for race in self.races:
            #print(f"{race}")
        #print("Choose a race for your character. ")


    ### Chooses a random race
    def getRace(self):
        return self.races[self.race]
    
    def getRaceAdjustments(self, score):
        race = self.getRace()
        if race == 'Dwarf':
            return 2 if score == 'Constitution' else 0
        elif race == 'Elf' or 'Halfling':
            return 2 if score == 'Dexterity' else 0
        elif race == 'Dragonborn':
            if score == 'Strength':
                return 2
            elif score == 'Charisma':
                return 1  
        elif race == 'Human':
           return 1
        elif race == 'Gnome':
            return 2 if score == 'Intelligence' else 0
        elif race == 'Half-Orc':
            if score == 'Strength':
                return 2
            if score == 'Constitution':
                return 1
        elif race == 'Tiefling':
            if score == 'Intelligence':
                return 1
            if score == 'Charisma':
                return 2
        elif race == 'Half-Elf':
            if score == 'Charisma':
                return 2
            if score == 'Dexterity' or score == 'Wisdom':
                return 1 

        return 0    
             









