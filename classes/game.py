# import simplejson as json
import os
from classes.character import Character
import random

class Game:

    START_STATUS_POINTS = 10

    def displayStats(player, enemy):
        items_to_display = ["name", "hp", "mp", "atk", "df"]
        stats = ["Player Stats", "Enemy Stats"]
        combatants = [player, enemy]
        UI = ""
        for i in range(len(combatants)):
            UI += "{}:\n".format(stats[i])
            for item in items_to_display:
                if item in ["mp", "hp"]:
                    UI += "{}: {}/{}\n".format(item.upper(), getattr(combatants[i],item), getattr(combatants[i],"max_" + item))
                else:
                    UI += "{}: {}\n".format(item.upper(), getattr(combatants[i],item))
            if i == 0:
                UI += "==============================\n"
        return UI

    def generate_random_player(name = None):
        if not name:
            name = input("Name yourself: ")
        points = Game.START_STATUS_POINTS
        str = random.randrange(1, points - 2)
        con = random.randrange(1, (points - str) -1)
        skl = points - (str + con)
        newCharacter = Character(name, str,con,skl)
        return newCharacter








class bcolor:
    PURPLE      = '\033[95m'
    BLUE        = '\033[94m'
    GREEN       = '\033[92m'
    YELLOW      = '\033[93m'
    RED         = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

class Persistence:
    def savedata(file, data):
        # Creating directory for saving stuff
        directory = os.path.dirname("assets/")
        if not os.path.exists(directory):
            os.makedirs("assets/")
        if os.path.isfile("assets/" + file) and os.stat("assets/" + file).st_size != 0:
            old_file = open("assets/" + file, "r+")
            data = json.loads(old_file.read())
        else:
            old_file = open("assets/" + file,"w+")

        old_file.seek(0)
        old_file.write(json.dumps(data))

    def load(file):
        if os.path.isfile("assets/" + file) and os.stat("assets/" + file).st_size != 0:
            old_file = open("assets/" + file, "r+")
            data = json.loads(old_file.read())
        else:
            data = []
        return data
