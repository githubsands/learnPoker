class Game:
    def __init__(players):
        self.players=players

    def Start():
        deck = NewDeck()
        pot = Pot()

        preflop = PreFlop(players==players, deck==deck, pot==pot)
        preflop()

        # flop = Flop(players==players, deck==deck, pot==pot)
        # flop()

        # turn = Turn(players==players, deck==deck, pot==pot)
        # turn()

        # river = River(players==players, deck==deck, pot==pot)
        # river()

        # showdown = Showdown(players==players, deck==deck, pot==pot)
        # showdown()

            # wait for all

# TODO: learn async
# async MakeCardRequest(player):
    #pass`

