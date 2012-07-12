import sys
from unittest import TestCase
from test import support

sys.path.append('../')

from base_cards.card import Card
from base_cards.deck import Deck, DeckError


class BaseDeckOperationsTest(TestCase):
    def test_add(self):
        d = Deck() # create a new deck
        d.add(Card()) # add a card to the d deck

        self.assertEqual(1, d.size()) # d deck's size is 1?

    def test_remove(self):
        d = Deck() # create a new deck
        c = Card() # create a new card

        d.add(c) # add the c card to the d deck

        with self.assertRaises(DeckError):
            d.remove(Card()) # card doesnt exist?

        d.remove(c) # remove the c card from the d deck

        self.assertEqual(0, d.size()) # d deck's size is 0?
        with self.assertRaises(DeckError):
            d.remove(c) # d deck is empty, raised DeckError?
        self.assertEqual(0, d.size()) # d deck's size is still 0?
            
    def test_remove_at(self):
        d = Deck() # create a new deck
        c = Card() # create a new card

        d.add(c) # add the c card to the d deck

        with self.assertRaises(DeckError):
            d.remove_at(42) # card doesnt exist?
        self.assertEqual(c, d.remove_at(0)) # returns the removed card?
        self.assertEqual(0, d.size()) # d deck's size is 0?
        with self.assertRaises(DeckError):
            d.remove_at(0) # d deck is empty, raised DeckError?
        self.assertEqual(0, d.size()) # d deck's size is still 0?
        
if __name__ == '__main__':
    support.run_unittest(BaseDeckOperationsTest)
