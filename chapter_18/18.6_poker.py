from card_classes import Card, Deck, PokerHand

# make a deck
deck = Deck()
deck.shuffle()

# make hand
hand = PokerHand()
deck.move_cards(hand, 7)
hand.classify()

print(hand)
print(hand.label)