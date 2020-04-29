class Error(Exception):
    pass

class AtLobbyCapacityError(Error):
    """Raised when a lobby is at capacity"""
