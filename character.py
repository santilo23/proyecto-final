
class Characters:
    def __init__(self, name='', health, strength, armor, level=1, exp=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.armor = armor
        self.level = level
        self.exp = exp

    
    def levelup(self, level=1):
        if self.exp >= 100:
            level += 1
        

    

        
