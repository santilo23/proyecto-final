from enemies import random_enemy

class Dungeons:
    def __init__(self, name = "", enemies = None):
        self.name = name
        if enemies is None:
            self.enemies = []
        else:
            self.enemies = enemies


dungeon1 = Dungeons("Las Catacumbas del Olvido", [random_enemy("easy"), random_enemy("easy"), random_enemy("easy"), random_enemy("intermediate"), random_enemy("boss")])
dungeon2 = Dungeons("Fortaleza de la Sombra Eterna", [random_enemy("easy"), random_enemy("intermediate"), random_enemy("intermediate"), random_enemy("hard"), random_enemy("boss")])
dungeon3 = Dungeons("Cueva de los Ecos Perdidos", [random_enemy("intermediate"), random_enemy("intermediate"), random_enemy("hard"), random_enemy("hard"), random_enemy("boss")])
dungeon4 = Dungeons("Templo de las Almas Errantes", [random_enemy("intermediate"), random_enemy("hard"), random_enemy("hard"), random_enemy("hard"), random_enemy("boss")])
dungeon5 = Dungeons("Cripta del Dragón Durmiente", [random_enemy("hard"), random_enemy("hard"), random_enemy("hard"), random_enemy("hard"), random_enemy("boss")])