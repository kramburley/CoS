import random

luck_effects = [{"name": "double damage", "effect_key": 1}, {"name": "armour pierce", "effect_key": 2}, {"name": "lifesteal", "effect_key": 3}]

print(random.choice(luck_effects)["effect_key"])
