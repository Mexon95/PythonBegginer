import random

flipping = random.randint(0, 1)

if flipping == 1:
    side_coin = "Heads";
else:
    side_coin = "Tails";

print(side_coin)