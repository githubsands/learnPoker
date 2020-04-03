class Chip():
    """Chip defines the class for chips"""
    colors = ("White", "Blue", "Red")

    def __init__(self):
        set_color(color)

    def set_color(color):
        while color in colors:
            try:
                self.color = color
                break
            except WrongChipColorError:
                raise
