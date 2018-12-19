import random
from classes.game import Game
import pygame
# luck_effects = [{"name": "double damage", "effect_key": 1}, {"name": "armour pierce", "effect_key": 2}, {"name": "lifesteal", "effect_key": 3}]
#
# print(random.choice(luck_effects)["effect_key"])
"""
'''
Name: Mark
HP: 10/10
MP: 6/6
Physical Attack: 15
Defence: 2
==============================
Enemy Stats:
Name: Rafa
HP: 16/16
MP: 8/8
Physical Attack: 8
Defence: 4
'''
player = Player("Mark", 5, 2, 3)
player.update_attibutes()
enemy = Player("Rafa", 4,4,2)
enemy.update_attibutes()


items_to_display = ["name", "hp", "mp", "atk", "df"]
stats = ["Player Stats", "Enemy Stats"]
combatants = [player, enemy]

for i in range(len(combatants)):
    print(stats[i])
    for item in items_to_display:
        if item in ["mp", "hp"]:
            print("{}: {}/{}".format(item.upper(), getattr(combatants[i],item), getattr(combatants[i],"max_" + item)))
        else:
            print("{}: {}".format(item.upper(), getattr(combatants[i],item)))
    print("==============================")
"""

# Game.generate_random_player()

print(pygame.ver)
