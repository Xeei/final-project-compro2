from game_card import Deck

class Entity:
    def __init__(self):
        self._cards = []

    def deal_card(self, deck:  Deck):
        card = deck.deal()
        self._cards.append(card)

class Dealer(Entity):
    def __init__(self):
        super().__init__()

    def show_card(self):
        for _, card in enumerate(self._cards):
            if _ == 0:
                print(card)
            else:
                print("xx")
                
class Player(Entity):
    def __init__(self):
        super().__init__()

    def show_card(self):
        for _, card in enumerate(self._cards):
            print(card)

