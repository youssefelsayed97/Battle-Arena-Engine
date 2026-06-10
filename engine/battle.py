import random
import time
from config import DELAY, SELF_ATTACK, LOSE, WIN, DRAW


# def determine_winner(player1, player2):
#
#     if player1.health == player2.health:
#         player1.status = DRAW
#         player2.status = DRAW
#         return Battle(player1, player2).fight()
#
#     if player1.health < player2.health:
#         player1.status = LOSE
#         player2.status = WIN
#         return player2
#
#     if player1.health > player2.health:
#         player1.status = WIN
#         player2.status = LOSE
#         return player1


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def fight(self):

        if self.player1 is self.player2:
            return SELF_ATTACK

        if not self.player1.is_alive():
            return self.player2

        if not self.player2.is_alive():
            return self.player1

        players = [self.player1, self.player2]

        # if not any(p.status == LOSE for p in players):

        print(f"Battle Start: {self.player1.name} ⚔ {self.player2.name}")
        time.sleep(DELAY)
        random.shuffle(players)
        r = 1
        while all(p.is_alive() for p in players) and r <= 3: #and (p.status == DRAW or p.status == WIN)
            print(f"Round {r}")
            for _ in range(2):
                attacker, defender = players
                attack_value, defense_value, damage = attacker.attack_(defender)
                if damage == 0:
                    print(f"🛡️ {defender.name} defends {attacker.name}'s attack")
                else:
                    print(f"{attacker.name} attack = {attack_value}\n{defender.name} defense = {defense_value}\n"
                          f"⚔{defender.name} took {damage} damage from {attacker.name}")
                    time.sleep(DELAY)
                    print(f"{attacker.name}     | Health = {attacker.health}\n"
                          f"{defender.name}     | Health = {defender.health}")
                    time.sleep(DELAY)

                # for p in players: # the train() spot
                #     if p.health < 5 and p.health != 0:
                #         result = p.train()
                #         print(f"{p.name} has trained!\n"
                #               f"Health = {result['old_health']} --> {result['new_health']}")
                #         print(result)
                if not defender.is_alive():
                    defender.status = LOSE
                    attacker.status = WIN
                    return attacker
                players.reverse()
            r += 1
            # if r > 3:
            #     print(self.determine_winner(players[0], players[1]))
            #     r = 1
        # print(self.determine_winner(self.player1, self.player2))
        if self.player1.health == self.player2.health:
            self.player1.status = DRAW
            self.player2.status = DRAW
            return None

        # return self.player1 if self.player1.health > self.player2.health else self.player2

        if self.player1.health < self.player2.health:
            self.player1.status = LOSE
            self.player2.status = WIN
            return self.player2

        if self.player1.health > self.player2.health:
            self.player1.status = WIN
            self.player2.status = LOSE
            return self.player1
        # return determine_winner(self.player1, self.player2)
        # else:
        #     return None
