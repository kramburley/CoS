import random

class Utility:
    def check_winner(hero, enemy):
        if hero.check_death():
            #check limit to zero for hero
            hero.luck -= 6
            if hero.luck < 0:
                hero.luck = 0
            enemy.luck += 5
            #check limit luck for enemy
            if enemy.luck > 25:
                enemy.luck = 25
        if enemy.check_death():
            #check limit to zero for enemy
            enemy.luck -= 6
            if enemy.luck < 0:
                enemy.luck = 0
            hero.luck += 5
            #check limit luck for hero
            if hero.luck > 25:
                hero.luck = 25

        #in the future, add gold here and exp....

    def chance_check(percentage):
        if random.randint(1, 100) <= percentage:
            return True
        return False
