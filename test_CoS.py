from classes.player import Player
from classes.utility import Utility
import pytest


@pytest.fixture
def instantiate_player():
    player = Player("Mark", 5, 2, 3)
    player.update_attibutes()
    yield player
    del player

@pytest.fixture
def instantiate_enemy():
    enemy = Player("Rafa", 4,4,2)
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
    instantiate_player.take_damage((instantiate_enemy.atk,0))
    assert instantiate_player.hp == 4

def test_checkDeath(instantiate_player):
    instantiate_player.take_damage((12, 0))
    isdeath = instantiate_player.check_death()
    assert isdeath == True

def test_healing(instantiate_player):
    instantiate_player.take_damage((5, 0))
    instantiate_player.recover(5)
    assert instantiate_player.hp == 10

def test_checkStartPlayerLuck(instantiate_player):
    assert instantiate_player.luck == 0

def test_winLuckIncreaseDecrease(instantiate_player, instantiate_enemy):
    instantiate_enemy.luck = 7
    instantiate_enemy.take_damage((20, 0))
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
    instantiate_player.luck = 100
    instantiate_enemy.hp = 100
    instantiate_enemy.df = 0
    atk_value, effect_value = instantiate_player.physical_attack()
    print(atk_value, effect_value)
    if Utility.chance_check(instantiate_player.luck):
        instantiate_enemy.take_damage(instantiate_player.physical_attack())
    assert instantiate_enemy.hp == 70
