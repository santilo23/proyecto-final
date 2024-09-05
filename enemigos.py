import random 

class Enemigos:
    def __init__(self, nombre, dificultad, salud) -> None:
        self.nombre = nombre
        self.dificultad = dificultad
        self.salud = salud

enemigos_faciles = [
    Enemigos(nombre="Rata de las Sombras", dificultad="fácil", salud=50),
    Enemigos(nombre="Goblin de las Cavernas", dificultad="fácil", salud=55),
    Enemigos(nombre="Mimic de Bolsillo", dificultad="fácil", salud=50),
    Enemigos(nombre="Esqueleto Roto", dificultad="fácil", salud=55),
    Enemigos(nombre="Murciélago Vampírico", dificultad="fácil", salud=50)
]

enemigos_intermedios = [
    Enemigos(nombre="Guerrero Espectral", dificultad="intermedio", salud=65),
    Enemigos(nombre="Lobo Sombrío", dificultad="intermedio", salud=70),
    Enemigos(nombre="Mago Corrupto", dificultad="intermedio", salud=65),
    Enemigos(nombre="Gólem de Piedra", dificultad="intermedio", salud=70),
    Enemigos(nombre="Serpiente de Fuego", dificultad="intermedio", salud=65)
]

enemigos_dificiles = [
    Enemigos(nombre="Serafín Caído", dificultad="dificiles", salud=80),
    Enemigos(nombre="Titán del Caos", dificultad="dificiles", salud=85),
    Enemigos(nombre="Mago Corrupto", dificultad="dificiles", salud=80),
    Enemigos(nombre="Arconte de las Sombras", dificultad="dificiles", salud=85),
    Enemigos(nombre="Demonio del Vacío", dificultad="dificiles", salud=80)
]

enemigos_jefes = [
    Enemigos(nombre="Dragón de la Oscuridad Eterna", dificultad="jefe", salud=100),
    Enemigos(nombre="Destructor de Mundos", dificultad="jefe", salud=105),
    Enemigos(nombre="El Primordial Olvidado", dificultad="jefe", salud=115),
    Enemigos(nombre="Avatar del Apocalipsis", dificultad="jefe", salud=120),
    Enemigos(nombre="Emperador del Inframundo", dificultad="jefe", salud=150)
]

def random_enemigo(dificultad):
    enemigo = None 
    if dificultad == 'facil':
        enemigo = random.choice(enemigos_faciles)
    elif dificultad == 'intermedio':
        enemigo = random.choice(enemigos_intermedios)
    elif dificultad == 'dificil':
        enemigo = random.choice(enemigos_dificiles)
    else: 
        enemigo = random.choice(enemigos_jefes)
    return enemigo

