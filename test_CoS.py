from classes.character import Character
from classes.utility import Utility
from classes.game import Game
from classes.enemy import Enemy
import pytest


@pytest.fixture
def instantiate_player():
    player = Character("Mark", 5, 2, 3)
    """
    Player Stats:
    Name: Mark
    HP: 10/10
    MP: 6/6
    Physical Attack: 15
    Defence: 2
    """
    player.update_attibutes()
    yield player
    del player

@pytest.fixture
def enemy_names():
    return ["Mark", "Ella", "Corinne"]

@pytest.fixture
def instantiate_enemy():
    enemy = Character("Rafa", 4,4,2)
    """
    Enemy Stats:
    Name: Rafa
    HP: 16/16
    MP: 8/8
    Physical Attack: 8
    Defence: 4
    """
    enemy.update_attibutes()
    yield enemy
    del enemy

def test_setPlayerBasicStuff(instantiate_player):
    assert instantiate_player.name == "Mark"
    assert instantiate_player.strength == 5
    assert instantiate_player.constitution == 2
    assert instantiate_player.skill == 3

def test_genPlayerAttributes(instantiate_player):
    assert instantiate_player.hp == 10
    assert instantiate_player.mp == 6
    assert instantiate_player.atk == 15
    assert instantiate_player.df == 2

def test_updatePlayerAttributes(instantiate_player):
    basic_stat = {
        "str": 4,
        "con": 3,
        "skl": 5
    }
    instantiate_player.levelup(basic_stat)
    assert instantiate_player.strength == 4
    assert instantiate_player.constitution == 3
    assert instantiate_player.skill == 5
    instantiate_player.update_attibutes() #bec change stat
    assert instantiate_player.hp == 12
    assert instantiate_player.mp == 15
    assert instantiate_player.atk == 20
    assert instantiate_player.df == 3

def test_takeDamage(instantiate_player, instantiate_enemy):
    instantiate_player.take_damage(instantiate_enemy.physical_attack())
    assert instantiate_player.hp == 4

def test_checkDeath(instantiate_player):
    instantiate_player.take_damage({"name": "default", "effects": 12, "defence": True})
    isdeath = instantiate_player.check_death()
    assert isdeath == True

def test_healing(instantiate_player):
    instantiate_player.take_damage({"name": "default", "effects": 5, "defence": True})
    instantiate_player.recover(5)
    assert instantiate_player.hp == 10

def test_checkStartPlayerLuck(instantiate_player):
    assert instantiate_player.luck == 0

def test_winLuckIncreaseDecrease(instantiate_player, instantiate_enemy):
    instantiate_enemy.luck = 7
    instantiate_enemy.take_damage({"name": "default", "effects": 20, "defence": True})
    instantiate_player.luck = 22
    Utility.check_winner(instantiate_player, instantiate_enemy)
    assert instantiate_player.luck == 25
    assert instantiate_enemy.luck == 1

def test_percentageChance():
    chance_result = Utility.chance_check(100)
    assert chance_result == True
    chance_result2 = Utility.chance_check(0)
    assert chance_result2 == False

#something to fix
def test_physicalAttack(instantiate_player, instantiate_enemy):
    instantiate_enemy.take_damage(instantiate_player.physical_attack())
    assert instantiate_enemy.hp == 5

def test_luckEffectsDoubleDamage(instantiate_player, instantiate_enemy):
    basic_stat = {
        "str": 10,
        "con": 3,
        "skl": 5
    }
    instantiate_enemy.levelup(basic_stat)
    instantiate_enemy.update_attibutes()
    instantiate_enemy.take_damage({"name": "double damage", "effects": instantiate_player.atk * 2, "defence": True})
    assert instantiate_enemy.hp == 3

def test_checkBasicUI(instantiate_enemy, instantiate_player):
    basicUI = """Player Stats:
NAME: Mark
HP: 10/10
MP: 6/6
ATK: 15
DF: 2
==============================
Enemy Stats:
NAME: Rafa
HP: 16/16
MP: 8/8
ATK: 8
DF: 4
"""
    generated_ui = Game.displayStats(instantiate_player, instantiate_enemy)
    assert generated_ui == basicUI

def test_generateRandomPlayerStats(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "Joseth")
    newPlayer = Game.generate_random_player()
    assert newPlayer.name == "Joseth"
    total_points = newPlayer.strength + newPlayer.constitution + newPlayer.skill
    assert total_points == 10
    assert newPlayer.strength > 0
    assert newPlayer.constitution > 0
    assert newPlayer.skill > 0
    assert newPlayer.luck == 0

def test_generateRandomEnemyNames(enemy_names):
    enemy_Name = Enemy.generateRandomName(enemy_names)
    print(enemy_Name)
    first, last = enemy_Name.split(' ')
    assert first in enemy_Name and last in enemy_Name

def test_generateRandomEnemy(enemy_names):
    enemy_Name = Enemy.generateRandomName(enemy_names)
    newEnemy = Game.generate_random_player(enemy_Name)
    total_points = newEnemy.strength + newEnemy.constitution + newEnemy.skill
    print(newEnemy)
    assert total_points == 10
    assert newEnemy.strength > 0
    assert newEnemy.constitution > 0
    assert newEnemy.skill > 0
    assert newEnemy.luck == 0

def test_actionSelectAttack(monkeypatch): #right/d. Attack
    monkeypatch.setattr('builtins.input', lambda x: )
