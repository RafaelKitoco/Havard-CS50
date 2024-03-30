from random import choice, randint, shuffle

coin = choice(["heads", "tails"])
print(coin)
nun = randint(1, 10)
print(nun)
cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)