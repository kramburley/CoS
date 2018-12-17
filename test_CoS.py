import CoS
import pytest

@pytest.fixture
def instantiate_player():
    player = CoS.Player("Mark", 5, 2, 3)
    player.update_attibutes()
    yield player
    del player

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

def test_takeDamage(instantiate_player):
    enemy = CoS.Player("Rafa", 4, 4, 2)
    enemy.update_attibutes()
    instantiate_player.take_damage(enemy.atk)
    assert instantiate_player.hp == 4

def test_checkDeath(instantiate_player):
    instantiate_player.take_damage(12)
    isdeath = instantiate_player.check_death()
    assert isdeath == True

def test_healing(instantiate_player):
    instantiate_player.take_damage(5)
    instantiate_player.recover(5)
    assert instantiate_player.hp == 10
