
import random

class Suit:
    color = ''

    def __init__(self, suit_val):
        self.color = suit_val

class Rank:
    val = None
    def __init__(self, number_val):
        self.val = number_val

class Card:
    suit = None
    rank = None
    def __init__(self, symbol, number):
       self.suit = Suit(symbol)
       self.rank = Rank(number)

    def __str__(self):
        return '{} : {}'.format(self.suit.color, self.rank.val)

class Deck:

    card = None

    def __init__(self, suitor, size):
        self.card = []
        shapes = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # makes the deck by adding the suits and ranks to the cards
        for suits in range(0, suitor):
            for ranks in range(1, size + 1):

                shapeVal = suits%4
                ranksVal = ranks%13
                # new_suit = Suit(shapes[shapeVal])
                # new_rank = Rank(ranks)
                # new_card = Card(new_suit, new_rank)
                new_card = Card(shapes[shapeVal], nums[ranksVal])
                self.add(new_card)

# prints the deck
    def print_cards(self):
        for card in self.card:
            print(card)

# add a new card, used to make the deck
    def add(self, card):
        self.card.append(card)

# shuffles the deck
    def shuffle(self):
        random.shuffle(self.card)


deck = Deck(4, 13)
deck.shuffle()
deck.print_cards()
# create a 4 element array with the suit strings to associate them with numbers

