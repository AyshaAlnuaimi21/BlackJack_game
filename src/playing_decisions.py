from deck import Deck
from time import sleep

class PlayingDisions:
    '''This is the playing decision class for the blackjack game'''
    playerWallet = 30
    winingFlag = False
    losesFlag = False
    endGameFlag = True

    def __init__(self):
        self.deck = Deck()
        self.player = self.deck.player
        self.dealer = self.deck.dealer
        self.playeramount = self.PlaceMoney()

    def PlaceMoney(self):
        userinput = input("your wallet: {}\nPlace an amount:\n1\n5\n10\n".format(self.playerWallet))
        if userinput in ['1', '5', '10']:
            self.playeramount = int(userinput)
            print('PlaceMoney = ', self.playeramount)
            return self.playeramount

    def update_wallet(self):
        if self.winingFlag:
            self.playerWallet += self.playeramount
            self.winingFlag = False
        if self.losesFlag:
            self.playerWallet -= self.playeramount
            self.losesFlag = False

    def DoubleDision(self):
        self.playeramount *= 2
        print('doubled = ', self.playeramount)
        self.Dision(self.UserInputDision(), self.deck.totalcards(self.player), self.deck.totalcards(self.dealer))

    def HitDision(self):
        if self.deck.totalcards(self.player) < 21:
            self.deck.drawcard(self.player)
            self.Dision(self.UserInputDision(), self.deck.totalcards(self.player), self.deck.totalcards(self.dealer))

    def SplitDision(self):
        player_1 = [self.player[0]]
        player_2 = [self.player[1]]
        print(player_1)
        print(player_2)
        self.deck.drawcard(player_1)
        self.deck.drawcard(player_2)
    
    def StandDision(self):
        PTtotal = self.deck.totalcards(self.player)
        DTotal = self.deck.totalcards(self.dealer)
        if PTtotal < 21 and DTotal < 21:
            if PTtotal > DTotal:
                print("Player Wins!")
                print("Player Wallet:", self.playerWallet)
                self.winingFlag = True
            elif PTtotal < DTotal:
                print("Dealer Wins!")
                print("Player Wallet:", self.playerWallet)
                self.losesFlag = True
        elif PTtotal == 21:
            print("Player Wins!")
            print("Player Wallet:", self.playerWallet)
            self.winingFlag = True
        elif DTotal == 21:
            print("Dealer Wins!")
            print("Player Wallet:", self.playerWallet)
            self.losesFlag = True
        elif PTtotal > 21:
            print("Dealer Wins!")
            print("Player Wallet:", self.playerWallet)
            self.losesFlag = True
        elif DTotal > 21:
            print("Player Wins!")
            print("Player Wallet:", self.playerWallet)
            self.winingFlag = True
        elif PTtotal == DTotal:
            print("PUSH")
            print("Player Wallet:", self.playerWallet)


    def Dision(self, dision, PTtotal, DTotal):
        if dision == '1':
            self.HitDision()
        elif dision == '2':
            self.StandDision()
        elif dision == '3':
            self.DoubleDision()
        elif dision == '4':
            self.SplitDision()
        
        # Check if the player's wallet is empty
        if self.playerWallet <= 1:
            print("Your wallet is empty. Game over.")
            self.endGameFlag = False  # Set endGameFlag to False when the wallet is empty

    def UserInputDision(self):
        user_input = input("Choose your action:1.Hit\n2.Stand\n3.Double\n4.Split\n")
        return user_input

    