import objects


def start_game(players):
    players = len(players)
    game = Game()
    game.Start()
    deck = objects.Deck()

    deck.Deal(players):9

# http handler
def send_cards(players):
    for i in players:
        # http logic here
