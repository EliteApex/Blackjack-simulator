from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]
    
    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]
    
    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)

    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        cardvals = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']
        suitvals = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank,suit) for rank in cardvals for \
            suit in suitvals ]
        self.cards.sort()
        

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all([shuffle in ("modified_overhand", "mongean") \
            for shuffle in shuffle_and_count.keys()])

        if 'modified_overhand' in shuffle_and_count.keys():
            self.cards = Shuffle.modified_overhand(self.cards, \
                shuffle_and_count['modified_overhand'])

        if 'mongean' in shuffle_and_count.keys():
            for i in range(shuffle_and_count['mongean']):
                self.cards = Shuffle.mongean(self.cards)
    

    def deal_hand(self, hand, return_card = False):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand)

        card = self.cards.pop(0)
        hand.add_card(card)
        if return_card:
            return card


    def get_cards(self):
        return self.cards
