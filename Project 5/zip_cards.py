from itertools import zip_longest

suits =  ["Hearts","Spades","Clubs","Diamonds"]
values = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]

deck = []

for suit in suits:
    temp = [] # create a temporary list, from which will create tuples
    temp.append(suit)
    deck.extend(list(zip_longest(temp, values, fillvalue=suit)),)
    # zip through the longest list i.e. values, and join with suit, filling in the suit for None
    # it is necessary to extend in order to not create multiple tuples or lists

print(deck)

