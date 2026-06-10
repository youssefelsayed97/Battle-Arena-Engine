import random
from config import MAX_ATTACK, MAX_HEALTH, MAX_DEFENSE, DRAW


class Player:

    def __init__(self, name, health, attack, defense, status=None):
        self.name = name
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.status = status

    def __str__(self):
        if not self.is_alive():
            return f"{self.name} is dead!"
        return f"{self.name} | HP: {self.health} | ATK: {self.attack} | DEF: {self.defense} | Status: {self.status}"

    def is_alive(self):
        return self.health > 0

    def train(self):

        if not self.is_alive() or \
                (self.health == MAX_HEALTH and self.attack == MAX_ATTACK and self.defense == MAX_DEFENSE):
            return None

        old_health = self.health
        old_attack = self.attack
        old_defense = self.defense

        self.health = min(MAX_HEALTH, self.health + random.randint(5, 30))
        self.attack = min(MAX_ATTACK, self.attack + random.randint(5, 30))
        self.defense = min(MAX_DEFENSE, self.defense + random.randint(5, 30))

        return {
            "old_health": old_health,
            "new_health": self.health,
            "old_attack": old_attack,
            "new_attack": self.attack,
            "old_defense": old_defense,
            "new_defense": self.defense
        }

    def roll_attack(self):
        attack_value = random.randint(max(1, self.attack // 4), max(1, self.attack // 2))
        return attack_value

    def roll_defense(self):
        defense_value = random.randint(max(0, self.defense // 4), max(1, self.defense // 2))
        return defense_value

    def take_damage(self, final_damage):
        self.health = max(0, self.health - final_damage)

    def attack_(self, defender):
        if not self.is_alive():
            return 0

        attack_value = self.roll_attack()
        defense_value = defender.roll_defense()

        final_damage = max(0, attack_value - defense_value)

        defender.take_damage(final_damage)

        return attack_value, defense_value, final_damage


