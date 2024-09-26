from character import Characters
import time
import random
from dungeons import dungeon1, dungeon2, dungeon3, dungeon4, dungeon5 #Importe la mazmorras, asi empezamos el juego y armar el sistema de ataque
from enemies import Enemies

player_name = None
player_character1 = None #Dejamos vacia la variable del personaje a elegir 
player_character2 = None 
player_character3 = None
player_progress = 0 
dungeon_progress = 0 #Progreso de mazmorras, empezamos desde 0, por que no hemos completado ninguna de las 5 existentes
list_character = [None, None, None]

def introductions(): #Primero imprimos la introduccion al juego
    global player_name
    print("¡Bienvenidos aventurero! Adéntrate en un mundo lleno de misteriosas mazmorras, donde la valentía y la estrategia son tus mejores aliados. ¡Forja tu leyenda enfrentando a peligrosos enemigos y conquistando cada nivel de las mazmorras!")
    time.sleep(3)
    player_name = input('¿Como es tu nombre?')
    time.sleep(3)
    print(f'¡Bienvenido {player_name}!')

def character_introduction(): #Presentamos los personajes a elegir 
    guerrero = Characters(type = 'Guerrero')
    time.sleep(2)
    mago = Characters(type = 'Mago')
    time.sleep(2)
    arquero = Characters(type = 'Arquero')
    time.sleep(2)
    orco = Characters(type = 'Orco')
    time.sleep(2)
    caballero = Characters(type = 'caballero')
    time.sleep(2)
    print(guerrero, mago, arquero, orco, caballero) 

def character_creator(): #Creamos los 3 personajes
    global player_name
    list_character = []
    available_characters = ['guerrero', 'mago', 'arquero', 'orco', 'caballero']
    contador = 0
    
    while True:
        character_choose = input('Elige que personaje vas a utilizar: ').lower()
        if contador == 2:
            break
        elif character_choose in available_characters:
            if character_choose == 'guerrero':
                list_character.append(Characters(name = player_name, type = "Guerrero", health = 100, armor = 50))
                contador += 1
            elif character_choose == 'mago':
                list_character.append(Characters(name = player_name, type = "Mago", health = 120, armor = 20))
                contador += 1
            elif character_choose == 'arquero':
                list_character.append(Characters(name = player_name, type = "Arquero", health = 90, armor = 30))
                contador += 1
            elif character_choose == 'orco':
                list_character.append(Characters(name = player_name, type = "Orco", health = 130, armor = 40))
                contador += 1
            elif character_choose == 'caballero':
                list_character.append(Characters(name = player_name, type = "Caballero", health = 90, armor = 50))
                contador += 1
            available_characters.remove(character_choose)  # Eliminar el personaje elegido de la lista
        else:
            print('Elige un personaje valido')
            
    for character in list_character:
        print(character)

def Game():
    pass

character_creator()
