from rlcard.utils.utils import init_standard_deck
from rlcard.games.base import Card


class LimitHoldemDealer:
    def __init__(self, np_random, deck_head=None):
        self.np_random = np_random
        self.deck = init_standard_deck()
        self.shuffle()
        if deck_head is not None:
            print(deck_head)
            for card in self.deck:
                if str(card).lower() in deck_head:
                    self.deck.remove(card)
            deck_head = [Card(suit=c[1].upper(), rank=c[0]) for c in deck_head]
            print([str(card) for card in deck_head])
            self.deck = deck_head + self.deck
        print("deck", deck_head)
        assert len(self.deck) == 52
        exit()
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
