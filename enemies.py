import random

class Enemies:
    def __init__(self, name, difficulty, health, experience_reward):
        self.name = name
        self.difficulty = difficulty
        self.health = health
        self.experience_reward = experience_reward

enemies_easy = [
    Enemies(name="Rata de las Sombras", difficulty="easy", health=50, experience_reward = 50),
    Enemies(name="Goblin de las Cavernas", difficulty="easy", health=55, experience_reward = 50),
    Enemies(name="Mimic de Bolsillo", difficulty="easy", health=50, experience_reward = 50),
    Enemies(name="Esqueleto Roto", difficulty="easy", health=55, experience_reward = 50),
    Enemies(name="Murciélago Vampírico", difficulty="easy", health=50, experience_reward = 50)
]

enemies_intermediate = [
    Enemies(name="Guerrero Espectral", difficulty="intermediate", health=65, experience_reward = 70),
    Enemies(name="Lobo Sombrío",difficulty="intermediate", health=70, experience_reward = 70),
    Enemies(name="Mago Corrupto", difficulty="intermediate", health=65, experience_reward = 70),
    Enemies(name="Gólem de Piedra", difficulty="intermediate", health=70, experience_reward = 70),
    Enemies(name="Serpiente de Fuego", difficulty="intermediate", health=65, experience_reward = 70)
]

enemies_hard = [
    Enemies(name="Serafín Caído", difficulty="hard", health=80, experience_reward = 100),
    Enemies(name="Mago Corrupto", difficulty="hard", health=80, experience_reward = 100),
    Enemies(name="Arconte de las Sombras", difficulty="hard", health=85, experience_reward = 100),
    Enemies(name="Demonio del Vacío", difficulty="hard", health=80, experience_reward = 100)
]

bosses = [
    Enemies(name="Dragón de la Oscuridad Eterna", difficulty="boss", health=100,experience_reward = 120),
    Enemies(name="Destructor de Mundos", difficulty="boss", health=105, experience_reward = 120),
    Enemies(name="El Primordial Olvidado", difficulty="boss", health=115, experience_reward = 120),
    Enemies(name="Avatar del Apocalipsis", difficulty="boss", health=120, experience_reward = 120),
    Enemies(name="Emperador del Inframundo", difficulty="boss", health=150, experience_reward = 120)
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

