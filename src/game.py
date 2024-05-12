from playing_decisions import PlayingDisions
from time import sleep

def start_game():
    game = PlayingDisions()
    while game.endGameFlag:
        game.deck.shuffle_deck()
        game.player = []
        game.dealer = []
        game.deck.draw2cards(game.player)
        game.deck.draw2cards(game.dealer)
        sleep(0.5)
        game.Dision(game.UserInputDision(), game.deck.totalcards(game.player), game.deck.totalcards(game.dealer))
        game.update_wallet()
