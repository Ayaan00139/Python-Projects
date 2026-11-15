import random
# OR----------- 
# from random import choice

coin = random.choice(["heads","tails"])# 50 50 for both choices
#print(coin)

number= random.randint(1,10)# random number from 1 to 10 inclusive
#print(number)

cards=["jack","queen","king"]
random.shuffle(cards)#shuffle the list given to it
# for card in cards:
#     print(card)

