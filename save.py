import shelve

with shelve.open("aCoins") as pc:
  pcoins = pc["Coins"]