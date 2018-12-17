import CoS
import pytest

@pytest.fixture
def instantiate_player():
    player = CoS.Player("Mark", 5, 2, 3)
    return player

def test_setPlayerBasicStuff(instantiate_player):
    assert instantiate_player.name == "Mark"
    assert instantiate_player.strength == 5
    assert instantiate_player.constitution == 2
    assert instantiate_player.skill == 3

def test_genPlayerAttributes(instantiate_player):
    instantiate_player.update_attibutes()
    assert instantiate_player.hp == 10
    assert instantiate_player.mp == 6
    assert instantiate_player.atk == 15
    assert instantiate_player.df == 2
