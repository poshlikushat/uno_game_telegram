import random
from .cards import Card, Color, CardType


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        random.shuffle(self.cards)

    def generate_deck(self):
        cards = []
        for color in (Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE):
            cards.append(Card(color, CardType.NUMBER, number=0))  # One 0-card for each color
            for number in range(1, 10):  # Two number-cards for each color
                cards.append(Card(color, CardType.NUMBER, number))
                cards.append(Card(color, CardType.NUMBER, number))
            for _ in range(2):  # Two cards with special type for each color
                cards.append(Card(color, CardType.SKIP))
                cards.append(Card(color, CardType.REVERSE))
                cards.append(Card(color, CardType.DRAW_TWO))
        for _ in range(4):  # Four cards WILD & WILD_DRAW_FOUR
            cards.append(Card(Color.WILD, CardType.WILD))
            cards.append(Card(Color.WILD, CardType.WILD_DRAW_FOUR))
        return cards

    def draw_card(self):
        return self.cards.pop()