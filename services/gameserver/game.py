class Game:
    def __init__(players):
        self.players=players

    def start():
        deck = NewDeck()
        pot = Pot()

    def assign_position(players):
        """assign_position assigns each player a random position at the
            game servers table"""

        # asyncrously send these requests and wait
        requests = class_start_round_http_request()

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

