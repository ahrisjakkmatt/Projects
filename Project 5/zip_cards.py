from itertools import zip_longest

suits =  ["Hearts","Spades","Clubs","Diamonds"]
values = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]

deck = []

for suit in suits:
    temp = []
    temp.append(suit)
    deck.extend(list(zip_longest(temp, values, fillvalue=suit)),)

print(deck)

