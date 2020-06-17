import random

class Card(object):
    """ represents an playing card """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        """ initializes card with suit and rank """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank

        if t1 > t2:
            return 1
        elif t1 < t2:
            return - 1
        else:
            return 0

class Deck(object):
    """ represents a deck of cards """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort(key=lambda Card: (Card.suit, Card.rank))

    def move_cards(self, hand, num):
        for _ in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_of_hands, num_of_cards):
        t = []
        for i in range(num_of_hands):
            h = Hand(label=f'hand_{i}')
            self.move_cards(h, num_of_cards)
            t.append(h)
        
        return t

class Hand(Deck):
    """ represents a hand of playing cards """
    def __init__(self, label=''):
        self.cards = []
        self.label = label

class PokerHand(Hand):

    def sort(self):
        """ sorts cards by rank then suit """
        self.cards.sort(key=lambda Card: (Card.rank, Card.suit))

    def suit_hist(self):
        """ builds a histogram of the suits that appear in hand
        stores result in attribute suits """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """ builds a histogram of the ranks that appear in hand
        stores results in attribute ranks """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """ returns true if the hand has flush, False otherwise """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5: return True
        return False

    def has_pair(self):
        """ returns True if the hand has a pair, False otherwise """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 2: return True
        return False

    def has_twopair(self):
        """ returns True if the hand has two pairs, False otherwise """
        self.rank_hist()
        counter = 0
        for val in self.ranks.values():
            if val == 2:
                counter += 1
            if counter == 2:
                return True
        return False

    def has_three(self):
        """ returns True if the hand has three of a kind, False otherwise """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 3: return True
        return False

    def has_staight(self):
        """ returns True if the hand has straight, False otherwise """
        straight = 0
        n = 0
        ace = False
        self.sort()
        for card in self.cards:
            if card.rank == n:
                continue
            elif card.rank == n + 1:
                straight += 1
                n = card.rank
            else:
                straight = 1
                n = card.rank

            if card.rank == 1:
                ace = True

            if card.rank == 12 and ace == True:
                straight += 1
            
            if straight == 5: return True
        return False

    def has_fullhouse(self):
        """ returns True if the hand has full house, False otherwise """
        self.rank_hist()
        flush = 0
        for val in self.ranks.values():
            if val == 2:
                flush += 1
            elif val >= 3:
                flush += 1

            if flush == 2:
                return True
        return False

    def has_four(self):
        """ returns True if the hand has four of a kind, False otherwise """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 4: return True
        return False
    
    def has_straighflush(self):
        """ returns True if the hand has a straight flush, False otherwise """
        if self.has_staight() and self.has_flush():
            return True
        return False


    def classify(self):
        """ changes label to highest value classification """
        if self.has_straighflush():
            self.label = 'Straight Flush'
        elif self.has_four():
            self.label = 'Four of a Kind'
        elif self.has_fullhouse():
            self.label = 'Full House'
        elif self.has_flush():
            self.label = 'Flush'
        elif self.has_staight():
            self.label = 'Straight'
        elif self.has_three():
            self.label = 'Three of a Kind'
        elif self.has_twopair():
            self.label = 'Two Pair'
        elif self.has_pair():
            self.label = 'Pair'
        else:
            self.label = 'High Card'