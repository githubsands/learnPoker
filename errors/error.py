class Error(Exception):
    pass

class WrongChipColorError(Error):
    """Raised when the wrong chip color is used"""

class AtLobbyCapacityError(Error):
    """Raised when a lobby is at capacity"""

class AtRoomCapacityError(Error):
    """Raised when a room is at capacity"""
