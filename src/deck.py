import random

class Deck:
    '''This is the deck class for the blackjack game'''
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

    def __init__(self):
        self.shuffle_deck()
        self.player = []
        self.dealer = []

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def totalcards(self, user):
        total = 0
        for card in user:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                total += int(card)
            elif card == 'A':
                total += 11
        return total

    def draw2cards(self, user):
        cards = []
        for _ in range(2):
            card = self.deck.pop()
            cards.append(card)
            user.append(card)
        print(user)
        return cards

    def drawcard(self, user):
        card = self.deck.pop()
        user.append(card)
        print(user)
        return card
