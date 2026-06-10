import random
import time

from config import SELF_ATTACK
from engine import Battle


class Tournament:
    def __init__(self, players):
        self.players = players

    def show_players(self):
        for i, player in enumerate(self.players, start=1):
            print(f"{i}- {player.name}")

    def start(self):

        if not self.players:
            return "No players in tournament"
        self.show_players()

        if len(self.players) % 2 != 0:
            return "Tournament must be even"

        while len(self.players) > 1:
            winners = [], cheaters = []
            for i in range(0, len(self.players), 2):
                drawAttempts = 0
                matchResult = Battle(self.players[i], self.players[i+1]).fight()
                if matchResult == SELF_ATTACK:
                    print("Skipping this round! cannot fight yourself!")
                    print("We excluded you from the tournament because we think that you are trying to cheat")
                    # remove player from the tournament
                    # cheaters.extend([self.players[i], self.players[i+1]])
                    
                    continue
                if matchResult is not None:
                    winners.append(matchResult)
                    print(f"The Winner is: {matchResult}")
                    continue
                while matchResult is None:
                    print("Draw! Rematch...")
                    matchResult = Battle(self.players[i], self.players[i + 1]).fight()
                    drawAttempts += 1
                    if drawAttempts > 3:
                        matchResult = random.choice([self.players[i], self.players[i+1]])

                winners.append(matchResult)
            self.players = winners
        print(f"The Champion is: {self.players[0]}")


                # if matchResult is None:
                    # draw.extend([self.players[i], self.players[i+1]])
                    # while rematchResult is not None:
                    #     rematchResult = Battle(draw[0], draw[1]).fight()
                    #     if rematchResult is not None:
                    #         winners.append(rematchResult)
                    #         draw.clear()
                    #         break

        # winners = []
        # firstPointer1 = 0
        # lastPointer1 = len(self.players) - 1
        #
        # while len(self.players) > 1:
        #     winnerResult = Battle(self.players[firstPointer1], self.players[lastPointer1]).fight()
        #     if winnerResult == SELF_ATTACK:
        #         print('skipping this round you cannot fight yourself')
        #     if winnerResult is not None:
        #         winners.append(winnerResult)
        #         print(winnerResult.name, winnerResult.status)
        #
        #     firstPointer1 += 1
        #     lastPointer1 -= 1
        #
        #     if firstPointer1 == len(self.players)//2:
        #         self.players = winners
        #         firstPointer1 = 0
        #         lastPointer1 = len(self.players) - 1
        #         print("winners are :")
        #         if len(winners) > 1:
        #             for p in self.players:
        #                 print(p)
        #             winners = []
        #         else:
        #             print(f"The Champion is: {winners[0]}")
        #         time.sleep(3)
        #