class Error(Exception):
    pass

class WrongChipColorError(Error):
    """Raised when the wrong chip color is used"""

