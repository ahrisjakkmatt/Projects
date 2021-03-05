# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this is like the card game War but using dice and the ability to bet money

# This game is kind of like the card game war, only with dice instead of cards.
# The user will input how many dice they are rolling, and the number of sides on the dice.
# The player will start with a set amount of "money" (you can choose the amount).
# You will choose an amount you are betting on the next play.
# You and a computer will both roll the amount of dice, and determine the winner (by sum of dice).
# You will gain or lose the money bet.
# You will then choose to bet again or to cash out.
# The game will continue until you cash out or are bankrupt.

"""Bet away, I may deposit the $ you earned in your bank account."""

import random
import os
from time import sleep

os.system('cls')
# random.seed(10) #remove this seed after testing

class Dice:
    def __init__(self, sides): # Deep copy
        self.faces = sides

    """It does not make sense do employ any of these comparison methods, and the add method with dice, only with cups"""
    # def __eq__(self, other):
    #     if type(self) == type(other):
    #         return((self.dice, self.faces)==(other.dice, other.faces_per_dice))
    #     else:
    #         return NotImplemented
    #
    # def __ne__(self, other):
    #     if type(self) == type(other):
    #         return((self.dice, self.faces)==(other.dice, other.faces_per_dice))
    #     else:
    #         return NotImplemented
    #
    # def __lt__(self, other):
    #     if type(self) == type(other):
    #         return((self.dice, self.faces)<(other.dice, other.faces_per_dice))
    #     else:
    #         return NotImplemented
    #
    # def __gt__(self, other):
    #     if type(self) == type(other):
    #         return((self.dice, self.faces)>(other.dice, other.faces_per_dice))
    #     else:
    #         return NotImplemented
    #
    # def __le__(self, other):
    #     if type(self) == type(other):
    #         return((self.dice, self.faces)<=(other.dice, other.faces_per_dice))
    #     else:
    #         return NotImplemented
    #
    # def __ge__(self, other):
    #     if type(self) == type(other):
    #         return((self.dice, self.faces)>=(other.dice, other.faces_per_dice))
    #     else:
    #         return NotImplemented
    #
    """This also was unnecessary each cup was initialized only once. Matter was neither created nor destroyed.
    Dice did not fall to the floor."""
    # def __add__(self, other):
    #     if type(self) == type(other):
    #         return Dice(self.dice+other.dice, self.faces)
    #     else:
    #         return NotImplemented


    def __str__(self):
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
        self.dictio = dict_dice # extra variables used in debugging code
        self.dice_list = dice_list # perhaps not the most intuitive to create a dictionary, then enum it then >> list
        self.value = 0 # without rolling the cup has no value

    def roll(self): # only after rolling does each cup have a value (equal to the sum of the sides)
        total_value=0
        for d in self.dice_list:
            total_value += random.randint(1, d) # perm. the list, determine # of sides, draw randomomly from [1,side]
        self.value=total_value
        return self.value

    # There are redundancies with using the comparison magic methods. Not all are necessary. In fact, I only needed
    # the != and < and took care of the scenarios with if/elif/else conditions
    def __eq__(self, other):
        if type(self) == type(other):
            return((self.value)==(other.value))
        else:
            return NotImplemented

    def __ne__(self, other):
        if type(self) == type(other):
            return((self.value)==(other.value))
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            return((self.value)<(other.value))
        else:
            return NotImplemented

    def __gt__(self, other):
        if type(self) == type(other):
            return((self.value)>(other.value))
        else:
            return NotImplemented

    def __le__(self, other):
        if type(self) == type(other):
            return((self.value)<=(other.value))
        else:
            return NotImplemented

    def __ge__(self, other):
        if type(self) == type(other):
            return((self.value)>=(other.value))
        else:
            return NotImplemented


    def __str__(self): # Deep copy
        cup_string = "Your cup has: \n"
        for i, (k, v) in enumerate(self.dictio.items()):
            cup_string=cup_string+("  " + str(v) + "  of (" + str(k) + "-sided) Dice\n")
        return cup_string

def intro(amount_to_bankrupt,name):
    print(f"{name}, are you ready to play?")
    sleep(2)
    os.system('cls')
    print("You and I throw the same dice.  If your numbers are higher you win.")
    sleep(3)
    print("If my dice are better you lose.  We can also tie.")
    sleep(3)
    print()
    print(f"You can bet up to ${amount_to_bankrupt} and cash out at any time.")
    sleep(2)
    print("As long as you don't go bankrupt.")
    sleep(2)
    print("If you win, you double your bet.   If not, and we don't tie, I win.  ... If we tie")
    sleep(4)
    print("nothing happens.")
    sleep(1)
    print()
    sleep(1)
    print()
    print("I have this here Gulp-sized cup that we can add")
    sleep(1)
    print("... any dice you can imagine!")
    sleep(2)

def play_rounds(max_bet,cup1,cup2,name):
    cashout=max_bet
    playing=1
    bet_amount=prompt_bet()
    while playing==1:
        if bet_amount > cashout:
            print(f"Sorry, {name}, you can bet up to  ${cashout}.")
            bet_amount = prompt_bet()
        else:
            cup1.roll()
            cup2.roll()
            sleep(1)
            print()
            print(f"You rolled  {cup1.value}")
            sleep(1)
            print(f"   I rolled  {cup2.value}.")
            print()
            sleep(2)
            if cup1==cup2:
                print("We rolled the same number.  Sad day.")
                sleep(2)
            if not cup1!=cup2:
                if cup1<cup2:
                    cashout=cashout-bet_amount
                    print(f"{name}, you lost  ${bet_amount}.   You still have  ${cashout} though.")
                    sleep(3)
                    print()
                    print("That's not a lot. Don't bet it all.")
                    sleep(2)
                    print()
                else:
                    cashout=cashout + bet_amount
                    print(f"You won ${bet_amount}!! Now you have ${cashout}.")
                    sleep(2)
            if cashout == 0:
                print()
                print("You lost all your money ... Eeek!")
                print()
                sleep(3)
                print(f"{name}, I hope you don't have to walk very far!")
                sleep(2)
                print("I would give you a ride but I can't. I have to go to the bank!")
                sleep(3)
                break
            print()
            playing = get_binary_int("Would you like to keep playing?\n        YES: 1         NO, Cashout:  0  >>>> ")
            sleep(1)
            os.system('cls')
            if playing == 0:
                break
            bet_amount = prompt_bet()
    print(f'You walk away with ${cashout}.')
    sleep(2)
    print('Better luck next time!')
    sleep(1)
    print(f"Thanks for playing!")
    sleep(5)

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

def prompt_bet():
    return get_int("How much would you like to bet?   >>>> ")

def prompt_dice_setup(name):
    sleep(1)
    print()
    setting_up = True
    die = {}
    new_to_dictionary = True
    first_pass = True
    while setting_up:
        while new_to_dictionary:
            if bool(die):
                if end_setup == 1:
                    while True:
                        faces = get_int("How many sides are on the die?           >>>> ")
                        if faces < 2:
                            print("We need more sides than that! (realistically)")
                            continue
                        else:
                            break
                    if faces in die:
                        print(f"  You already setup {die[faces]} die with {faces} sides.")
                        print()
                    else:
                        quantity_of_dice = get_int(f"How many dice with {faces} sides are you using ?           >>>> ")
                        die_temp = {faces: quantity_of_dice}
                        die.update(die_temp)
                        end_setup = get_binary_int("  Are there any more dice?\n        YES: 1         NO:  0  >>>> ")
                        print()
                elif end_setup == 0:
                    new_to_dictionary = False
                    setting_up = False
                else:
                    print(f"  Sorry, {name} please try '0' or '1'.")
                    continue
            else:
                while True:
                    faces = get_int("How many sides are on the die?           >>>> ")
                    if faces < 2:
                        print()
                        print("We (realistically) need more sides than that! ")
                        print()
                        continue
                    else:
                        break
                quantity_of_dice = get_int(f"How many dice with {faces} sides are you using ?           >>>> ")
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
                            print(f"  Sorry, {name} please enter 1 or 0.")
                            continue
                        break
    return die

def main():
    os.system('cls')
    print("Welcome to War  (with dice).")
    sleep(1)
    print()
    sleep(1)
    print()
    print()
    print("Created by:           Ahriel Godoy")
    print()
    sleep(1)
    os.system('cls')
    print("Hey stranger.  By the looks of you, there is a lot of money in your pocket.")
    sleep(3)
    print()
    amount_to_bankrupt = get_int("How much total money do you have, to spend, or give away?              >>>> ")
    os.system('cls')
    if amount_to_bankrupt <= 0:
        print("Sorry, that's not enough to play today.")
        sleep(2)
        os.system('cls')
    else:
        print("...")
        sleep(1)
        print("With that much you have enough to take the bus.")
        sleep(2)
        print("We all start somewhere.")
        sleep(2)
        print("I guess.")
        sleep(2)
        print()
        os.system('cls')
        name = input("What is your name again?              >>>> ")
        os.system('cls')
        # intro prompt, just some explaining, story, nonsense and jokes
        intro(amount_to_bankrupt,name)
        # prompt user for the quantities and sides of each dice class, entering into a dictionary
        dice = prompt_dice_setup(name)
        # construct two identical cups (per components) of dice for each player, but with unique memory locations to
        # track the values of each cup throw
        cup = Cup(dice)
        cup2 = Cup(dice)
        # Prompts are implemented to excluded negatives and non-integers, as well as execute the desired outcomes
        # i.e. play or cashout
        print()
        print("That is enough to play, the cup is almost full.")
        sleep(2)
        print(cup)
        sleep(4)
        os.system('cls')
        play_rounds(amount_to_bankrupt,cup,cup2,name)

main() # call the main function as required per rubrik