# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this is a demonstration of the game Bisca (a Portuguese version of the Italian game Bríscola)

# This variant of Bisca is for 2 players. The most common version of Bisca is that of 4 players as a paired team.

# References:--------------------------------------------------------------------------------------
# The wikipedia referencing the rules of Bisca can be found at https://en.wikipedia.org/wiki/Bisca_(card_game)
# There is also an app in the google play store called "Briscola", made by DrKappa at
# https://play.google.com/store/apps/details?id=net.drkappa.game.briscola&hl=en_US&gl=US
# Referencing the app, the rules will follow the settings : {Single Player, Portuguese Rules, 5 Sets to Win}

# The Deck:-----------------------------------------------------------------------------------------
# Bisca is played with the common 52-card French deck but removing the 8's, 9's, and 10's of each suit. Therefore in
# total are 40 cards required to play.

# Scoring and Win Conditions-------------------------------------------------------------------------
# The card ranks from highest to lowest are : A 7 K J Q 6 5 4 3 2.
# Notice the Ace is the highest ranking card, the 7 is ranked above all face and number cards, and then followed by the
# King, Jack and Queen. These cards have corresponding points. The cards 6, 5, 4, 3 and 2 are not worth points.
# There is also a trump suit that is determined in the first round. All cards of the trump suit beat non-trump suits,
# and if 2 or more cards of that trump suit are in the round, the ranking follows the card ranks.

# Trump cards, suit type and card rankings determine the winner of each round. In the 2-player game, there are 20 rounds
# per set. At the beginning of each set, the points are zeroed. The winner of each round wins the 2 cards played in
# that round. Points are counted at the end of each set to determine the winner of the set. The player scoring 61 or
# more points at the end of the set wins the set. If both players end the set with 60 points, the set is a tie and is
# replayed. The first player to win 5 rounds wins the game.

# The main objective of the game is to accumulate more points than the opponent, based on the cards that are captured
# and forfeited.
# The values of the cards at the end of the set are as follows:
#   Each:
#           Ace             is worth    11 points       4x(11pt)    44pt
#           Seven (7)       is worth    10 points       4X(10pt)    40pt
#           King            is worth    4 points        4X(4pt)     16pt
#           Jack            is worth    3 points        4x(3pt)     12pt
#           Queen           is worth    2 points        4x(2pt)     8pt

#           (2) thru (6)    is worth    0 points        20X(0pt)    0pt
#           -------------------------------------------------------------
#   Total:  40 cards                                                120pt

# The deal:---------------------------------------------------------------------------------------
# The first dealer is chosen at random. The dealer shuffles the cards and the player at the dealer's left cuts, randomly
# selecting and showing the trump suit and that card is then placed at the bottom of the deck, partially visible. That
# visible trump card cannot be an Ace or Seven. If an Ace or Seven is selected with the cut, the next card replaces it,
# or the next, until one is selected that is neither Ace nor Seven. This mechanic will not be demonstrated as it can be
# built into the shuffle/deal and is not part of the players' actions.

# The dealer then gives 3 cards to each player, one card at a time.
# The player who cut the deck (Player B) begins by selecting a card from his hand (of three cards) into the center.
# The player who dealt that round (Player A) then plays one from her hand, which either captures the card in the center
# or is forfeited in that round.

# The first card of the round will by default win the round, unless challenged by a higher ranking card of the same
# suit, or a trump card.

# If the cards are the same suit, the highest value card (or the highest face number on non-value cards) wins;
# If the cards differ in suits and neither are a trump card, then the first card wins;
# If the cards are of different suits and there is a "trump card" among them, who played the highest trump card wins;
# Captured cards are placed face down near the player who won them for later score counting - these cards are not played
# again in that set.

# After the round each player (with two cards left) takes a new card from the top of the deck. Whoever won the previous
# takes the top card.

# Rounds are repeated until all cards are played in the deck, including the partially visible trump card selected in
# the cut.
# At the end of the set, the captured cards values are counted by adding their point values. The total available points
# are 120 points so the player accumulating 61 or more points before, earns 1 set point in the game. At a 60-60 split
# point set the set is forfeited and replayed.

import random
import os
from time import sleep
os.system('cls')

random.seed(10) #remove this seed after testing

SUITS = ("Clubs",
         "Diamonds",
         "Hearts",
         "Spades")

RANKS = ("Two", "Three", "Four", "Five", "Six",
        "Queen", "Jack", "King",
        "Seven",
        "Ace")

VALUES = {"Two": (2, 0), "Three": (3, 0), "Four": (4, 0), "Five": (5, 0), "Six": (6, 0),
               "Queen": (7, 2), "Jack": (8, 3), "King": (9, 4),
               "Seven": (10, 10),
               "Ace": (11, 11)}

TRUMP = ""

playing = True

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        RANK_POINTS = {"Two": (2, 0), "Three": (3, 0), "Four": (4, 0), "Five": (5, 0), "Six": (6, 0),
                       "Queen": (7, 2), "Jack": (8, 3), "King": (9, 4),
                       "Seven": (10, 10),
                       "Ace": (11, 11)}

        #self.order = RANK_POINTS[rank[0]]
        #self.point = RANK_POINTS[rank[1]]

    def __str__(self):
        return '['+self.rank + ' of ' +self.suit+']'


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list#
        self.trump = ""
        print('The deck of Bisca is composed of 40 cards. This is the traditional french deck without the '
              '8s, 9s, and 10s. There are 40 cards.')
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has '+str(len(self.deck))+' cards: '+deck_comp

    def shuffle(self):
        print('The deck was shuffled.')
        print()
        random.shuffle(self.deck)

    def cut(self):
        trump = []
        single_card = random.randint(0, 39)
        if self.deck[single_card].rank=="Ace" or self.deck[single_card].rank=="Seven":
            single_card = random.randint(0, 39)
        else:
             pass
        print('The card cut was: '+self.deck[single_card].__str__())
        print(self.deck[single_card].suit+' are the trump suit.')
        print('The '+self.deck[single_card].__str__()+' was sent to the bottom of the draw pile facing up.')
        print()
        trump.append(self.deck[single_card])
        temp=self.deck.pop(single_card)
        self.deck.append(temp)
        """This is a temp variable may not need"""
        self.trump = trump[0].suit
        return self.trump


        # print('The trump card is: ' + deck[single_card].__str__())
        # self.deck.pop(single_card)
        # return single_card

    def deal(self):
        single_card = self.deck.pop(0)
        #player.hand.draw_card.(single_card)
        return single_card


class Hand:
    def __init__(self, c1, c2, c3):
        self.cards = [c1, c2, c3]  # start with an empty list as we did in the Deck class

    def draw_card(self, card):
        print('The '+card.__str__()+' was drawn.')
        self.cards.append(card)
        #return card
        # name = card.rank
        # self.value += VALUES[name][0]

    def play_card(self, card):
        self.cards.remove(card)

    def __str__(self):
        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n '+card.__str__()
        return 'The hand has '+str(len(self.cards))+' cards: '+hand_comp


class Player:
    def __init__(self, name, hand, pile=[]):
        self.name = name
        self.hand = hand
        self.pile = Pile()
        self.points = 0

    def __str__(self):
        #print(self.name + ' has: ' +self.pile.points())
        hand_comp = ''
        for card in self.hand.cards:
            hand_comp += ' ' + card.__str__()
        return self.name + ' has: ' + hand_comp

    def print_hand(self):
        hand_comp = ''
        for card in self.hand.cards:
            hand_comp += ' ' + card.__str__()
        return self.name+"'s hand has: " + hand_comp

    def print_pile(self):
        pile_comp = ''
        for card in self.pile.cards:
            pile_comp += ' ' + card.__str__()
        return self.name+"'pile has: " + pile_comp


class Pile:
    def __init__(self):
        self.cards = []
        self.points = 0

    def add_card(self,card):
        self.cards.append(card)

    def points(self):
        for card in self.cards:
            name = card.rank
            self.points += VALUES[name][0]
        return str(self.points)+' points'

    def __str__(self):
        pile_comp = []
        for card in self.cards:
            pile_comp += '\n '+card.__str__()
        return 'The pile has: '+pile_comp


class Draw_Pile:
    def __init__(self, cards):
        self.cards = []  # start with an empty list as we did in the Deck class

    def draw_card(self, card):
        self.pile.pop(card)

    def __str__(self):
        draw_pile_comp = ''
        for card in self.card:
            draw_pile_comp += '\n ' + card.__str__()
        return 'The hand has: ' + hand_comp


class Points:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total - + self.bet


def compare_ranks(card1, card2):
    suit = card1.suit
    if card2.suit == suit:
        if card2.rank[0] > card1.rank[0]:
            sleep(1)
            print(f'{card2.__str__()} beats the {card1.__str__()}.')
            sleep(1)
            return False
        else:
            sleep(1)
            print(f'{card1.__str__()} beats the {card2.__str__()}.')
            sleep(1)
            return True
    elif card2.suit == TRUMP:
        sleep(1)
        print(f'{card2.__str__()} is a trump card and wins.')
        sleep(1)
        return False
    else:
        sleep(1)
        print(f'{card1.__str__()} is the highest of {card1.suit} and wins.')
        sleep(1)
        return True

def play_from_hand(deck, hand):
    global playing

    while True:
        x = input("What card would you like to play? Enter 'a' or 'b' or 'c'")

        if x[0].lower() == 'a':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def prompt_cards(first_to_play,second_to_play, round=1):
    print(f'Round {round}: {first_to_play.name} starts:')

    global playing

    while True:
        option1 = input(
            f'Does {first_to_play.name} want to play A:{first_to_play.hand.cards[0]} or B:{first_to_play.hand.cards[1]} or C:{first_to_play.hand.cards[2]}? ')
        if option1[0].lower() == 'a':
            x = 0
            playing = False
        elif option1[0].lower() == 'b':
            x = 1
            playing = False
        elif option1[0].lower() == 'c':
            x = 2
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break
    print(f'{first_to_play.name} played {first_to_play.hand.cards[x]}')
    print()
    sleep(1)
    print(f"{second_to_play.name}'s turn:")

    playing = True

    while True:
        option2 = input(
            f'Does {second_to_play.name} want to play A:{second_to_play.hand.cards[0]} or B:{second_to_play.hand.cards[1]} or C:{second_to_play.hand.cards[2]}? ')
        if option2[0].lower() == 'a':
            y = 0
            playing = False
        elif option2[0].lower() == 'b':
            y = 1
            playing = False
        elif option2[0].lower() == 'c':
            y = 2
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break
    print(f'{second_to_play.name} played {second_to_play.hand.cards[y]}')
    print()
    sleep(1)
    #print(type(result1))
    #print(result2)
    return(x,y)

def adjust_hands(first_to_play,second_to_play, round=1, won_last=True):
    sleep(1)
    os.system('cls')
    if won_last==True:
        x,y=prompt_cards(first_to_play,second_to_play,round)
        if compare_ranks(first_to_play.hand.cards[x],second_to_play.hand.cards[y]) == True:
            first_to_play.pile.add_card(first_to_play.hand.cards[x]), first_to_play.pile.add_card(second_to_play.hand.cards[y])
            os.system('cls')
            print(f"{first_to_play.hand.cards[x]} and {second_to_play.hand.cards[y]} were added to {first_to_play.name}'s pile.")
            sleep(1)
            result=True
        else:
            second_to_play.pile.add_card(first_to_play.hand.cards[x]), second_to_play.pile.add_card(second_to_play.hand.cards[y])
            os.system('cls')
            print(
                f"{first_to_play.hand.cards[x]} and {second_to_play.hand.cards[y]} were added to {second_to_play.name}'s pile.")
            sleep(1)
            result=False
        first_to_play.hand.cards.pop(x), second_to_play.hand.cards.pop(y)
    else:
        x,y = prompt_cards(second_to_play, first_to_play, round)
        if compare_ranks(second_to_play.hand.cards[x],first_to_play.hand.cards[y]) == True:
            second_to_play.pile.add_card(second_to_play.hand.cards[x]), second_to_play.pile.add_card(first_to_play.hand.cards[y])
            os.system('cls')
            print(f"{second_to_play.hand.cards[x]} and {first_to_play.hand.cards[y]} were added to {second_to_play.name}'s pile.")
            sleep(1)
            result=True
        else:
            first_to_play.pile.add_card(second_to_play.hand.cards[x]), first_to_play.pile.add_card(first_to_play.hand.cards[y])
            os.system('cls')
            print(
                f"{second_to_play.hand.cards[x]} and {first_to_play.hand.cards[y]} were added to {first_to_play.name}'s pile.")
            sleep(1)
            result=False
        first_to_play.hand.cards.pop(y), second_to_play.hand.cards.pop(x)
    return [first_to_play, second_to_play,x,y,result]


# test_deck = Deck()
# print(test_deck)
# name="King"
# card=VALUES[name]
# print(card[0])
# print(VALUES[name][0])

os.system('cls')
print("This is Bisca.")
print("Created by:           Ahriel Godoy")
sleep(2)

# Create & shuffle the deck, cut, deal three cards to each player
os.system('cls')
print("Create & shuffle the deck, cut, deal three cards to each player")
sleep(1)
os.system('cls')
deck = Deck()
deck.shuffle()
#print(deck.__str__())
#print()
#sleep(200)
TRUMP = deck.cut()
sleep(2)
# j=input()
#print(deck.__str__())
#print(deck.trump)
#print(deck)
#print(deck.deck[0])

# player_name = "Ahriel"
player_name = input("What is player 1's name? ")
card1 = (deck.deal())
card2 = (deck.deal())
card3 = (deck.deal())
player_hand = Hand(card1, card2, card3)
p1 = Player(player_name,player_hand)
print(p1.print_hand())
print()
# dealer_name = "Dealer"
dealer_name = input("What is player 2's name? ")
card4 = (deck.deal())
card5 = (deck.deal())
card6 = (deck.deal())
dealer_hand = Hand(card4, card5, card6)
p2 = Player(dealer_name,dealer_hand)
print(p2.print_hand())
print()
sleep(1)

p1,p2,x,y,won=adjust_hands(p1,p2,1)
# result1 = p1.hand.cards[x]
# result2 = p2.hand.cards[y]
sleep(1)
print(p1.print_hand())
print(p1.print_pile())
print(p2.print_hand())
print(p2.print_pile())

i=1
while i<18:
    i += 1
    if won == True:
        cardA = deck.deal()
        cardB = deck.deal()
        p1.hand.draw_card(cardA)
        p2.hand.draw_card(cardB)
    else:
        cardA = deck.deal()
        cardB = deck.deal()
        p1.hand.draw_card(cardB)
        p2.hand.draw_card(cardA)
    p1, p2, x, y, won = adjust_hands(p1, p2,i, won)
    sleep(1)
    os.system('cls')
    print(p1.print_hand())
    print(p1.print_pile())
    print(p2.print_hand())
    print(p2.print_pile())
    sleep(2)
    #pause = input()
    os.system('cls')
#print(p1.pile)
#print(p2.pile)
#print(p1.hand)
#print(p2.hand)

#print(deck)
#print(cardA)
#print(cardB)


#print(deck)

"""

while True:
    print("This is Bisca.")

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)"""