class Player():
    def __init__(self, name, str, cons, skl):
        self.name = name
        self.strength = str
        self.constitution = cons
        self.skill = skl

    def update_attibutes(self):
        self.hp = self.strength * self.constitution
        self.max_hp = self.hp
        self.mp = self.skill * self.constitution
        self.max_mp = self.mp
        self.atk = self.skill * self.strength
        self.df = self.constitution

    def levelup(self, bvalues):
        self.strength = bvalues["str"]
        self.constitution = bvalues["con"]
        self.skill = bvalues["skl"]

    def take_damage(self, dmg):
        self.hp -= (dmg - self.df)

    def check_death(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def recover(self, heal_amount):
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
