import random
from abilities import Golpeo 
from abilities import ability_chooser

class Enemies:
    def __init__(self, name, difficulty, health):
        self.name = name
        self.difficulty = difficulty
        self.health = health

enemies_easy = [
    Enemies(name="Rata de las Sombras", difficulty="easy", health=50),
    Enemies(name="Goblin de las Cavernas", difficulty="easy", health=55),
    Enemies(name="Mimic de Bolsillo", difficulty="easy", health=50),
    Enemies(name="Esqueleto Roto", difficulty="easy", health=55),
    Enemies(name="Murciélago Vampírico", difficulty="easy", health=50)
]

enemies_intermediate = [
    Enemies(name="Guerrero Espectral", difficulty="intermediate", health=65),
    Enemies(name="Lobo Sombrío",difficulty="intermediate", health=70),
    Enemies(name="Mago Corrupto", difficulty="intermediate", health=65),
    Enemies(name="Gólem de Piedra", difficulty="intermediate", health=70),
    Enemies(name="Serpiente de Fuego", difficulty="intermediate", health=65)
]

enemies_hard = [
    Enemies(name="Serafín Caído", difficulty="hard", health=80),
    Enemies(name="Mago Corrupto", difficulty="hard", health=80),
    Enemies(name="Arconte de las Sombras", difficulty="hard", health=85),
    Enemies(name="Demonio del Vacío", difficulty="hard", health=80)
]

bosses = [
    Enemies(name="Dragón de la Oscuridad Eterna", difficulty="boss", health=100),
    Enemies(name="Destructor de Mundos", difficulty="boss", health=105),
    Enemies(name="El Primordial Olvidado", difficulty="boss", health=115),
    Enemies(name="Avatar del Apocalipsis", difficulty="boss", health=120),
    Enemies(name="Emperador del Inframundo", difficulty="boss", health=150)
]

def random_enemy(difficulty):
    enemy = None 
    if difficulty == 'easy':
        enemy = random.choice(enemies_easy)
    elif difficulty == 'intermediate':
        enemy = random.choice(enemies_intermediate)
    elif difficulty == 'hard':
        enemy = random.choice(enemies_hard)
    else: 
        enemy = random.choice(bosses)
    return enemy

