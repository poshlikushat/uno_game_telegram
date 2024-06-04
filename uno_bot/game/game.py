from .deck import Deck


class UNOGame:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.directions = 1  # Clockwise
        self.top_card = self.deck.draw_card()
        self.current_player_index = 0
        pass
