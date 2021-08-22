import shelve


with shelve.open('allCards') as cd:
  card1 = cd["card1"]
  card2 = cd["card2"]


def in_shop():
  print("here's where you buy cards. \n1: rusty and broken card\n2: broken 8-bit card")
  to_buyq = input()


