from classes.character import Character
import random

class Enemy(Character):
    def generateRandomName(list_of_names):
        first = random.choice(list_of_names)
        last = random.choice(list_of_names)
        return "{} {}".format(first, last)
