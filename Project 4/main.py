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
random.seed(10) #remove this seed after testing

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

def intro(name):
    print(f"{name}, are you ready to play?")
    sleep(2)
    os.system('cls')
    print("You and I throw the same dice.  If your numbers are higher, you win.")
    sleep(3)
    print("If mine are higher, I will win.  We can also, tie.")
    sleep(3)
    os.system('cls')
    print(f"You can bet up to ${amount_to_bankrupt} and cash out at any time.")
    sleep(3)
    print("As long as you don't go ... bankrupt.")
    sleep(3)
    print("If you win, you double your bet.   If I win, I make money off your misfortune.   If we tie...")
    sleep(5)
    print("nothing happens.")
    sleep(4)
    print()
    print()
    print("Lets' pick the dice we will use and add them to ...")
    sleep(1)
    print("our super, big, Gulp-sized cup.")
    sleep(4)
    print()
    sleep(1)

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
                    print("That's not a lot, you should bet it all.")
                    sleep(3)
                    print()
                else:
                    cashout=cashout + bet_amount
                    print(f"You won  ${bet_amount}!!   Now you have  ${cashout}.")
                    sleep(3)
            if cashout == 0:
                print()
                print("You lost ... all your money ... Yikes!")
                print()
                sleep(3)
                print(f"No gas money, no bus money.  {name}, I hope you don't have to walk very far!")
                sleep(2)
                break
            print()
            playing = get_binary_int("Would you like to keep playing?\n        YES: 1         NO, Cashout:  0  >>>> ")
            os.system('cls')
            if playing == 0:
                break
            bet_amount = prompt_bet()
    sleep(3)
    print()
    print(f'You walk away with ${cashout}.')
    sleep(3)
    print()
    print('Better luck next time!')
    sleep(3)
    os.system('cls')
    print(f"Thanks for playing, {name}!")
    sleep(10)

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
    print("We can make any die with any number of sides.")
    sleep(5)
    print()
    setting_up = True
    die = {}
    new_to_dictionary = True
    first_pass = True
    while setting_up:
        while new_to_dictionary:
            if bool(die):
                if end_setup == 1:
                    faces = get_int("How many sides are on the die?           >>>> ")
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
                faces = get_int("How many sides are on the die?           >>>> ")
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


os.system('cls')
print("Welcome to War  (with dice).")
print()
sleep(1)
amount_to_bankrupt = get_int("How much total money do you have, to spend, or give away?              >>>> ")
os.system('cls')
if amount_to_bankrupt <= 0:
    print("Sorry, that's not enough to play today.")
    sleep(2)
    os.system('cls')
else:
    print("Ok, you have the chance to walk away rich.")
    sleep(1)
    print("But your chances are not very good.")
    sleep(2)
    print()
    name = input("What is your name again?              >>>> ")
    os.system('cls')
    intro(name)
    dice = prompt_dice_setup(name)
    cup = Cup(dice)
    cup2 = Cup(dice)
    print()
    print(cup)
    sleep(4)
    os.system('cls')
    play_rounds(amount_to_bankrupt,cup,cup2,name)