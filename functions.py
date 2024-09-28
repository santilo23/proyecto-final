from character import Characters
import time
import random
from dungeons import dungeon1, dungeon2, dungeon3, dungeon4, dungeon5 #Importe la mazmorras, asi empezamos el juego y armar el sistema de ataque
from enemies import Enemies

player_name = None
player_progress = 0 
dungeon_progress = 0 #Progreso de mazmorras, empezamos desde 0, por que no hemos completado ninguna de las 5 existentes
list_character = []

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
    global list_character
    available_characters = ['guerrero', 'mago', 'arquero', 'orco', 'caballero']
    contador = 0
    
    while contador < 3:
        character_choose = input('Elige que personaje vas a utilizar: ').lower()

        if character_choose in available_characters:
            if character_choose == 'guerrero':
                list_character.append(Characters(name = player_name, type = "Guerrero", health = 100, armor = 50))
            elif character_choose == 'mago':
                list_character.append(Characters(name = player_name, type = "Mago", health = 120, armor = 20))
            elif character_choose == 'arquero':
                list_character.append(Characters(name = player_name, type = "Arquero", health = 90, armor = 30))
            elif character_choose == 'orco':
                list_character.append(Characters(name = player_name, type = "Orco", health = 130, armor = 40))
            elif character_choose == 'caballero':
                list_character.append(Characters(name = player_name, type = "Caballero", health = 90, armor = 50))
            available_characters.remove(character_choose)  # Eliminar el personaje elegido de la lista
            contador += 1        
        else:
            print('Ya lo seleccionaste o no existe')

def game():
    global player_progress #0
    global dungeon_progress #0
    current_dungeon = None #Creamos una nueva variable de mazmorra actual
    
    
    dungeons = [dungeon1, dungeon2, dungeon3, dungeon4, dungeon5] #Colocamos en una lista las 5 mazmorras
    current_dungeon = dungeons[player_progress] 
    dungeon_progress = int(0)
    print(f"¡Bienvenido a la mazmorra: {current_dungeon.name}!")
    time.sleep(2)

        
    
    


