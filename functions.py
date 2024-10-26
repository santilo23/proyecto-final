from character import Characters, Warrior, Magician, Archer, Orco, Knight
import time
import random
from dungeons import * #Importe la mazmorras, asi empezamos el juego y armar el sistema de ataque
from enemies import random_enemy
from abilities import enemy_abilities
from CONSTANTES import * #Importe todas las variables constantes 
from items import Item, items_list

player_name = None
player_progress = 0 #Progreso del jugador 
dungeon_progress = 0 #Progeso de la mazmorra actual
list_character = [] 
player1 = None
player2 = None
player3 = None
current_dungeon = None

def introductions(): #Primero imprimos la introduccion al juego
    global player_name
    print(BIENVENIDA)
    time.sleep(3)
    player_name = input('¿Como es tu nombre?')
    time.sleep(3)
    print(SALUDO + player_name)

def character_introduction(): #Presentamos los personajes a elegir 
    print(WARRIOR) 
    time.sleep(2)
    print(MAGICIAN)
    time.sleep(2)
    print(ORCO)
    time.sleep(2)
    print(KNIGHT)
    time.sleep(2)
    print(ARCHER)
    time.sleep(2)
    
def character_creator(): #Creamos los 3 personajes
    global player_name, list_character, player1, player2, player3

    available_characters = ['guerrero', 'mago', 'arquero', 'orco', 'caballero'] 
    contador = 0
    i = 0
    while contador < 3:
        for character in available_characters:
            print(character.capitalize(), end=' / ')
        character_choose = input(f'\nElige que personaje vas a utilizar: ').lower()
        if character_choose in available_characters:
            if character_choose == 'guerrero':
                list_character.append(Warrior())
            elif character_choose == 'mago':
                list_character.append(Magician())
            elif character_choose == 'arquero':
                list_character.append(Archer())
            elif character_choose == 'orco':
                list_character.append(Orco())
            elif character_choose == 'caballero':
                list_character.append(Knight())
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
    global current_dungeon #mazmorra actual

    dungeons = [dungeon1, dungeon2, dungeon3, dungeon4, dungeon5] #Colocamos en una lista las 5 mazmorras
    current_dungeon = dungeons[player_progress] 
    dungeon_progress = int(0)
    print(f"¡Bienvenido a la mazmorra: {current_dungeon.name}!")
    time.sleep(2)

    while dungeon_progress < 5:  
        if dungeon_progress == 4:
            print("¡Has llegado al jefe final!")
            enemy = current_dungeon.enemies[4]
            character_attack(enemy)
            player_progress += 1
            current_dungeon = dungeons[player_progress]
            print(f"¡Bienvenido a la mazmorra: {current_dungeon.name}!")
        else:
            enemy = current_dungeon.enemies[dungeon_progress]
            print(f"Nivel {dungeon_progress + 1}: {enemy.name}")
            time.sleep(3)
            character_attack(enemy)
    print("¡Has completado todas las mazmorras!")
    time.sleep(3)

def player_abilities_chooser(player):
    i = 0
    for abilitie in player.abilities:
        print(f"{i+1} - {player.abilities[i].name}, Daño: {player.abilities[i].damage}")
        i += 1
    
    while True:
        try:
            choice = int(input('Ingrese la habilidad que desees: '))
            if choice == 1:
                return player.abilities[0]
            elif choice == 2:
                return player.abilities[1]
            elif choice == 3:
                return player.abilities[2]
            else:
                print("Esta opción no está disponible, vuelve a intentarlo")
            time.sleep(2)
            break
        except ValueError:
            print('Debes ingresar un numero valido entre 1-3')
            return player_abilities_chooser(player)
    
def character_chooser():
    global list_character, player1, player2, player3, current_dungeon
    i = 1

    for character in list_character:
        print(f'{i}- Personaje: {character.type}, Health: {character.health}, Armor: {character.armor}')
        i += 1

    while True:
        try:
            choice = int(input('Elige el Heroe con el que deseas atacar: '))
            if choice == 1: 
                return player1
            elif choice == 2:
                return player2
            elif choice == 3:
                return player3
            else:
                print(OPTION)
            break    
        except ValueError:
            print('Debes ingresar un numero valido entre 1-3')
            return character_chooser()
        
def enemy_drop_item():
    drop_chance = random.random()  # Valor entre 0.0 y 1.0
    if drop_chance > 0.7:  # 30% de probabilidad de dejar caer un ítem
        dropped_item = random.choice(items_list)
        return dropped_item
    
    return None
        
def character_attack(enemy):
    global player1, player2, player3, player_progress, dungeon_progress, player, current_dungeon
    enemy_health = enemy.health 
    
    while list_character is not None and enemy_health > 0:
        player = character_chooser()
        if player is None:
            return character_chooser()
        else: 
            pass
        print(f'Enemigo: {enemy.name}, Salud: {enemy_health}')

        player_attack = player_abilities_chooser(player) #Seleccionar la habilidad del jugador 
        if player_attack is None:
            return player_abilities_chooser(player)
        else:
            pass
        print(f'Ataque elegido: {player_attack.name}')
        time.sleep(2)

        enemy_attack = random.choice(enemy_abilities) #Selecionar las habilidades del enemigo
        print("3... 2... 1...")
        time.sleep(2)

        player_damage = player_attack.damage #Ataque de jugador
        enemy_health -= player_damage  
        print(ATAQUE)
        time.sleep(2)

        print("El enemigo responde con:", enemy_attack.name) #Ataque enemigo
        enemy_damage = enemy_attack.damage 

        if player.armor > 0:
            if enemy_damage <= player.armor:
                player.armor -= enemy_damage  # El daño solo afecta a la armadura
                net_damage = 0
                print(f"La armadura absorbió todo el daño. Armadura restante: {player.armor}")
            else:
                net_damage = enemy_damage - player.armor  # El daño restante afecta a la vida
                print(f"La armadura absorbió {player.armor} de daño.")
                player.armor = 0  # La armadura se agota
                player.health -= net_damage  # El daño restante se resta de la salud
                print(f"Daño restante que afectó la salud: {net_damage}")
        else:
            # Si no hay armadura, el daño va directo a la salud
            player.health -= enemy_damage
            print(f"Daño recibido: {enemy_damage}")

        time.sleep(2)
        

        # Verificar si el jugador o el enemigo han sido derrotados
        if player.health <= 0:
            print(f"{player.name} ha sido derrotado.")
            list_character.remove(player)  # Eliminar al jugador de la lista si es derrotado
            if not list_character:  # Si no quedan jugadores
                print(GAME_OVER)
                break

        if enemy_health <= 0:
            print(f"¡El enemigo {enemy.name} ha sido derrotado!") 
            print(f"Has ganado {enemy.experience_reward} exp")

            exp_reward = enemy.experience_reward
            for player in list_character:
                player.gain_experience(exp_reward)

            dropped_item = enemy_drop_item()
            if dropped_item:
                print(f"¡El enemigo dejó caer un {dropped_item.name}!")
                dropped_item.apply_item(player)

            dungeon_progress += 1 #Sumamos 1 cada vez que derrotamos a un enemigo 1 de 5
            if dungeon_progress < 5: 
                print(f"Progreso en la mazmorra: {dungeon_progress + 1} de 5")
                time.sleep(3) 
            else:
                print("¡Has completado la mazmorra!")
                time.sleep(2)
                dungeon_progress = 0 #Vuelve a 0 ya que tiene 5 enemegos en la proxima mazmorra
                time.sleep(3)
        
character_creator()
game()