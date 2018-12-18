class Player():
    LUCK_EF = [{"name": "double damage"}, {"name": "armour pierce"}, {"name": "lifesteal"}]

    def __init__(self, name, str, cons, skl):
        self.name = name
        self.strength = str
        self.constitution = cons
        self.skill = skl
        self.luck = 0

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
        self.hp -= (dmg[0] - self.df) + dmg[1]

    def check_death(self):
        if self.hp <= 0:
            return True
        return False

    def recover(self, heal_amount):
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def physical_attack(self):
        return (self.atk, self.calc_luck_effect())

    def calc_luck_effect(self):
        effect = Player.LUCK_EF[0]["name"]
        if effect == "double damage":
            return self.atk
        return 0
