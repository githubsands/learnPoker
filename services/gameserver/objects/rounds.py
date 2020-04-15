class Round():
    def __init__(self, players, deck, pot):
        self.players=players
        self.pot=pot

    def __call__(self):
        return self.play()

    def fold_player(self):
        """fold_player removes the given player from the list"""
        self.players.remove(player)

    def check():
        """a"""

    def send_cards():
        """send_cards sends the players there cards through http"""

    def ask_bet():
        """ask_bet ask the players for there chips through http"""

class PreFlop(Round):
    def play(self):
        for player in players:
            cards = deck.Deal(players)


class Flop(Round):
    pass

class Turn(Round):
   pass

class River(Round):
    pass


class ShowDown(Round):
    pass
