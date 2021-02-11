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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
