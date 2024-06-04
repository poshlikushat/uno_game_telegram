from enum import Enum, auto


class Color(Enum):  # A class for keeping colors of cards
    RED = auto()
    YEllOW = auto()
    GREEN = auto()
    BlUE = auto()
    WILD = auto()


class CardType(Enum):  # A class for keeping card types of cards
    NUMBER = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    WILD = auto()
    WILD_DRAW_FOUR = auto()


class Card:
    def __init__(self, color, card_type, number=None):
        self.color = color
        self.card_type = card_type
        self.number = number

    def __str__(self):
        if self.card_type == CardType.NUMBER:  # If CardType == NUMBER
            return f'{self.color.name} {self.number}'  # Returning color and number
        else:  # If not NUMBER...
            return f'{self.color.name} {self.card_type.name}'  # ...returning color and card type
