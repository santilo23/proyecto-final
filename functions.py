from character import Characters
import time
import random
from dungeons import dungeon1, dungeon2, dungeon3, dungeon4, dungeon5 #Importe la mazmorras, asi empezamos el juego y armar el sistema de ataque
from enemies import random_enemy
from abilities import enemy_abilities

player_name = None
player_progress = 0 
dungeon_progress = 0 #Progreso de mazmorras, empezamos desde 0, por que no hemos completado ninguna de las 5 existentes
list_character = []
player1 = None
player2 = None
player3 = None

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
    caballero = Characters(type = 'Orco')
    time.sleep(2)
    print(guerrero, mago, arquero, orco, caballero) 

def character_creator(): #Creamos los 3 personajes
    global player_name
    global list_character
    global player1
    global player2
    global player3
    available_characters = ['guerrero', 'mago', 'arquero', 'orco', 'caballero']
    contador = 0
    
    while contador < 3:
        for character in available_characters:
            print(character)
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

    player1 = list_character[0]
    player2 = list_character[1]
    player3 = list_character[2]

def game():
    global player_progress #0
    global dungeon_progress #0
    current_dungeon = None #Creamos una nueva variable de mazmorra actual
    
    
    dungeons = [dungeon1, dungeon2, dungeon3, dungeon4, dungeon5] #Colocamos en una lista las 5 mazmorras
    current_dungeon = dungeons[player_progress] 
    dungeon_progress = int(0)
    print(f"¡Bienvenido a la mazmorra: {current_dungeon.name}!")
    time.sleep(2)

    while dungeon_progress < 5:
        if current_dungeon.name == "Las Catacumbas del Olvido":
            enemy = current_dungeon.enemies[dungeon_progress]
            print(f'Nivel {dungeon_progress + 1} : {enemy.name}')
            time.sleep(2)
            character_attack(enemy)
        else: 
            break
def player_abilities_chooser():
    while True:
                print(f'Elige el personaje con el que deseas luchar(número):\n 1-{player1.type}\n 2-{player2.type}\n 3-{player3.type}')
                choice = int(input(''))
                if choice == 1:
                    print(f'Elegiste {player1.type}')
                    print("HABILIDADES: ")
                    print(f"1-{player1.abilities[0].name}, Daño: {player1.abilities[0].damage}")
                    print(f"2-{player1.abilities[1].name}, Daño: {player1.abilities[1].damage}")
                    print(f"3-{player1.abilities[2].name}, Daño: {player1.abilities[2].damage}")
                    choice = int(input("Elige la habilidad que vas a utilizar: "))
        
                    if choice == 1:
                        return player1.abilities[0]
                    elif choice == 2:
                        return player1.abilities[1]
                    elif choice == 3:
                        return player1.abilities[2]
                    else:
                        print("Esta opción no está disponible, vuelve a intentarlo")
                        time.sleep(2)
                elif choice == 2:
                    print(f'Elegiste {player2.type}')
                    print("HABILIDADES: ")
                    print(f"1-{player2.abilities[0].name}, Daño: {player2.abilities[0].damage}")
                    print(f"2-{player2.abilities[1].name}, Daño: {player2.abilities[1].damage}")
                    print(f"3-{player1.abilities[2].name}, Daño: {player2.abilities[2].damage}")
                    choice = int(input("Elige la habilidad que vas a utilizar: "))
        
                    if choice == 1:
                        return player2.abilities[0]
                    elif choice == 2:
                        return player2.abilities[1]
                    elif choice == 3:
                        return player2.abilities[2]
                    else:
                        print("Esta opción no está disponible, vuelve a intentarlo")
                        time.sleep(2)
                elif choice == 3:
                    print(f'Elegiste {player3.type}')
                    print("HABILIDADES: ")
                    print(f"1-{player3.abilities[0].name}, Daño: {player3.abilities[0].damage}")
                    print(f"2-{player3.abilities[1].name}, Daño: {player3.abilities[1].damage}")
                    print(f"3-{player3.abilities[2].name}, Daño: {player3.abilities[2].damage}")
                    choice = int(input("Elige la habilidad que vas a utilizar: "))
        
                    if choice == 1:
                        return player3.abilities[0]
                    elif choice == 2:
                        return player3.abilities[1]
                    elif choice == 3:
                        return player3.abilities[2]
                    else:
                        print("Esta opción no está disponible, vuelve a intentarlo")
                        time.sleep(2)
                else:    
                    break

def character_attack(enemy):
    global player1
    global player2
    global player3
    global list_character
    enemy_health = enemy.health

    while list_character is not None and enemy_health > 0:
        for character in list_character:
            print(f'Personaje: {character.type}, Health: {character.health}, Armor: {character.armor}')
        print(f'Enemigo: {enemy.name}, Salud: {enemy_health}')
        player_attack = player_abilities_chooser()
        print(f'Ataque elegido: {player_attack.name}')
        time.sleep(2)
        enemy_health -= player_attack.damage 
        print(f'{enemy.name}, salud: {enemy_health}')
        time.sleep(2)
        enemy_attack = random.choice(enemy_abilities)
        print(f'{player_attack.name} esta por ser atacado')
        enemy_damage = enemy_attack.damage - player_attack.armor 
        player_attack.health = player_attack.health - enemy_damage
        time.sleep(2)
        break

character_creator()
game()

    