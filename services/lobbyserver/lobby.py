class Lobby:
    """
    Defines the lobby of the game
    """

    def __init__(self, limit):
        self.rooms = ""

    def roomsplayers(player):
        while self.playerlimit > len(self.players)+1:
            try:
                self.players.append(player)
            except AtLobbyCapacityError:
                raise
