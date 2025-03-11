import random

class Card:
    def __init__(self, symbol: str, number: str):
        self.__symbol = symbol
        self.__number = number

    def get_score(self):
        if self.__number in ["J", "Q", "K"]:
            return [10]
        elif self.__number == "A":
            return [1, 11]
        else:
            return [int(self.__number)]

    def __str__(self):
        return f"{self.__symbol}:{self.__number} -> {",".join(str(score) for score in self.get_score())}"

class Deck:
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    symbols = ["♠", "♥", "♦", "♣"]
    def __init__(self):
        self.__deck = [Card(symbol, number) for number in self.numbers for symbol in self.symbols]
        self.suffle()

    def suffle(self):
        random.shuffle(self.__deck)

    def display_all_card(self):
        [print(c) for c in self.__deck]
        print(len(self.__deck))


d = Deck()
d.display_all_card()