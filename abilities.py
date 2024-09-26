import random

class Abilities:
    def __init__(self, name = "", type = "", damage = float(0)):
        self.name = name
        self.type = type
        self.damage = damage

mage_abilities = [
    Abilities("Bola de Fuego", "Mago", 40),
    Abilities("Rayo de Hielo", "Mago", 30),
    Abilities("Explosión Arcana", "Mago", 50),
    Abilities("Descarga", "Mago", 30),
    Abilities("Toque de Energía", "Mago", 20),
    Abilities("Espejo de Escarcha", "Mago", 40),
    Abilities("Nova Arcana", "Mago", 60)
]

warrior_abilities = [
    Abilities("Ataque Frenético", "Guerrero", 60),
    Abilities("Golpe Definitivo", "Guerrero", 80),
    Abilities("Embate", "Guerrero", 40),
    Abilities("Corte Rápido", "Guerrero", 30),
    Abilities("Ira del Guerrero", "Guerrero", 70),
    Abilities("Ataque Giratorio", "Guerrero", 45),
    Abilities("Embiste", "Guerrero", 55)
]

knight_abilities = [
    Abilities("Lanza de Justicia", "Caballero", 50),
    Abilities("Carga Heroica", "Caballero", 65),
    Abilities("Golpe de Escudo", "Caballero", 35),
    Abilities("Juicio Divino", "Caballero", 70),
    Abilities("Rendición", "Caballero", 50),
    Abilities("Emblema de Valor", "Caballero", 20),
    Abilities("Desafío", "Caballero", 40)
]

archer_abilities = [
    Abilities("Disparo Preciso", "Arquero", 30),
    Abilities("Flecha Venenosa", "Arquero", 20),
    Abilities("Lluvia de Flechas", "Arquero", 45),
    Abilities("Tiro a la Cabeza", "Arquero", 55),
    Abilities("Doble Disparo", "Arquero", 25),
    Abilities("Flecha Explosiva", "Arquero", 60),
    Abilities("Flecha Distorsionante", "Arquero", 40),
]

enemy_abilities = [
    Abilities("Golpe Rápido", "Enemigo", 30),
    Abilities("Ataque Sorpresa", "Enemigo", 25),
    Abilities("Arañazo", "Enemigo", 15),
    Abilities("Mordisco", "Enemigo", 15),
    Abilities("Lanzamiento de Escombros", "Enemigo", 20),
    Abilities("Picotazo", "Enemigo", 20),
    Abilities("Embiste", "Enemigo", 25),
    Abilities("Garras Filosas", "Enemigo", 30),
    Abilities("Aliento Venenoso", "Enemigo", 20),
    Abilities("Ataque Desesperado", "Enemigo", 30),
]

Golpeo = Abilities("Golpeo", "All", 20)

def ability_chooser(character_type):
    ability = None
    if character_type == "Guerrero":
        ability = random.choice(warrior_abilities)
    elif character_type == "Mago":
        ability = random.choice(mage_abilities)
    elif character_type == "Arquero":
        ability = random.choice(archer_abilities)
    else:
        ability = random.choice(knight_abilities)
    return ability