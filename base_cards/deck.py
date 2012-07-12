class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        "Add card to deck."
        self.cards.append(card)

    def remove(self, card):
        "Remove card from deck."
        try:
            self.cards.remove(card)
        except ValueError:
            raise DeckError('card not exists')

    def remove_at(self, card_id):
        "Remove card at card_id from deck."
        try:
            card = self.cards[card_id]
            self.remove(self.cards[card_id])
            return card
        except DeckError:
            raise DeckError('card not exists')
        except IndexError:
            raise DeckError('invalid card number')

    def size(self):
        "Size of deck."
        return len(self.cards)

class DeckError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
            
