class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible = True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        cardvals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suitvals = ['clubs', 'diamonds','hearts', 'spades']

        assert rank in cardvals
        assert suit in suitvals
        assert isinstance(visible, bool)

        self.rank = rank
        self.suit = suit 
        self.visible = visible 
        

    def __lt__(self, other_card):
        """
        Returns a boolean value if card1 is less than card2. 
        First compares rank, then compares suit
        """
        cardvals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suitvals = ['clubs', 'diamonds','hearts', 'spades']

        if cardvals.index(self.rank) < cardvals.index(other_card.rank):
            return True
        elif cardvals.index(self.rank) > cardvals.index(other_card.rank):
            return False
        else:
            if suitvals.index(self.suit) < suitvals.index(other_card.suit):
                return True
            elif suitvals.index(self.suit) > suitvals.index(other_card.suit):
                return False


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        suit_syms = {'clubs':'♣', 'diamonds':'♦', 'hearts':'♥', 'spades':'♠'}

        if self.visible:
            return  '____' + '\n' + '|' + str(self.rank) + '  |' + '\n' + \
            '| ' + suit_syms[self.suit] + ' |' + '\n' + '|__' + \
            str(self.rank) + '|'
        else:
            return '____' + '\n' + '|' + '?' + '  |' + '\n' + \
            '| ' + '?' + ' |' + '\n' + '|__' + '?' + '|'


    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """ 
        if self.visible:       
            return '(' + str(self.rank) + ', ' + self.suit + ')'
        else:
            return '(?, ?)'


    def get_rank(self):
        return self.rank
    

    def get_suit(self):
        return self.suit


    def get_visible(self):
        return self.visible


    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
    
    