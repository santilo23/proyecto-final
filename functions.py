from character import Characters
import time
import random

player_name = None
player_character1 = None
player_character2 = None
player_character3 = None
player_progress = 0
dungeon_progress = 0

def introductions():
    global player_name
    print("¡Bienvenidos aventurero! Adéntrate en un mundo lleno de misteriosas mazmorras, donde la valentía y la estrategia son tus mejores aliados. ¡Forja tu leyenda enfrentando a peligrosos enemigos y conquistando cada nivel de las mazmorras!")
    time.sleep(3)
    player_name = input('¿Como es tu nombre?')
    time.sleep(3)
    print(f'¡Bienvenido {player_name}!')

def character_introduction():
    guerrero = Characters(type = 'Guerrero')
    mago = Characters(type = 'Mago')
    arquero = Characters(type = 'Arquero')
    orco = Characters(type = 'Orco')
    caballero = Characters(type = 'Orco')
    
def character_creator():
    type = input('Elige los personajes: ')

            

