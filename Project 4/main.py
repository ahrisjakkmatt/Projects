# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this is a demonstration of the card game War, but as a variant using dice, and the ability to
# bet money

# The game you will make is kind of like the card game war, only with dice instead of cards. The user will input how many dice they are rolling, and the number of sides on the dice.
#
# The player will start with a set amount of "money" (you can choose the amount).
#
# You will choose an amount you are betting on the next play
#
# You and a computer will both roll the amount of dice, and determine the winner (by sum of dice)
#
# You will gain or lose the money bet
#
# You will then choose to bet again or to cash out
#
# The game will continue until you cash out or are bankrupt.
#
#
#
# What you should include in your code:
#
# A dice class which should include (you may include more than this list)
#
#     constructor
#     string magic method
#     All Comparison magic methods (6 in total listing in slides)
#     An add operation magic method (this may be useful in the next class)
#     some way to roll it (this may be its own method or in the constructor)
#
# A "Cup of Dice" class which should include (you may include more than this list)
#
#     constructor
#     A list of dice defined on creation
#     string magic method
#     All Comparison magic methods (6 in total listing in slides)
#     Some way to roll all dice (this may be its own method or in the constructor)
#
# A main method where that runs your game (you may have other methods as well)

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
               "Ace": (11, 11)} # This tuple is in reference to the rank assignment and points of each card, unique

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

        self.rankpoints = RANK_POINTS[self.rank][0]
        self.points = RANK_POINTS[self.rank][1]
        #self.order = RANK_POINTS[rank[0]]
        #self.point = RANK_POINTS[rank[1]]

    def __str__(self):
        return '['+self.rank + ' of ' +self.suit+']'


class Deck:
    def __init__(self): # Deep copy <<< as well as all initializations and instantiations of all classes
        self.deck = []  # start with an empty list#
        self.trump = ""
        # print('The deck of Bisca is composed of 40 cards. This is the traditional french deck without the '
        #       '8s, 9s, and 10s. There are 40 cards.')
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

    def __str__(self): # Deep copy because it replaces the memory
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has '+str(len(self.deck))+' cards: '+deck_comp

    def shuffle(self):
        # print('The deck was shuffled.')
        print()
        random.shuffle(self.deck) # This is a deep copy because it returns a new memory address of the deck list

    def cut(self):
        trump = []
        single_card = random.randint(0, 39)
        if self.deck[single_card].rank=="Ace" or self.deck[single_card].rank=="Seven":
            # Here, by traditional rules, the flipped (cut) card cannot be the 2 strongest trumps, Ace or Seven,
            # This would severely hinder the play of the game, because the cut card, is also the last card, so
            # In the 4 person game, with additional rules and playability, those 2 cards provide extra scoring ability,
            # if played in the middle game. The game by DrKappa in Google Play does not utilize this rule.
            single_card = random.randint(0, 39)
        else:
             pass
        print('The card cut was: '+self.deck[single_card].__str__())
        print(self.deck[single_card].suit+' are the trump suit.')
        print('The '+self.deck[single_card].__str__()+' was sent to the bottom of the draw pile facing up.')
        print()
        trump.append(self.deck[single_card]) # Shallow / reference to deck[single_card]
        temp=self.deck.pop(single_card)
        self.deck.append(temp)  # Shallow
        """This is a temp variable may not need"""
        self.trump = trump[0].suit
        sleep(4)
        return self.trump


        # print('The trump card is: ' + deck[single_card].__str__())
        # self.deck.pop(single_card)
        # return single_card

    def deal(self): # Deep copy
        if len(self.deck)>0:
            single_card = self.deck.pop(0)
            return single_card
        else:
            return "Deck is empty."
        #player.hand.draw_card.(single_card)

class Dice:
    def __init__(self, sides): # Deep copy
        self.faces = sides

    def __eq__(self, other):
        if type(self) == type(other):
            return((self.dice, self.faces)==(other.dice, other.faces_per_dice))
        else:
            return NotImplemented

    def __ne__(self, other):
        if type(self) == type(other):
            return((self.dice, self.faces)==(other.dice, other.faces_per_dice))
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            return((self.dice, self.faces)<(other.dice, other.faces_per_dice))
        else:
            return NotImplemented

    def __gt__(self, other):
        if type(self) == type(other):
            return((self.dice, self.faces)>(other.dice, other.faces_per_dice))
        else:
            return NotImplemented

    def __le__(self, other):
        if type(self) == type(other):
            return((self.dice, self.faces)<=(other.dice, other.faces_per_dice))
        else:
            return NotImplemented

    def __ge__(self, other):
        if type(self) == type(other):
            return((self.dice, self.faces)>=(other.dice, other.faces_per_dice))
        else:
            return NotImplemented

    def __add__(self, other):
        if type(self) == type(other):
            return Dice(self.dice+other.dice, self.faces)
        else:
            return NotImplemented

    def roll(self):
        total_value=0
        for die in self.quantity_of_dice:
            total_value += die*random.randint(2, self.faces)
        return total_value

    def __str__(self): # Deep copy
        return 'Die['+str(self.faces)+']'

class Cup:
    def __init__(self, dict_dice): # Pass in the dictionary created during the setup prompt
        size = 0
        dice_list=[]
        for i, (k, v) in enumerate(dict_dice.items()):
            size += v
            j=0
            while j < v:
                temp = Dice(k)
                dice_list.append(temp.faces)
                j += 1
        self.size = size
        self.dictio = dict_dice
        self.dice_list = dice_list
        # j=0
        # while j < len(dice_list):
        #     self.dice_list = self.dice_list.append(type(dice_list[j]))
        #     j+=1
        self.value = 0

    def roll(self):
        total_value=0
        for d in self.dice_list:
            total_value += random.randint(1, d)
        self.value=total_value
        return self.value

    def __str__(self): # Deep copy
        cup_string = "Your cup has: \n"
        for i, (k, v) in enumerate(self.dictio.items()):
            cup_string=cup_string+("  " + str(v) + "  of (" + str(k) + "-sided) Dice\n")
        return cup_string

class Hand:
    def __init__(self, c1, c2, c3): # Deep copy
        self.cards = [c1, c2, c3]  # start with an empty list as we did in the Deck class

    def draw_card(self, card): # Deep copy
        # print('The '+card.__str__()+' was drawn.')
        self.cards.append(card)
        #return card
        # name = card.rank
        # self.value += VALUES[name][0]

    def play_card(self, card): # Deep copy
        self.cards.remove(card)

    def __str__(self): # Deep copy
        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n '+card.__str__()
        return 'The hand has '+str(len(self.cards))+' cards: '+hand_comp


class Player:
    def __init__(self, name, hand, pile=[]): # Deep copy
        self.name = name
        self.hand = hand
        self.pile = Pile()
        self.points = 0

    def __str__(self): # Deep copy
        #print(self.name + ' has: ' +self.pile.points())
        hand_comp = ''
        for card in self.hand.cards:
            hand_comp += ' ' + card.__str__()
        return self.name + ' has: ' + hand_comp

    def print_hand(self): # Deep copy
        hand_comp = ''
        for card in self.hand.cards:
            hand_comp += ' ' + card.__str__()
        return self.name+"'s hand has: " + hand_comp

    def print_pile(self): # Deep copy
        pile_comp = ''
        for card in self.pile.cards:
            pile_comp += ' ' + card.__str__()
        return self.name+"'pile has: " + pile_comp


class Pile:
    def __init__(self): # Deep copy
        self.cards = []
        self.points = 0

    def add_card(self,card): # Deep copy
        self.cards.append(card)

    def points(self): # Deep copy
        for card in self.cards:
            name = card.rank
            self.points += VALUES[name][0]
        return str(self.points)+' points'

    def __str__(self): # Deep copy
        pile_comp = ''
        for card in self.cards:
            pile_comp += '\n '+card.__str__()
        return str(pile_comp)


def compare_ranks(card1, card2):
    suit = card1.suit
    # print(f'{card2.__str__()} has {card2.suit} suit and rank {card2.rankpoints}')
    # print(f'{card1.__str__()} has {card1.suit} suit and rank {card1.rankpoints}')
    # x=input()
    sleep(1)
    if card2.suit == suit:
        if card2.rankpoints > card1.rankpoints:
            # sleep(1)
            print(f'{card2.__str__()} beats the {card1.__str__()}.')
            sleep(1)
            return False
        else:
            # sleep(1)
            print(f'{card1.__str__()} beats the {card2.__str__()}.')
            sleep(1)
            return True
    elif card2.suit == TRUMP:
        # sleep(1)
        print(f'{card2.__str__()} is a trump card and wins.')
        sleep(1)
        return False
    else:
        # sleep(1)
        print(f'{card1.__str__()} is the highest of {card1.suit} and wins.')
        sleep(1)
        return True

# This function takes in the choices of both players. Since there wasn't enough time to code the adversary logic
# The game works by two players selecting each cards, unbeknownst of the card options of the other player, it is
# Difficult to do see all the cards and play similar to in real life, since it is a game where lack of information
# affects gameplay
def prompt_cards(first_to_play,second_to_play, round=1):
    sleep(1)
    os.system('cls')
    print(f'Round {round}: {first_to_play.name} starts:')

    global playing
    if round <19: # 18 rouns to clear the deck and assign cards to 2 players.
        while True:
            option1 = input(
                f'Do you play\n     A:{first_to_play.hand.cards[0]} or '
                f'B:{first_to_play.hand.cards[1]} or C:{first_to_play.hand.cards[2]}? \n>>> ')
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
        # sleep(1)
        print(f"{second_to_play.name}'s turn:")

        playing = True

        while True:
            option2 = input(
                f'Do you play\n     A:{second_to_play.hand.cards[0]} or '
                f'B:{second_to_play.hand.cards[1]} or C:{second_to_play.hand.cards[2]}? \n>>> ')
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
        return(x,y)
    elif round==19: # Each player has two cards to select in second-to-last round
        while True:
            option1 = input(
                f'Do you play\n     A:{first_to_play.hand.cards[0]} or '
                f'B:{first_to_play.hand.cards[1]}? \n>>> ')
            if option1[0].lower() == 'a':
                x = 0
                playing = False
            elif option1[0].lower() == 'b':
                x = 1
                playing = False
            else:
                print("Sorry, please try again.")
                continue
            break
        print(f'{first_to_play.name} played {first_to_play.hand.cards[x]}')
        print()
        # sleep(1)
        print(f"{second_to_play.name}'s turn:")

        playing = True

        while True:
            option2 = input(
                f'Do you play\n   A:{second_to_play.hand.cards[0]} or '
                f'B:{second_to_play.hand.cards[1]}? \n>>> ')
            if option2[0].lower() == 'a':
                y = 0
                playing = False
            elif option2[0].lower() == 'b':
                y = 1
                playing = False
            else:
                print("Sorry, please try again.")
                continue
            break
        print(f'{second_to_play.name} played {second_to_play.hand.cards[y]}')
        print()
        return(x,y)
    elif round == 20:
        # Last round each player has only 1 card, play is predetermined because the order of play depends on victor of previous round
        print(f"Each player only has 1 card left. {first_to_play} starts.")
        print()
        sleep(2)
        print(f'{first_to_play.name} played {first_to_play.hand.cards[0]}')
        print(f'{second_to_play.name} played {second_to_play.hand.cards[0]}')
        sleep(3)
        return(0,0)


# In this function the ranks of the selected cards are assessed, and the resulting logic alters the hand,
# and adds to the winner's pile, it iterates with round number, returning the winning player
# the original logic did not return Player type, instead it returned a Bool, and the logic was redundant because
# the output was a reference to the previous iteration, and was supposed to swap players...
# Depending on who wins a round, that person starts the next round, anyways, it was redundant, and the skeleton remained
# Having more time, I would clean this up.

# This function returns a shallow copy of the players
def adjust_hands(first_to_play,second_to_play, round, winner_previous_round):
    if winner_previous_round==first_to_play:
        if round>1:
            print(f'    {first_to_play.name}    won that round.')
            sleep(1)
            os.system('cls')
        x,y=prompt_cards(first_to_play,second_to_play,round)
        if compare_ranks(first_to_play.hand.cards[x],second_to_play.hand.cards[y]) == True:
            first_to_play.pile.add_card(first_to_play.hand.cards[x]), \
            first_to_play.pile.add_card(second_to_play.hand.cards[y])
            # os.system('cls')
            print(f"{first_to_play.hand.cards[x]} and {second_to_play.hand.cards[y]} were added to "
                  f"{first_to_play.name}'s pile.")
            print()
            winner_this_round=first_to_play
            result=True
        else:
            second_to_play.pile.add_card(first_to_play.hand.cards[x]), \
            second_to_play.pile.add_card(second_to_play.hand.cards[y])
            # os.system('cls')
            print(
                f"{first_to_play.hand.cards[x]} and {second_to_play.hand.cards[y]} were added to "
                f"{second_to_play.name}'s pile.")
            print()
            winner_this_round=second_to_play
            result=False
        first_to_play.hand.cards.pop(x), second_to_play.hand.cards.pop(y)
    else:
        print(f'    {second_to_play.name}    won that round.')
        sleep(1)
        os.system('cls')
        x,y = prompt_cards(second_to_play, first_to_play, round)
        if compare_ranks(second_to_play.hand.cards[x],first_to_play.hand.cards[y]) == True:
            second_to_play.pile.add_card(second_to_play.hand.cards[x]), \
            second_to_play.pile.add_card(first_to_play.hand.cards[y])
            # os.system('cls')
            print(f"{second_to_play.hand.cards[x]} and {first_to_play.hand.cards[y]} were added to "
                  f"{second_to_play.name}'s pile.")
            print()
            winner_this_round=second_to_play
            result=True
        else:
            first_to_play.pile.add_card(second_to_play.hand.cards[x]), \
            first_to_play.pile.add_card(first_to_play.hand.cards[y])
            # os.system('cls')
            print(
                f"{second_to_play.hand.cards[x]} and {first_to_play.hand.cards[y]} were added to "
                f"{first_to_play.name}'s pile.")
            print()
            winner_this_round=first_to_play
            result=False
        first_to_play.hand.cards.pop(y), second_to_play.hand.cards.pop(x)
    sleep(2)
    return [first_to_play, second_to_play,x,y,winner_this_round]

def get_binary_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, your response must be 0 or 1.")
            continue

        if (value < 0) or (value > 1):
            print("Sorry, your response must be 0 or 1.")
            continue
        else:
            break
    return value

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, your response must be an integer.")
            continue
        else:
            break
    return value

def prompt_dice_setup():
    setting_up = True
    die = {}
    new_to_dictionary = True
    first_pass = True
    while setting_up:
        while new_to_dictionary:
            if bool(die):
                if end_setup == 1:
                    faces = get_int("How many faces are on the die?           >>>> ")
                    if faces in die:
                        print(f"  You already setup {die[faces]} die with {faces} faces.")
                        print()
                    else:
                        quantity_of_dice = get_int(f"How many dice with {faces} faces are you using ?           >>>> ")
                        die_temp = {faces: quantity_of_dice}
                        die.update(die_temp)
                        end_setup = get_binary_int("  Are there any more dice?\n        YES: 1         NO:  0  >>>> ")
                        print()
                elif end_setup == 0:
                    new_to_dictionary = False
                    setting_up = False
                else:
                    print("  Sorry, please try '0' or '1'.")
                    continue
            else:
                faces = get_int("How many faces are on the die?           >>>> ")
                quantity_of_dice = get_int(f"How many dice with {faces} faces are you using ?           >>>> ")
                die_temp = {faces: quantity_of_dice}
                die.update(die_temp)
                while first_pass:
                    try:
                        end_setup = get_binary_int("  Are there any more dice?\n        YES: 1         NO:  0  >>>> ")
                        print()
                    except ValueError:
                        continue
                    else:
                        if end_setup == 1:
                            first_pass = False
                            continue
                        elif end_setup == 0:
                            first_pass = False
                            new_to_dictionary = False
                            setting_up = False
                        else:
                            print("  Sorry, please enter 1 or 0.")
                            continue
                        break
    return die


os.system('cls')
# print("This is War With Dice.")
# sleep(1)
# print()
# print("Find the rules at:"), sleep(1)
# print("https://en.wikipedia.org/wiki/Bisca_(card_game)")
# sleep(1)
# print()
# print()
# print("Created by:           Ahriel Godoy")
# print()
# sleep(1)
# os.system('cls')
# # player_name = 'Ahriel'
# player_name = input("Who is playing?               ")
# amount_to_bankrupt = input("How much total money do you have?               ")
# dealer_name = 'Computer' #input("And who else?                 ")
# # quantity_of_dice = input("How many dice are you using?               ")
# # quantity_of_dice = input("How many faces are on the die?               ")
# print()
# print("Ready to play?");sleep(1)
# print("You and I throw the same dice. If your numbers are higher you win.");sleep(1)
# print("If mine are higher I win. We can also tie.");sleep(1)
# print(f"You can bet up to {amount_to_bankrupt}.");sleep(1)
# print("You choose to cash out at any time.");sleep(1)
# print("When you win, you double your bet. When I win, I take your bet. If we tie, no money is lost.");sleep(1)
# print("You can play until you cash out or until you bankrupt");sleep(1)
# print()
# print("Lets' pick the die we will throw from the cup.");sleep(1)
dice = prompt_dice_setup()
print("Your cup has: ")
for i, (k, v) in enumerate(dice.items()):
    print("  "+str(v)+"  of ("+str(k)+"-sided) Dice")
print(dice)
cup = Cup(dice)
# print(cup.size)
# print(cup.dice_list)
# print(cup.dictio)
# print(cup)
print(cup.roll())
sleep(1)
print(cup.roll())
sleep(1)
print(cup.roll())
# Create & shuffle the deck, cut, deal three cards to each player
# os.system('cls')
# print("Create & shuffle the deck, cut, deal three cards to each player")
# sleep(1)
# # os.system('cls')
# deck = Deck()
# deck.shuffle()
# # print(deck.__str__())
#
# # sleep(200) This was necessary to pause and right down the cards, so I test with an actual physical deck, sorting by
# # the shuffle position ... of course later I realized I could just return and read the console after it was printed
# TRUMP = deck.cut()
# # sleep(2)
# # j=input() I added inputs as pauses requiring the player to hit enter to continue, to read the text, not sure if there
# # is another better way
# #print(deck.__str__())
# #print(deck.trump)
# #print(deck)
# #print(deck.deck[0])
#
#
#
# # The first three cards are needed to be dealt "hard coded" to initialize the Hand class //
# # the instantiation of classes creates assigns to a new memory location so these are all Deep copys
# card1 = (deck.deal())
# card2 = (deck.deal())
# card3 = (deck.deal())
# player_hand = Hand(card1, card2, card3)
# p1 = Player(player_name,player_hand)
# print()
# card4 = (deck.deal())
# card5 = (deck.deal())
# card6 = (deck.deal())
# dealer_hand = Hand(card4, card5, card6)
# p2 = Player(dealer_name,dealer_hand)
#
# # print(p1.print_hand())
# # print(p2.print_hand())
#
# # sleep(1)
# # round 1 has no previous_winner, it is just be predetermined to be player 1, but in 4 person game, this changes with every round
# p1,p2,x,y,winner=adjust_hands(p1,p2,1,p1)
# # result1 = p1.hand.cards[x]
# # result2 = p2.hand.cards[y]
# # sleep(1)
# # print(p1.print_hand())
# # print(p1.print_pile())
# # print(p2.print_hand())
# # print(p2.print_pile())
#
# i=1 # round number
# while i<18:
#     # it is important to note that the last card (that was "cut" out) in the deck is visible, and is a trump card,
#     # players may try to lose round 17 to earn that trump card
#     # drawing, appending to hand, popping from deck, all happens in rounds 1-17
#     i += 1
#     if winner == p1:
#         cardA = deck.deal()
#         cardB = deck.deal()
#         p1.hand.draw_card(cardA)
#         p2.hand.draw_card(cardB)
#         print()
#     else:
#         cardA = deck.deal()
#         cardB = deck.deal()
#         p1.hand.draw_card(cardB)
#         p2.hand.draw_card(cardA)
#         print()
#     p1, p2, x, y, winner = adjust_hands(p1, p2, i, winner)
#
#
#
#     #pause = input()
#     # os.system('cls')
# while i<20:
#     i += 1
#     p1, p2, x, y, winner = adjust_hands(p1, p2, i, winner)
# p1_sum=0
# for card in p1.pile.cards:
#     p1_sum+=card.points # this is a deep copy because ints are not iterable
# p2_sum=0
# for card in p2.pile.cards:
#     p2_sum+=card.points # deep copy
# print()
# print(p1.print_pile()), sleep(2)
# print()
# print(p2.print_pile()), sleep(2), os.system('cls'), print()
# print("Now we total the points in each players pile.")
# sleep(1)
# print(f"{p1.name} sums the points in his earned pile and gets {p1_sum} points.")
# sleep(2)
# print()
# print(f"{p2.name} sums the points in his earned pile and gets {p2_sum} points.")
# print()
# sleep(2)
# if p1_sum==p2_sum:
#     print("There were 60 points to each player. This set was a draw.")
# elif p1_sum>p2_sum:
#     print(f"{p1.name} had more points and won the set.")
# else:
#     print(f"{p2.name} had more points and won the set.")
# sleep(7)
# os.system('cls')
# print()
# sleep(2)
# print()
# sleep(2)
# print("Thank you!")
# sleep(10)