import shelve
import time
global bitcoins
global tomine
bitcoins = 0
class Cards:   # cards in the game
  rustyandbrokencard = 0.0001
  broken8bitcard = 0.0003

with shelve.open('allCards') as cd:
  cd["card1"] = Cards.rustyandbrokencard
  cd["card2"] = Cards.broken8bitcard

with shelve.open('aCoins') as pc:
  pbitcoins = pc["Bitcoins"]
  pgcards = pc["gcards"]
  e_pgcards = pc["egcards"]


def mine():
  global tomine
  global pbitcoins
  pgcards
  global bitcoins
  counter = 0
  tomine = int(tomine)
  while True:
    counter += 1
    bitcoins += e_pgcards
    print(bitcoins)
    if counter >= tomine:
      with shelve.open('aCoins') as pc:
        pc["Bitcoins"] += bitcoins
        print(f"bitcoins: {pc['Bitcoins']}")
      bitcoins = 0
      time.sleep(2)
      break
    time.sleep(2)

