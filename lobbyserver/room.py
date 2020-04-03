class Room:
    """
    Defines the room of the game
    """

    def __init__(self, limit):
        self.players = ""
        self.playerlimit = limit

    def addplayers(player):
        while self.playerlimit > len(self.players)+1:
            try:
                self.players.append(player)
            except AtRoomCapacityError:
                raise
