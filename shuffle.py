class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25

    >>> Shuffle.mongean([i for i in range (1,6)])

    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(num,int) and num >= 0
        assert isinstance(cards, list)

        temp_cards = cards.copy()
        if num == 0:
            return cards
        else:
            mid = len(temp_cards) // 2
            bound = num // 2

            if len(cards) % 2 == 0 and num % 2 == 1:
                moving_cards = temp_cards[mid - bound - 1: mid + bound]
                temp_cards[mid - bound - 1: mid + bound] = []
            elif num % 2 == 1 and len(cards) % 2 == 1:
                moving_cards = temp_cards[mid - bound: mid + bound + 1]
                temp_cards[mid - bound : mid + bound + 1] = []
            else:
                moving_cards = temp_cards[mid - bound : mid + bound]
                temp_cards[mid - bound : mid + bound] = []
            temp_cards = moving_cards + temp_cards
            return Shuffle.modified_overhand(temp_cards, num - 1)
    

    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times 
        restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        #odd top even bottom
        assert isinstance(cards, list)
        
        if len(cards) == 1:
            return [cards[0]]

        temp_cards = Shuffle.mongean(cards[:-1])

        if len(temp_cards) % 2 == 1:
            return [cards[-1]] + temp_cards
        else:
            return temp_cards + [cards[-1]]
