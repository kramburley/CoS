import CoS

def test_setPlayerName():
    player = CoS.Player("Mark")
    assert player.name == "Mark"

def test_setPlayerBasicStuff():
    player = CoS.Player("Rafa", 2,2,3)
    assert player.name == "Rafa"
    assert player.strength == 2
    assert player.constitution == 2
    assert player.skill == 3
