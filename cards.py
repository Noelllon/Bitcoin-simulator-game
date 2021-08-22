import shelve
import time
global bitcoins
global tomine
bitcoins = 0
class Cards:   # cards in the game
  rustycard = 0.0001

with shelve.open('aCoins') as pc:
  pbitcoins = pc["Bitcoins"]
  pgcards = pc["gcards"]
  e_pgcards = pc["egcards"] = Cards.rustycard

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