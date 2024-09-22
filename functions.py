from character import Characters
player_name = None

def introductions():
    global player_name
    print("¡Bienvenidos aventurero! Adéntrate en un mundo lleno de misteriosas mazmorras, donde la valentía y la estrategia son tus mejores aliados. ¡Forja tu leyenda enfrentando a peligrosos enemigos y conquistando cada nivel de las mazmorras!")
    player_name = input('¿Como es tu nombre?')
    print(f'¡Bienvenido {player_name}!')

def character_introduction():
    guerrero = Characters(type='Guerrero')
    mago = Characters(type='Mago')
    arquero = Characters(type='Arquero')
    orco = Characters(type='Orco')

def character_creator():
    type = input('Elige los personajes: ')
    for i in range(1,3):
        if type == '1':
            
