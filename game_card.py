import random
import pygame as pg
from config import Config
import os
class Card:
    def __init__(self, symbol: str, number: str):
        self.__symbol = symbol
        self.__number = number
        self.__image = pg.transform.smoothscale(pg.image.load(os.path.join(Config.image_path, f"{self.__number+self.__symbol}.png")), (100, 150))
    def get_score(self):
        if self.__number in ["J", "Q", "K"]:
            return [10]
        elif self.__number == "A":
            return [1, 11]
        else:
            return [int(self.__number)]
        
    def show_card(self, screen, position):
        screen.blit(self.__image, (100,200))



    def __str__(self):
        return f"{self.__symbol}:{self.__number} -> {",".join(str(score) for score in self.get_score())}"

class Deck:
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    symbols = ["S", "H", "D", "C"]
    def __init__(self):
        self.__deck = [Card(symbol, number) for number in self.numbers for symbol in self.symbols]
        self.__back_deck = pg.transform.smoothscale(pg.image.load(os.path.join(Config.image_path, f"purple_back.png")), (100, 150))
        self.suffle()

    @property
    def remain(self):
        return len(self.__deck)

    def suffle(self):
        random.shuffle(self.__deck)

    def display_all_card(self, screen):
        for c in self.__deck:
            c.show_card(screen)

    def render(self, screen):
        screen.blit(self.__back_deck, (int(Config.screen_size[0]*0.85), int(Config.screen_size[1]*0.5-150/2)))
        
    def deal(self):
        card = self.__deck.pop()
        return card