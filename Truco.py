from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []

player1_cards = []
player2_cards = []

#IntEnum for card values
class Card(IntEnum):
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  JACK = 11
  QUEEN = 12
  KING = 13
  ACE = 14

#suit enum for cards
class Suit(Enum):
  SPADES = "spades"
  HEARTS = "hearts"
  CLUBS = "clubs"
  DIAMONDS = "diamonds"

#class for cards
class PlayingCard:
  def __init__(self, card_value, card_suit):
    self.card = card_value
    self.suit = card_suit

#function to deal fuil deck of cards
def create_deck():
  for suit in Suit:
    for card in Card:
      full_deck.append(PlayingCard(Card(card), Suit(suit)))
  return full_deck

#Draw monster cardo
def draw_card(deck):
  rand_card = randint(0, len(deck) -1)
  return deck.pop(rand_card)


#Deal two players for the game
def deal_war():
  while(len(partial_deck) > 0):
    player1_cards.append(draw_card(partial_deck))
    player2_cards.append(draw_card(partial_deck))

create_deck()
partial_deck = list(full_deck)
deal_war()

for i in range(0,len(player1_cards)):
  if (player1_cards[i].card > player2_cards[i].card):
    print("Player 1 wins the match with: ", player1_cards[i].card)
    print("Player 2 loses with: ", player2_cards[i].card)
  if(player1_cards[i].card < player2_cards[i].card):
    print("Player 2 wins the match with: ", player2_cards[i].card)
    print("Player 1 loses with: ", player1_cards[i].card)
  else:
    print("War!")



#test_card = draw_card(partial_deck)
#print("You drew a: ", test_card.card, test_card.suit)

#for i in range(0, len(full_deck)):
  #print("Suit: ", full_deck[i].suit)
  #print("Card: ", full_deck[i].card)
