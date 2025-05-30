from rlcard.utils.utils import init_standard_deck
from rlcard.games.base import Card


class LimitHoldemDealer:
    def __init__(self, np_random, deck_head=None):
        self.np_random = np_random
        self.deck = init_standard_deck()
        self.shuffle()
        if deck_head is not None:
            new_deck = []
            for card in self.deck:
                if card.rank+card.suit.lower() in deck_head:
                    continue
                new_deck.append(card)
            deck_head = [Card(suit=c[1].upper(), rank=c[0]) for c in deck_head]
            self.deck = new_deck + deck_head[::-1]
        assert len(self.deck) == 52
        self.pot = 0

    def shuffle(self):
        self.np_random.shuffle(self.deck)

    def deal_card(self):
        """
        Deal one card from the deck

        Returns:
            (Card): The drawn card from the deck
        """
        return self.deck.pop()
