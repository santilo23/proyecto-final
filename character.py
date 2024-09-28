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
        

    def is_alive(self):
        return self.armor > 0 or self.health > 0 #Si el escudo es mayor a 0 o la vida el personaje esta vivo

    def receive_damage(self, damage):
        self.armor -= damage
        if self.armor < 0: #Si nos quedamos sin escudo, comienza a restar la vida
            self.health -= damage 

    def levelup(self, level=1): #Hay que agregar mas niveles, subir la vida, si el nivel sube 
        if self.exp >= 100:
            level += 1
        #Subir vida y subir escudo
        
    def experience(self, exp=0): #Nivel de experiencia sube a medida que derrotamos enemigos (en progreso)
        pass

    def __repr__(self): #Caracteristicas de cada personaje(intro)
        description = ""
        if self.type == "Guerrero":
            description = "Un **Guerrero** es un luchador fuerte y hábil en combate cuerpo a cuerpo, usando armas pesadas y gran resistencia física para liderar en batalla."
        elif self.type == "Mago":
            description = "Un Mago es un maestro de las artes arcanas, usando poderosos hechizos para atacar a distancia y controlar el campo de batalla."
        elif self.type == "Orco":
            description = "Un **Orco** es una criatura enorme y brutal, con gran fuerza física pero poca inteligencia. Es temido por su poder destructivo y su resistencia en combate."
        elif self.type == "Caballero":
            description = "Un **Caballero** es un guerrero honorable y bien entrenado, experto en combate con espada y escudo, que defiende a los débiles y lucha con disciplina y valor."
        elif self.type == 'Archer': 
            description = "Un **Arquero** es un combatiente ágil y preciso, experto en atacar a distancia con su arco, aprovechando su velocidad y destreza para golpear desde lejos y evadir ataques."
        return description



