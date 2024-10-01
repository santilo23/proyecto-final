from abilities import Golpeo
from abilities import ability_chooser
from enemies import Enemies

class Characters:
    def __init__(self, name = "" , type = "", health=int(0), armor=int(0), level=1):
        self.name = name
        self.type = type
        self.health = health
        self.armor = armor
        self.level = level
        self.exp = 0
        self.abilities = [Golpeo, ability_chooser(type), ability_chooser(type)] #3 habilidades, 2 al azar y una predeterminada

    def levelup(self, level=1): #Hay que agregar mas niveles, subir la vida, si el nivel sube 
        if self.exp >= 100:
            level += 1
        #Subir vida y subir escudo
        
    def experience(self, exp=0): #Nivel de experiencia sube a medida que derrotamos enemigos (en progreso)
        pass

    def __repr__(self):  # Representación de características
        return f"Name: {self.name}, Type: {self.type}, Health: {self.health}, Armor: {self.armor}, Level: {self.level}"

class Warrior(Characters):
    def __init__(self, name=""):
        super().__init__(name, type="Guerrero", health=150, armor=100, level=1)
        self.abilities = [Golpeo, ability_chooser(self.type), ability_chooser(self.type)]  
    
    def __repr__(self):
        return "Un **Guerrero** es un luchador fuerte y hábil en combate cuerpo a cuerpo."

class Magician(Characters):
    def __init__(self, name=""):
        super().__init__(name, type="Mago", health=80, armor=30, level=1)
        self.abilities = [Golpeo, ability_chooser(self.type), ability_chooser(self.type)]
    
    def __repr__(self):
        return "Un **Mago** es un maestro de las artes arcanas, usando poderosos hechizos." 

class Orco(Characters):
    def __init__(self, name=""):
        super().__init__(name, type="Orco", health=200, armor=50, level=1)
        self.abilities = [Golpeo, ability_chooser(self.type), ability_chooser(self.type)]
    
    def __repr__(self):
        return "Un **Orco** es una criatura enorme y brutal, con gran fuerza física."

class Knight(Characters):
    def __init__(self, name=""):
        super().__init__(name, type="Caballero", health=130, armor=120, level=1)
        self.abilities = [Golpeo, ability_chooser(self.type), ability_chooser(self.type)]
    
    def __repr__(self):
        return "Un **Caballero** es un guerrero honorable y bien entrenado, experto en combate con espada."

class Archer(Characters):
    def __init__(self, name=""):
        super().__init__(name, type="Archer", health=90, armor=40, level=1)
        self.abilities = [Golpeo, ability_chooser(self.type), ability_chooser(self.type)]
    
    def __repr__(self):
        return "Un **Arquero** es un combatiente ágil y preciso, experto en ataques a distancia."

