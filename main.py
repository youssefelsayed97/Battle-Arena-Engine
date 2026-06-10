from models import Player
from engine import Tournament
import time
import config
# CONDITION TO AVOID DUPLICATED NAMES
p1 = Player('ahmed', '100', '100', '100')
p2 = Player('youssef', '100', '100', '100')
p3 = Player('ali', '100', '100', '100')
p4 = Player('amr', '100', '100', '100')
p5 = Player('sayed', '100', '100', '100')
p6 = Player('saad', '100', '100', '100')
p7 = Player('mohamed', '100', '100', '100')
p8 = Player('mostafa', '100', '100', '100')

ps = [p1, p2, p3, p4, p5, p6, p7, p8] # comment i should mark the player as a loser or winner to avoid leting him join the battle again

t = Tournament(ps)

winner = t.start()
time.sleep(config.DELAY)

# print(f"{winner} is the winner!")

