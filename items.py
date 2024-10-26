class Item:
    def __init__(self, name, effect_type, effect_value):
        self.name = name
        self.effect_type = effect_type 
        self.effect_value = effect_value  

    def apply_item(self, player):
        if self.effect_type == 'permanente':
            if self.name == 'Aumento de Salud':
                player.health += self.effect_value
                print(f"{player.type} ha ganado {self.effect_value} puntos de salud permanentemente.")
            elif self.name == 'Mejora de Armadura':
                player.armor += self.effect_value
                print(f"{player.type} ha ganado {self.effect_value} puntos de armadura permanentemente.")
            else:
                player.armor += self.effect_value
                print(f"{player.type} ha ganado {self.effect_value} puntos de armadura permanentemente.")

        elif self.effect_type == 'consumible':
            if self.name == 'Poción de Curación':
                player.health += self.effect_value
                print(f"{player.type} ha recuperado {self.effect_value} puntos de salud.")
            else:
                player.health += self.effect_value
                print(f"{player.type} ha recuperado {self.effect_value} puntos de salud.")

items_list = [
    Item("Poción de Curación", "consumible", 50),   # Recupera 50 de salud
    Item("Aumento de Salud", "permanente", 20),     # Aumenta permanentemente la salud en 20
    Item("Mejora de Armadura", "permanente", 5),    # Aumenta permanentemente la armadura en 5
    Item("Poción de Energía", "consumible", 30),    # Recupera 30 de salud
    Item("Escudo Protector", "permanente", 10),     # Aumenta la armadura en 10 permanentemente
]
