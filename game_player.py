from game_card import Deck

class Entity:
    def __init__(self, name):
        self.__name = name
        self._cards = []

    def deal_card(self, deck:  Deck):
        card = deck.deal()
        self._cards.append(card)

class Dealer(Entity):
    def __init__(self, name):
        super().__init__(name)

    def show_card(self):
        print(self.__name)
        for _, card in enumerate(self._cards):
            if _ == 0:
                print(card)
            else:
                print("xx")
                
class Player(Entity):
    def __init__(self, name):
        super().__init__(name)

    def show_card(self):
        print(self.__name)
        for _, card in enumerate(self._cards):
            print(card)

