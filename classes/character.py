class Character:
    LUCK_EF = [{"name": "double damage"}, {"name": "armour pierce"}, {"name": "lifesteal"}]

    def __init__(self, name, str, cons, skl):
        self.name = name
        self.strength = str
        self.constitution = cons
        self.skill = skl
        self.luck = 0

    def __str__(self):
        return "Name:{} Strength: {} Constitution: {} Skill: {} Luck: {}".format(self.name, self.strength, self.constitution, self.skill, self.luck)

    def __repr__(self):
        pass

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
        if dmg["defence"]:
            self.hp -= dmg["effects"] - self.df
        else:
            self.hp -= dmg["effects"]

    def check_death(self):
        if self.hp <= 0:
            return True
        return False

    def recover(self, heal_amount):
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def physical_attack(self):
        return (self.calc_luck_effect(self.atk))

    def calc_luck_effect(self, dmg):
        # { "name": "armour piece", "effects": dmg , "defence": False},
        # if effect == "double damage":
        #     return { "name": "double damage", "effects": (dmg * 2), "defence": True }
        return {"name": "default", "effects": dmg, "defence": True}
