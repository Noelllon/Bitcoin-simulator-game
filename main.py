import save
import cards
import shelve
with shelve.open('aCoins') as pc:
  pbitcoins = pc["Bitcoins"]
  pcoins = pc["Coins"]
  pgcards = pc["gcards"]
  print(f"inventory: {pgcards}")
  print(f"You have: {pcoins} Coins and: {pbitcoins} bitcoins")

while True:
  print("what do you want to do?")
  print("(S)tats \n(U)pgrades \n(Ex)Change \n(I)nventory \n(Sa)ve \n(M)ine bitcoins")
  wtd = input().lower()
  if wtd.startswith('m'):
    tomine_time = input("how many times do you wanna mine (only numbers)")
    cards.tomine = tomine_time
    cards.mine()
  elif wtd.startswith('ex'):
    with shelve.open('aCoins') as pc:
      pbits = pc["Bitcoins"] * 1243
      pc["Coins"] += pbits
      pc["Bitcoins"] = 0
  elif wtd.startswith("s"):
    with shelve.open('aCoins') as pc:
      pbitcoins = pc["Bitcoins"]
      pcoins = pc["Coins"]
      pgcards = pc["gcards"]
      print(f"inventory: {pgcards}")
      print(f"You have: {pcoins} Coins and: {pbitcoins} bitcoins")


