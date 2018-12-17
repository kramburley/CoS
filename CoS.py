class Player():
    def __init__(self, name, str, cons, skl):
        self.name = name
        self.strength = str
        self.constitution = cons
        self.skill = skl

    def update_attibutes(self):
        self.hp = 10
        self.mp = 6
        self.atk = 15
        self.df = 2
